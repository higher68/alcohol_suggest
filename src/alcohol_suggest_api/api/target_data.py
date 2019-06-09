import traceback

from flask import Blueprint
from flask import current_app as app
from flask import jsonify, make_response, request

from jsonschema.exceptions import ValidationError

from .classes import SuggestErrorResponse, SuggestRequest, SuggestResponse
from ..common_method import create_response, start_session
from ..constants import ApiResultCode as code, get_error_message
from ..models.settings import Settings

api = Blueprint('target_data', __name__, url_prefix='/target_data')


@api.route('/register', methods=['POST'])
def suggest_prefecture():
    """過去データ登録用エンドポイント

    Parameters
    ----------
    なし

    Returns
    -------
    flask.wrappers.Response
        レスポンス
    """
    pass


def _validate_alcohol_suggest(request_data, settings):
    """
    リクエストのバリデーションチェック

    Parameters
    ----------
    request_data: TODO
        リクエストクラス

    Returns
    -------
    ret: ApiResultCode
        ==OK: バリデーションエラーなし
        !=OK: バリデーションエラーあり
    """
    pass
