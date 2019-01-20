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

    except ValidationError as e:
        app.logger.error(e)
    except Exception as e:
        app.logger.error(e)

