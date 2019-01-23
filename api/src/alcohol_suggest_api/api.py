import traceback
from dataclasses import asdict

from flask import Blueprint, current_app as app, jsonify, make_response, request

from jsonschema.exceptions import ValidationError

from .classes import SuggestRequest, SuggestResponse, SuggestErrorResponse

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
        #TODO パラメータとして、一杯あたり何mlかをdbに定義する
        days = req.days
        glasses = req.glasses
        app.logger.info(f'alcohol suggest start: {days}days {glasses}glasses / week')
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
    except Exception as e:
        app.logger.error(e)


def make_candidate(amount_month):
    """候補県を計算

    Returns
    -------
    候補県のリスト
    """
    ## TODO DBから処理を取ってくるところ
    ## TODO 計算のロジック自体




def create_response(res, status_code=200):
    """レスポンス作成

    Returns
    ------
    flask.wrappers.Response
    """
    ## TODO

