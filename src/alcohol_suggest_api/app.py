import logging.config
import os
import traceback
from logging import getLogger

from flask import Flask

from .config import app_config
from .models import db
from .models.settings import Settings

# from .api.mock import mock
# from tests import test


def create_app(flask_env='production',
               logging_conf_path='../conf/logging.conf',
               app_conf_path='../conf/alcohol_suggest.cfg'):
    """アプリインスタンス作成

    Parameters
    ----------
    flask_env : {'production', 'development', 'test'}, optional, default 'production'
        アプリ実行環境
        - production: 本番環境
        - development: 開発環境
        - test: テスト環境
    logging_conf_path: str, optional, default '../conf/logging.conf'
        ログ設定ファイルパス

    Returns
    -------
    flask.app.Flask
        アプリインスタンス
    """
    app = Flask(__name__)

    # logging設定
    logging.config.fileConfig(logging_conf_path)
    app.logger = getLogger(__name__)

    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config.from_object(app_config[flask_env])
    if os.path.exists(app_conf_path):
        app.config.from_pyfile(app_conf_path)
    else:
        app.logger.warning(f"Config file is not exists: {app_conf_path}")

    # dbの初期化
    db.init_app(app)
    # api部分が作れたら実装
    # app.register_blueprint(api)

#    if flask_env == 'development':
#        app.register_blueprint(mock)
#    if flask_env == 'test':
#        app.register_blueprint(test)
    try:
        with app.app_context():
            app.settings = Settings.get_settings
    except Exception as e:
        app.logger.error(f"{e}\n{traceback.format_exec()}")
        raise e

    return app
