""" データタイプに関するテスト """
import json
import os
import pytest


@pytest.fixture
def response_json():
    """レスポンスのjsonを定義
    """
    data_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'datas')
    response_dir = os.path.join(data_dir, 'response')
    with open(response_dir, encoding='utf-8') as fin:
        data = json.load(fin)
    return data


@pytest.fixture
def request_json():
    """リクエストのjsonを定義
    """
    data_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'datas')
    request_dir = os.path.join(data_dir, 'request')
    with open(request_dir, encoding='utf-8') as fin:
        data = json.load(fin)
    return data


def test_suggest(client, request_json, response_json):
    response = client.post('suggest', data=request_json)
    assert response == response_json
