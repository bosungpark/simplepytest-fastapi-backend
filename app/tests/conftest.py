"""
conftest.py

Pytest 에서 공통으로 사용되는 Fixture / Plugin / Module을 모아두는 파일
conftest.py은 도메인 모듈(디렉토리)별로 나눠서 관리

Fixture: requiring network access depend on connectivity and are usually time-expensive to create. 
scope: be invoked once per function, classes, modules, packages or session
"""
import pytest
import random

@pytest.fixture(scope="function")
def numbers():
    """
    간단한 테스트 데이터를 생성하는 함수
    마치 클래스의 __enter__ 함수와 같이 활용할 수 있다.
    """
    return [random.randrange(10) for _ in range(10)]

@pytest.fixture(scope="function")
def db(): 
    """
    간단한 테스트를 위한 fake_db
    클래스의 __exit__ 함수와 같이 함수의 종료시점에 처리되어야할 문제를 정의했다.
    """
    data = {"something":1,"somethingelse":2} 
    yield data
    data = {}
    print("db 리셋하고 커넥션 닫을게요~~")
