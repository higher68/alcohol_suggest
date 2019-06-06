
from contextlib import contextmanager

from api.classes.alcoloh_suggest import ErrorResponse

from dataclass import asdict

from flask import jsonify, make_response

from sqlalchemy.orm import sessionmaker

from .models import db


def create_response(res=None, status_code=200):
    """
    レスポンス作成

    Parameters
    ----------
    res: class
        レスポンスクラス
    status_code: int
        ステータスコード

    Returns
    -------
    flask.wrappers.Response
        レスポンス
    """
    if res is None:
        res = {}
        return make_response(jsonify(res), status_code)
    return make_response(jsonify(asdict(res)), status_code)


def create_error_responze(error_message, status_code):
    """
    エラー時レスポンス作成

    Parameters
    ----------
    error_message: str
        エラーメッセージ
    status_code: int
        ステータスコード

    Returns
    -------
    flask.wrappers.Response
        レスポンス
    """
    res = ErrorResponse(error_message)
    return create_response(res, status_code)


@contextmanager
def start_session(commit=False):
    """
    SQLAlchemyのセッション管理。
    commit: bool
        True: セッション処理後コミット
        False: セッション処理後にコミットしない
    """
    Session = sessionmaker(bind=db.engine)
    try:
        session = Session()
        try:
            # トランザクション処理を開始
            yield session
            if commit:
                session.commit()
        except Exception:
            # 例外発生時はトランザクションをロールバック、例外をraise
            session.rollback()
            raise
    finally:
        # トランザクション処理あとにセッションをクローズ
        if session is not None:
            session.close()
