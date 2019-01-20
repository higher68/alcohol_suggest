class Config(object):
    """
    アプリ基底クラス
    """
    # original config
    DEBUG = False
    TESTING = False

    # application specific config
    PORT = 5000
    

class ProductionConfig(Config):
    """
    本番環境設定
    """
    pass


class DevelopmentConfig(Config):
    """
    本番環境設定
    """
    DEBUG = True


class TestingConfig(Config):
    """
    テスト環境設定
    """
    TESTING = True


app_config = {
        'production': ProductionConfig,
        'development': DevelopmentConfig,
        'test': TestingConfig
        }

