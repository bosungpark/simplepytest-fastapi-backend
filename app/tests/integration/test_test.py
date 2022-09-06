"""
integration 테스트 파일입니다.
"""
from app.main import add

def test_fixture(numbers):
    """
    conftest.py에서 정의한 fixture, numbers가 적절한 데이터를 생성하는지 테스트합니다.
    """
    assert add(*numbers[:2]) == numbers[0] + numbers[1]


def test_db(db):
    """
    conftest.py에서 정의한 fixture, db가 종료된 뒤, 뒤처리를 제대로 하는지 테스트합니다.
    """
    assert db == {"something":1,"somethingelse":2}