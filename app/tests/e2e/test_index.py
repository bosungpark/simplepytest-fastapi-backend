"""
e2e 테스트 파일입니다.
"""
from fastapi.testclient import TestClient
from app.main import app

def test_index():
    """
    간단한 api 테스트 함수입니다.
    """
    with TestClient(app) as client:
        res = client.get("/")
        assert res.status_code == 200