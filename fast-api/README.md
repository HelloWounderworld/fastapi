# To run Fast API project in a server:
Go to the directory where main.py founded it and run

    fastapi dev main.py

Or running in development mode, for production use

    fastapi run

You can access following ports:

- Serving at: http://127.0.0.1:8000

- API docs: http://127.0.0.1:8000/docs (or http://127.0.0.1:8000/redoc)

The advantage to access "http://127.0.0.1:8000/docs" it will be unnecessary to install Postman to test each request type to check if your program is working.

Tip: To get out of the api serve mode just type Ctrl+C

## Other form to run your project in virtual environment:
Go to the your directory that you want to run and just type

    uvicorn main:app --reload

where "main" is the name os file "main.py" and "app" is the name of variable "app" defined at the code. Finally, the "reload" as the name wants to say is to reload as the code is changed.

If you instance the class FastAPI like following

    my_awesome_api = FastAPI()

so when you activate the uvicorn it will be

    uvicorn main:my_awsome_api --reload

The local url for this case is the same above.

Tip: Shows the schema of the OpenAPI, the FastAPI shows whole details of each api's defined in main.py.

    http://127.0.0.1:8000/openapi.json

## References:

1. [Swagger UI][1]
2. [Redoc UI][2]
3. [Open API Specification - FastAPI uses the schema using OpenAPI default][3]
4. [Data Model - Schema in OpenAPI][4]
5. [Database Schema][5]
6. [The class FastAPI is inherited by Starlette][4]
7. [Endpoint vs Routes][7]
8. [Route is equivalent to an endpoint in FastAPI][8]
9. [Decorators][9]
10. [Regular Expressions][10]
11. [Ellipsis "...", Python's special characters][11]
12. [Kwargs][12]
13. [Param class. Query and Path are subclass of the Praram class][13]

[1]: https://github.com/swagger-api/swagger-ui

[2]: https://github.com/Redocly/redoc

[3]: https://github.com/OAI/OpenAPI-Specification

[4]: https://swagger.io/docs/specification/data-models/

[5]: https://en.wikipedia.org/wiki/Database_schema

[6]: https://www.starlette.io/

[7]: https://danaepp.com/endpoints-vs-routes

[8]: https://fastapi.tiangolo.com/pt/tutorial/first-steps/#rota

[9]: https://www.geeksforgeeks.org/decorators-in-python/

[10]: https://www.w3schools.com/python/python_regex.asp

[11]: https://docs.python.org/3/library/constants.html#Ellipsis

[12]: https://github.com/HelloWounderworld/Review-Python/blob/main/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/README.md#aula-32---empacotamento-e-desempacotamento-de-dicion%C3%A1rios--args-e-kwargs

[13]: https://param.holoviz.org/user_guide/How_Param_Works.html
