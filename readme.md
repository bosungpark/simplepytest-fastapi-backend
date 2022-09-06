**환경설정**

- 가상환경 켜기: pipenv shell

- 필요한 패키지 설치: pipenv install --dev

- pytest 실행 명령: pytest

**테스트 layer 구분**

테스트 피라미드: 

- 동화된 테스트를 어떻게 효율적으로 만들지 고민하기 위해 만들어진 형태

- 고수준 테스트를 만들기 보다는 최대한 저수준의 유닛테스트를 많이 만들어야 한다

![테스트 피라미드](https://user-images.githubusercontent.com/81157873/188581836-a07dc1db-5ce4-41a7-b1e7-5db54f7aee47.png){: width="100" height="100"}

- E2E: 가장 직관적인 레벨, 이 단계에서 문제가 생긴다면 요청, 파싱, 리턴 값 등을 의심해 볼 수 있다.

- Integration: 실제 서비스가 잘 작동하는지, 도입한 기술이 문제는 없는지 등에 대한 통합 테스트를 하는 레벨, E2E가 api 사이의 상호작용이라면, Integration은 프로젝트 내부의 상호작용을 다룬다고 이해했다.

- Functional: 

- Unit: 전체 코드 중에 아주 작은 부분을 테스트 하는 것, 함수 하나 하나 테스트 코드를 작성하는 것이 해당된다.

- domain: 