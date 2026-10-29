# 05. Query Parameters and String Validations

- 문서: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
- 날짜:

## 핵심 한 줄
매개변수에 대한 메타데이터를 넣고 싶다면, 파이썬의 Annotated와 Query 라이브러리들을 이용할 수 있다.

## 배운 것
- 매개변수 타입에 Annotated를 사용해 메타데이터 추가 가능
- 매개변수에 대한 추가 검증은 Query를 통해 가능

## 직접 실험해본 것
<!-- 일부러 틀린 값 넣기, 순서 바꾸기, 타입 빼보기 등 → 결과 -->
- 시도: Annotated, Qurey문 예제 종류별로 모두 타이핑 해보기
  - 결과: 성공

## 헷갈렸던 점 / 질문
- 매개변수에 대한 메타데이터가 왜 필요한 것일까? Annotated를 사용해야 되나?
  - 기본값 자리를 원래 의미대로 쓸 수 있다.
  ```python
  # 예전 방식
  async def read_items(q: str | None = Query(default=None, max_length=50), db: Session = Depends(get_db)):

  # Annotated 방식
  async def read_items(q: Annotated[str | None, Query(max_length=50)] = None, db: Annotated[Session, Depends(get_db)]):
  ```
  - 재사용이 쉽다. (자주 쓰는 의존성을 타입 별칭으로 만들어 두기 좋다)
  ```python
  DBsession = Annotated[Session, Depends(get_db)]
  CurrentUser = Annotated[User, Depends(get_current_user)]

  async def read_me(user: CurrentUser, db: DBSession)
  ```

## 더 알아볼 것
- 정규식 표현은 추후에 다시 공부해보기