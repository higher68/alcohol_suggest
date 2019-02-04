from sqlalchemy import inspect
from sqlalchemy.dialects import postgresql

from . import db


class Settings(db.Model):
    """
    settingsテーブルクラス
    """
    __tablename__ = 'settings'
    id = db.Column(db.Intger, primary_key=True, autoincrement=True)
    past_length = db.column(db.Integer, nullable=False)
    candidate_num = db.column(db.Integer, nullable=False)

@staticmethod
def get_settings():
    """
    設定取得

    Parameters
    ----------
    なし

    Returns
    -------
    dict
        各種設定情報

    """
    pass
