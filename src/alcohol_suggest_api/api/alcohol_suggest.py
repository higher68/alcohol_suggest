import traceback
from datetime import datetime

from flask import Blueprint
from flask import current_app as app
from flask import jsonify, make_response, request

from jsonschema.exceptions import ValidationError

from .classes import SuggestErrorResponse, SuggestRequest, SuggestResponse
from ..common_method import create_response, start_session
from ..constants import ApiResultCode as code, get_error_message
from ..models.archives import Archives
from ..models.settings import Settings

api = Blueprint('api', __name__, url_prefix='/api')
with start_session() as session:
    settings = session.query(Settings).first()


@api.route('/suggest', methods=['POST'])
def suggest_prefecture():
    """alcohol_suggest_spi処理関数

    Parameters
    ----------
    なし

    Returns
    -------
    flask.wrappers.Response
        レスポンス
    """
    try:
        req = SuggestRequest.from_dict(request.json)
        validate_result_code = _validate_alcohol_suggest(req, settings)
        if validate_result_code != code.OK:
            return ValidationError(get_error_message(validate_result_code))
        # TODO パラメータとして、一杯あたり何mlかをdbに定義する
        days = req.days
        glasses = req.glasses
        app.logger.info(
            f'alcohol suggest start: {days}days {glasses}glasses / week')
        app.logger.info('1日あたりの飲酒量計算')
        amount_day = settings.ml_of_1glass * days * glasses / 7
        app.logger.info('1月(30日)あたりの飲酒量計算')
        amount_month = amount_day * 30
        results = make_candidate(amount_month)
        res = SuggestResponse(results)
        app.logger.info("処理が正常終了しました。")
        return create_response(res)

    except ValidationError as e:
        if e.validator == "required":
            app.logger.error(e)
            return create_response(get_error_message(code.VALIDATION_REQUIRED_ERROR), 400)
        elif e.validator == "type":
            app.logger.error(e)
            return create_response(get_error_message(code.VALIDATION_TYPE_ERROR), 400)
        else:
            app.logger.error(e)
            app.logger.error(traceback.format_exc())
            return create_response(e.message, 400)
    except Exception as e:
        app.logger.error(e)
        app.logger.error(traceback.format_exc())
        return create_response(get_error_message(code.SERVER_ERROR), 500)


def make_candidate(amount_month):
    """候補県を取得

    Returns
    -------
    候補県のリスト
    """
    # TODO DBから候補県を年代で絞ってとってくる
    this_year = datetime.datetime.now().year
    with start_session() as session:
        query = Archives.prefecture, Archives.consumption, Archives.sales
        query_filter = (Archives.data_source_ver ==
                        this_year - settings.past_length)
        session.query(query).filter(query_filter)
    # TODO 計算のロジック自体


def _validate_alcohol_suggest(request_data, settings):
    """
    リクエストのalcohol_suggest要素のバリデーションチェック

    Parameters
    ----------
    request_data: SuggestReques
        リクエストクラス

    Returns
    -------
    ret: ApiResultCode
        ==OK: バリデーションエラーなし
        !=OK: バリデーションエラーあり
    """
    if request_data.days > settings.drink_days_upper_limit:
        return code.VALIDATION_DAYS_UPPER_LIMIT_ERROR
    if request_data.glasses < settings.alcohol_consumption_lower_limit:
        return code.VALIDATION_CONSUMPTION_LOWER_LIMIT_ERROR
    if request_data.glasses < settings.number_of_output_upper_limit:
        return code.VALIDATION_OUTPUTNUM_UPPER_LIMIT_ERROR

    return code.OK
