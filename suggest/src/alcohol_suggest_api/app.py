import logging.config  ### loggingをconfから読み込む
from logging import getLogger

from flask import Flask

## CONFIG_PATH = '../conf/.cfg'

def create_app(flask_env='production', logging_conf_path='../conf/logging.conf'):
    """アプリインスタンス作成

    Parameters
    ----------
    flask_env : {'production', 'development', 'test'}, optional, default 'prodection'
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
    
    ## logging設定
    logging.config.fileConfig(logging_conf_path)
    app.logger = getLogger(__name__)
    
    app.config['JSON_AS_ASCII'] = False

    # config fileで設定を読み込むようにしたほうがいいが、未実装

    # api部分が作れたら実装 
    # app.register_blueprint(api)

    return app
