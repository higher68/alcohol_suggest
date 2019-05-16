from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from .models import db

def create_response(res=None, status_code=200):
    """
    レスポンス作成

    Parameters
    ----------


    Returns
    -------
    """
    pass


def create_error_responze(error_message, status_code):
    """
    エラー時レスポンス作成

    Parameters
    ----------

    Returns
    -------
    """


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
