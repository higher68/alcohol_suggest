from . import db


class Archives(db.Model):
    """
    archivesテーブルクラス
    """
    __tablename__ = 'archives'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prefecture = db.Column(db.Integer, nullable=False)
    sales = db.Column(db.Integer, nullable=False)
    consumption = db.Column(db.Integer, nullable=False)
    data_source_ver = db.Column(db.Integer, nullable=False)
