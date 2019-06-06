from sqlalchemy import inspect

from . import db
from ..common_method import start_session


class Settings(db.Model):
    """
    settingsテーブルクラス
    """
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    past_length = db.Column(db.Integer, nullable=False)
    candidate_num = db.Column(db.Integer, nullable=False)
    alcohol_consumption_lower_limit = db.Column(db.Integer, nullable=False)
    drink_days_upper_limit = db.Column(db.Integer, nullable=False)

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

        with start_session() as session:
            settings = session.query(Settings).first()
        print({c.key: getattr(settings, c.key)
               for c in inspect(settings).mapper.column_attrs})
        return {c.key: getattr(settings, c.key) for c in inspect(settings).mapper.column_attrs}
