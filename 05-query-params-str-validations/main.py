# FastAPI를 사용하면 매개변수에 대한 추가 정보 및 검증을 선언할 수 있다.
# 이 애플리케이션을 예로 들어보자.

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 추가 검증
"""
q가 선택적이지만 값이 주어질 때마다 길이가 50자를 초과하지 않게 강제하려 합니다.

Query와 Annotated 임포트
이를 위해 먼저 다음을 임포트합니다.

fastapi에서 Query
typing에서 Annotated

Annotated를 사용해 매개변수에 메타데이터를 추가할 수 있다.
"""
# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()

# q: Annotated[str | None] = None으로 감싸면
# q는 str 또는 None이 될 수 있는 매개변수이며 기본값은 None이다.
# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 검증 더 추가하기
# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 정규식 추가
# 매개변수와 일치해야 하는 정규 표현식 pattern을 정의할 수도 있다.
# ^ : 뒤따르는 문자로 시작하며, 앞에는 문자가 없다.
# fixedquery: 정확히 fixedquery 갑승ㄹ 가집니다.
# $ 여기서 끝나며, fixedquery 이후로 더 이상 문자가 없습니다.
# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 필수지만 None 가능
# from typing import Annotated
# from fastapi import FastAPI, Query
# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3)]):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 쿼리 매개변수 리스트 / 다중값
# Query로 쿼리 매개변수를 명시적으로 정의할 때 값들의 리스트를 받도록 선언할 수 있고
# 다른 말로 하면 여러 값을 받도록 선언할 수도 있다.
# 예를 들어, URL에서 여러 번 나타날 수 있는 q 쿼리 매개변수를 선언하려면 다음과 같이 작성할 수 있다.
# list 타입으로 쿼리 매개변수를 선언하려면 Query를 명시적으로 사용해야 한다.
# http://localhost:8000/items/?q=foo&q=bar
# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items

# 더 많은 메타데이터 선언
# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# description도 추가 가능하다
# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title = "Query string",
#             description = "Query string for items to search in the database that have a good match",
#             min_length = 3,
#         ),
#     ] = None,
# ):

#     results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 별칭 매개변수
"""
파이썬에서는 -를 변수명에 넣지 못한다.
매개변수가 item-query이길 원한다면, alias를 선언할 수 있다.
"""
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"items_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

