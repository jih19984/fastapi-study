# FastAPI Study

[FastAPI 공식문서 Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)를 순서대로 따라가며 실습한 기록.

## 진행 방식
1. 챕터 문서를 읽는다
2. 해당 폴더에 `main.py`를 **직접 타이핑**한다 (복붙 금지)
3. `fastapi dev NN-chapter/main.py` 실행 → `http://127.0.0.1:8000/docs` 에서 호출해본다
4. 일부러 깨뜨려보며 실험하고, 결과를 `NOTE.md`에 기록한다
5. 챕터 하나 끝나면 커밋 (`git commit -m "NN chapter-name"`)

## 환경 세팅
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 진도표
상태: ⬜ 시작 전 · 🟨 진행 중 · ✅ 완료

| # | 챕터 | 노트 | 상태 |
|---|------|------|------|
| 01 | [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) | [NOTE](01-first-steps/NOTE.md) | ✅ |
| 02 | [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/) | [NOTE](02-path-params/NOTE.md) | ✅ |
| 03 | [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/) | [NOTE](03-query-params/NOTE.md) | ✅ |
| 04 | [Request Body](https://fastapi.tiangolo.com/tutorial/body/) | [NOTE](04-body/NOTE.md) | ✅ |
| 05 | [Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) | [NOTE](05-query-params-str-validations/NOTE.md) | ⬜ |
| 06 | [Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/) | [NOTE](06-path-params-numeric-validations/NOTE.md) | ⬜ |
| 07 | [Query Parameter Models](https://fastapi.tiangolo.com/tutorial/query-param-models/) | [NOTE](07-query-param-models/NOTE.md) | ⬜ |
| 08 | [Body - Multiple Parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/) | [NOTE](08-body-multiple-params/NOTE.md) | ⬜ |
| 09 | [Body - Fields](https://fastapi.tiangolo.com/tutorial/body-fields/) | [NOTE](09-body-fields/NOTE.md) | ⬜ |
| 10 | [Body - Nested Models](https://fastapi.tiangolo.com/tutorial/body-nested-models/) | [NOTE](10-body-nested-models/NOTE.md) | ⬜ |
| 11 | [Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) | [NOTE](11-schema-extra-example/NOTE.md) | ⬜ |
| 12 | [Extra Data Types](https://fastapi.tiangolo.com/tutorial/extra-data-types/) | [NOTE](12-extra-data-types/NOTE.md) | ⬜ |
| 13 | [Cookie Parameters](https://fastapi.tiangolo.com/tutorial/cookie-params/) | [NOTE](13-cookie-params/NOTE.md) | ⬜ |
| 14 | [Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/) | [NOTE](14-header-params/NOTE.md) | ⬜ |
| 15 | [Cookie Parameter Models](https://fastapi.tiangolo.com/tutorial/cookie-param-models/) | [NOTE](15-cookie-param-models/NOTE.md) | ⬜ |
| 16 | [Header Parameter Models](https://fastapi.tiangolo.com/tutorial/header-param-models/) | [NOTE](16-header-param-models/NOTE.md) | ⬜ |
| 17 | [Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/) | [NOTE](17-response-model/NOTE.md) | ⬜ |
| 18 | [Extra Models](https://fastapi.tiangolo.com/tutorial/extra-models/) | [NOTE](18-extra-models/NOTE.md) | ⬜ |
| 19 | [Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/) | [NOTE](19-response-status-code/NOTE.md) | ⬜ |
| 20 | [Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/) | [NOTE](20-request-forms/NOTE.md) | ⬜ |
| 21 | [Form Models](https://fastapi.tiangolo.com/tutorial/request-form-models/) | [NOTE](21-request-form-models/NOTE.md) | ⬜ |
| 22 | [Request Files](https://fastapi.tiangolo.com/tutorial/request-files/) | [NOTE](22-request-files/NOTE.md) | ⬜ |
| 23 | [Request Forms and Files](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/) | [NOTE](23-request-forms-and-files/NOTE.md) | ⬜ |
| 24 | [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) | [NOTE](24-handling-errors/NOTE.md) | ⬜ |
| 25 | [Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/) | [NOTE](25-path-operation-configuration/NOTE.md) | ⬜ |
| 26 | [JSON Compatible Encoder](https://fastapi.tiangolo.com/tutorial/encoder/) | [NOTE](26-encoder/NOTE.md) | ⬜ |
| 27 | [Body - Updates](https://fastapi.tiangolo.com/tutorial/body-updates/) | [NOTE](27-body-updates/NOTE.md) | ⬜ |
| 28 | [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) | [NOTE](28-dependencies/NOTE.md) | ⬜ |
| 29 | [Security](https://fastapi.tiangolo.com/tutorial/security/) | [NOTE](29-security/NOTE.md) | ⬜ |
| 30 | [Middleware](https://fastapi.tiangolo.com/tutorial/middleware/) | [NOTE](30-middleware/NOTE.md) | ⬜ |
| 31 | [CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) | [NOTE](31-cors/NOTE.md) | ⬜ |
| 32 | [SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) | [NOTE](32-sql-databases/NOTE.md) | ⬜ |
| 33 | [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/) | [NOTE](33-bigger-applications/NOTE.md) | ⬜ |
| 34 | [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) | [NOTE](34-background-tasks/NOTE.md) | ⬜ |
| 35 | [Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/) | [NOTE](35-metadata/NOTE.md) | ⬜ |
| 36 | [Static Files](https://fastapi.tiangolo.com/tutorial/static-files/) | [NOTE](36-static-files/NOTE.md) | ⬜ |
| 37 | [Testing](https://fastapi.tiangolo.com/tutorial/testing/) | [NOTE](37-testing/NOTE.md) | ⬜ |
| 38 | [Debugging](https://fastapi.tiangolo.com/tutorial/debugging/) | [NOTE](38-debugging/NOTE.md) | ⬜ |

