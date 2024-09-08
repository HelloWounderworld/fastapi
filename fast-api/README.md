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