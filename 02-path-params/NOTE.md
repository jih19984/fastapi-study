# 02. Path Parameters

- 문서: https://fastapi.tiangolo.com/tutorial/path-params/
- 날짜:

## 핵심 한 줄
사용자가 입력가능한 매개변수의 도메인을 정하고 싶을 때 파이썬의 enum을 사용할 수 있다.

## 배운 것
- 함수 매개변수에 type assertion을 하면 FastApi는 데이터 검증을 한다.
- pydantic
  - 모든 데이터 검증이 Pydantic을 통해 내부적으로 이뤄진다.
- 경로 처리는 순차적으로 이뤄지기 때문에 선언 순서를 반드시 확인해야 한다. (좁은 범위를 먼저)
  ```py
  # /{user_id}가 먼저 선언되어 있어 /users/me까지 가지 못한다.
  @app.get("/users/{user_id}")
  async def read_user(user_id: str):
      return {"user_id": user_id}

  @app.get("/users/me")
  async def read_user_me():
      return {"user_id": "the current user"}
  ```
- 경로 정의를 재정의할 수 없다. (앞에 것이 먼저 매칭)
- 경로 매개변수를 받는 경로 처리가 있고, 가능한 유효한 경로 매개변수 값들을 미리 정의하고 싶다면 Python 표준 Enum을 사용할 수 있다.
- 
## 직접 실험해본 것
<!-- 일부러 틀린 값 넣기, 순서 바꾸기, 타입 빼보기 등 → 결과 -->
- 시도: Enum을 통해서 경로 매개변수 정의하고 실행해보기
  - 결과: 정상적으로 Swagger 문서에 반영됨

## 헷갈렸던 점 / 질문
- model_name이 ModelName이라는 객체 타입으로 들어가는데 어떻게 조건문에서 비교가 가능한가?
  - FastApi가 문자열을 Enum 멤버로 바꿔서 넘겨준다!
  - FastApi가 내부적으로 Pydantic을 통해 이 값을 검증하고 변환해준다.
  - 즉, ModelName.alexnet이라는 멤버 객체로 변환된다.

## 더 알아볼 것
- enum은 항상 써도 좋은가?
  - 값이 자주 바뀌거나 DB에서 관리되는 목록이라면 enum은 맞지 않다.