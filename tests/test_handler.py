import json

import pytest

from mangajj import app


@pytest.fixture()
def apigw_event():
    return {
        "resource": "/{proxy+}",
        "requestContext": {},
        "queryStringParameters": {"title": "naruto", "chapter": "1"},
        "headers": {},
        "httpMethod": "GET",
        "path": "/chapter"
    }


def test_lambda_handler(apigw_event):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "manga_title" in ret["body"]
    assert data["manga_title"] == "naruto"
    # assert "location" in data.dict_keys()
