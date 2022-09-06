"""
테스트 할 메서드들을 정의한 파일입니다.
당연한 이야기이지만, 이 공간에서 테스트 메서드를 참조하는 것은 순환참조가 발생할 수 있기 때문에 지양해야합니다.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    """
    e2e 통신 테스트를 위한 간단한 api
    """
    return 

def add(x,y):
    """
    unit 테스트를 위한 간단한 덧셈 함수
    """
    return x+y