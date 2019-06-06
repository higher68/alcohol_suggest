from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class SuggestRequest(JsonSchemaMixin):
    """リクエストクラス

    Attributes
    ----------
    days : int
        1週間の飲酒日数
    glasses : int
        飲酒量・・・単位=杯
    """
    days: int
    glasses: int


@dataclass
class SuggestResponse(JsonSchemaMixin):
    """レスポンスクラス

    Attributes
    ---------
    prefecture
        出身県候補
    """
    # TODO Atttributeをlistに
    prefecture: str = ''


@dataclass
class SuggestErrorResponse(JsonSchemaMixin):
    """エラーレスポンスクラス

    Attributes
    ----------
    error_message : str
        エラーメッセージ
    """
    error_message: str = ''
