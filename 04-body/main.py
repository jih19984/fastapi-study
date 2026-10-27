# 클라이언트로부터 여러분의 API로 데이터를 보내야 할 때, 요청 본문으로 보냅니다.
# 요청 본문은 클라이언트에서 API로 보내지는 데이터 입니다. 
# 응답 본문은 API가 클라이언트로 보내는 데이터 입니다.
# 여러분의 API는 대부분의 경우 응답 본문을 보내야 합니다. 하지만 클라이언트는 항상 요청 본문을 보낼
# 필요는 없고, 때로는 (쿼리 매개변수와 함께) 어떤 경로만 요청하고 본문은 보내지 않을 수도 있다.

"""
요청 본문을 선언하기 위해서 모든 강력함과 이점을 갖춘 Pydantic 모델을 사용합니다.
"""

# 먼저 pydantic에서 BaseModel을 임포트해야 합니다.
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# 1. 반환 타입 힌트를 지정해주지 않으면 FastApi가 응답 타입을 모른다!
# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item

# 2. 모델 사용하기
# 함수 안에서 모델 객체의 모든 어트리뷰트에 직접 접근 가능하다.
# model_dump 메서드는 Pydantic 모델 객체를 파이썬 딕셔너리로 바꿔주는 메서드
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# 3. 요청 본문 + 경로 매개변수 + 쿼리 매개변수
# 경로 매개변수와 요청 본문, 쿼리 매개변수를 동시에 선언할 수 있다.
# **은 딕셔너리를 풀어서 언패킹해 그 안의 키-값들을 그대로 펼쳐 넣는 문법이다.
# 만일 매개변수가 단일 타입으로 되어있으면, 쿼리 매개변수로 해석될 것이다.
# 만약 매개변수가 Pydantic 모델 타입으로 선언 되어있으면, 요청 본문으로 해석될 것이다.
@app.put("/items/{item_id}")
async def update_item(item_id : int, item: Item, q: str | None = None):
    result = {"item_id" : item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
