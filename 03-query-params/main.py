# 경로 매개변수의 일부가 아닌 다른 함수의 매개변수를 선언하면 "쿼리" 매개변수로 자동해석한다.
# 쿼리 매개변수는 경로에서 고정된 부분이 아니기 때문에 선택적일 수 있고 기본값을 가질 수도 있다.

# from fastapi import FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, 
#                  {"item_name": "Bar"},
#                  {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip:skip+limit]

# 선택적 매개변수
# 같은 방법으로 기본값을 None으로 설정하여 선택적 매개변수를 선언할 수 있다.
# 이 경우 함수 매개변수 q는 선택적이며, 기본값으로 None 값이 된다. 
# 경로 매개변수와 함수 쿼리 매개변수는 다르다는 것을 알정도로 똑똑하다!
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: int = 0, q: int | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# 쿼리 매개변수 형변환
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# 여러 경로 / 쿼리 매개변수
# 여러 경로 매개변수와 쿼리 매개변수를 동시에 선언할 수 있으며 FastAPI는 어느 것이 무언인지 알고 있습니다.
# 그리고 특정 순서로 선언할 필요가 없습니다.
# 매개변수들은 이름으로 감지됩니다.

# 필수 쿼리 매개변수
# 경로가 아닌 매개변수에 대한 기본값을 선언할 때 해당 매개변수는 필수적이지 않았다.
# 특정값을 춫가하지 않고 선택적으로 만들기 위해선 기본값을 None으로 설정하면된다.
# 그러나 쿼리 매개변수를 필수로 만들려면 단순히 기본값을 선언하지 않으면 된다.
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

# 경로 매개변수와 마찬가지로 Enum을 사용할 수 있다.
from fastapi import FastAPI
from enum import IntEnum

app = FastAPI()

class ItemType(IntEnum):
    item_x = 1
    item_y = 2
    item_z = 3

@app.get("/items/{item_id}")
async def read_item_id(item_id : ItemType):
    if item_id is ItemType.item_x:
        return {"item_id" : item_id, "message": "x 아이템"}
    elif item_id == 2:
        return {"item_id" : item_id.value}
    elif item_id == 3:
        return {"item_id" : item_id.value}