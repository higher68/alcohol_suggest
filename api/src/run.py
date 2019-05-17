import os

from alcohol_suggest_api import create_app

"""
suggestAPIアプリケーション起動
"""
conf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf')
logging_conf_path = os.path.join(conf_dir, 'logging.conf')
app_conf_path = os.path.join(conf_dir, 'alcohol_suggest.cfg')

flask_env = os.getenv('FLASK_ENV', 'production')
app = create_app(flask_env, logging_conf_path, app_conf_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
