import os
import pytest
from alcohol_suggest import create_app

conf_dir = os.path.join(os.dirname(os.path.abspath(__file__)), '../conf')
logging_conf_path = os.path.join(conf_dir, 'logging_conf')


@pytest.fixture(scope='function', autouse=True)
def scope_function():
    app = create_app(flask_env='test', logging_conf_path=logging_conf_path)
    app.app_context().push()
