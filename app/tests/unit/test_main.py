"""
유닛 테스트 파일입니다.
"""
from app.main import add

def test_add():
    """
    간단한 유닛 테스트 함수
    """
    assert add(3,4) == 7