from . import db


class Archive(db.Model):
    """
    archiveテーブルクラス
    """
    __tablename__ = 'archive'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prefecture = db.Column(db.Integer, nullable=False)
    sales = db.Column(db.Integer, nullable=False)
    consumption = db.Column(db.Integer, nullable=False)
