# 01. First Steps

- 문서: https://fastapi.tiangolo.com/tutorial/first-steps/
- 날짜: 10/26

## 핵심 한 줄
OpenApi는 API를 문서로 적기 위한 표준 형식이고, REST API는 웹에서 서버와 데이터를 주고받는 방식을 정한 설계 스타일로 URL(자원), HTTP메서드(동작)으로 구성된다.

## 배운 것
- uv: 파이썬 패키지와 프로젝트를 관리하는 도구. 아주 빠르다. 기존에 python3 -m venv .venv 하던 거를 uv venv로 하게 만들어준다
- option + esc를 통해 import할 수 있는 목록들이 뜬다.
- async def는 비동기 함수를 만들어주며, 비동기는 기다리는 동안 다른 일을 할 수 있다를 의미한다.
- /docs 문서로 연결하면 자동으로 Api 문서로 이동된다. (직접 실행 가능)
- /redoc 문서는 doc과 비슷한 또다른 Api 문서를 만들어준다. (읽기 좋음)
- FastAPI는 API를 정의하기 위한 OpenAPI 표준을 사용한다.
- @app.get("/"): FastAPI에게 바로 아래에 있는 함수가 다음으로 이동하는 요청을 처리한다는 것을 알려준다.
- /: 경로, get: 작동, root: 함수
- FastAPI Cloud에 애플리케이션 배포를 fastapi deploy로 간단하게 할 수 있다. 

## 직접 실험해본 것
<!-- 일부러 틀린 값 넣기, 순서 바꾸기, 타입 빼보기 등 → 결과 -->
- 시도: main.py 작성 후 dev 서버 키기
  - 결과: web에서 {"message":"Hello World"}가 보임

## 헷갈렸던 점 / 질문
- FastApi는 OpenAPI 표준을 기반으로 설계된 프레임워크라는데 OpenAPI가 뭐지?
  - API를 문서로 어떻게 적을지에 대한 표준
  - REST API를 설명하는 표준 형식. 각 경로가 어떤 파라미터를 받고 어떤 응답을 돌려주는지를 정해진 JSON/YAML 형식으로 적는다.

- REST API란?
  - 웹에서 서버와 데이터를 주고받는 방식을 정한 설계 스타일
  - URL로는 자원(명사)을 나타내고, HTTP 메서드로는 동작을 나타낸다.

## 더 알아볼 것