from dataclasses import dataclass
from typing import List

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
    days : int
    glasses : int



