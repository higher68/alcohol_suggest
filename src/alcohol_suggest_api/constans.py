from enum import IntEnum


class ApiResultCode(IntEnum):
    """
    処理結果コード
    """
    OK = 0
    VALIDATION_REQUIRED_ERROR = 101
    VALIDATION_TYPE_ERROR = 101
    VALIDATION_CONSUMPTION_LOWER_LIMIT_ERROR = 103
    VALIDATION_DAYS_UPPER_LIMIT_ERROR = 104


def get_error_message(result_code):
    """
    エラーメッセージ取得

    Parameters
    ----------
    result_code: ApiResultCode
        処理結果コード

    Returns
    -------
    str
        エラーメッセージ

    """
    _error_messages = {
        ApiResultCode.VALIDATION_REQUIRED_ERROR: "リクエストの必須項目が足りません",
        ApiResultCode.VALIDATION_TYPE_ERROR: "リクエストの入力値が不正です",
        ApiResultCode.VALIDATION_CONSUMPTION_LOWER_LIMIT_ERROR: "リクエストの入力値が最小値を下回っています",
        ApiResultCode.VALIDATION_DAYS_UPPER_LIMIT_ERROR: "リクエストの入力値が最大値を上回っています"
    }
    return _error_messages[result_code]
