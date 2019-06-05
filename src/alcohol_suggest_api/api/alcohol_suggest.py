import traceback

from flask import Blueprint
from flask import current_app as app
from flask import jsonify, make_response, request

from jsonschema.exceptions import ValidationError

from .classes import SuggestErrorResponse, SuggestRequest, SuggestResponse
from ..common_method import create_response, start_session
from ..constans import ApiResultCode as code, get_error_message
from ..models.settings import Settings

api = Blueprint('api', __name__, url_prefix='/api')


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
        with start_session() as session:
            settings = session.query(Settings).first()
        validate_result_code = _validate_alcohol_suggest(req, settings)
        if validate_result_code != code.OK:
            return ValidationError(get_error_message(validate_result_code))
        # TODO パラメータとして、一杯あたり何mlかをdbに定義する
        days = req.days
        glasses = req.glasses
        app.logger.info(
            f'alcohol suggest start: {days}days {glasses}glasses / week')
        jug = 350
        app.logger.info('1日あたりの飲酒量計算')
        amount_day = jug * days * glasses / 7
        app.logger.info('1月(30日)あたりの飲酒量計算')
        amount_month = amount_day * 30
        results = make_candidate(amount_month)
        res = SuggestResponse(results)

        return create_response(res)

    except ValidationError as e:
        app.logger.error(e)
        app.logger.error(traceback.format_exc())
        return create_response()
    except Exception as e:
        app.logger.error(e)
        app.logger.error(traceback.format_exc())


def make_candidate(amount_month):
    """候補県を計算

    Returns
    -------
    候補県のリスト
    """
    # TODO DBから処理を取ってくるところ
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
    if request_data.days <= settings.drink_days_upper_limit:
        return code.VALIDATION_CONSUMPTION_LOWER_LIMIT_ERROR
