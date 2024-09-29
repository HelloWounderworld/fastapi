# Error message with "uvicorn main:app --reload":
Process SpawnProcess-13:
Traceback (most recent call last):
  File "C:\Users\leona\AppData\Local\Programs\Python\Python312\Lib\multiprocessing\process.py", line 314, in _bootstrap
    self.run()
  File "C:\Users\leona\AppData\Local\Programs\Python\Python312\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\uvicorn\_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\uvicorn\server.py", line 65, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leona\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\leona\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leona\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 687, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\uvicorn\server.py", line 69, in serve
    await self._serve(sockets)
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\uvicorn\server.py", line 76, in _serve
    config.load()
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\uvicorn\config.py", line 434, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leona\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\basic-example-using-pydantic\main.py", line 14, in <module>
    @app.get("/items/")
     ^^^^^^^^^^^^^^^^^^
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\fastapi\routing.py", line 992, in decorator
    self.add_api_route(
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\fastapi\routing.py", line 931, in add_api_route
    route = route_class(
            ^^^^^^^^^^^^
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\fastapi\routing.py", line 552, in __init__
    self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\fastapi\dependencies\utils.py", line 268, in get_dependant
    param_details = analyze_param(
                    ^^^^^^^^^^^^^^
  File "C:\Users\leona\Documents\study-programming\fastapi\fast-api\.venv\Lib\site-packages\fastapi\dependencies\utils.py", line 482, in analyze_param
    assert is_scalar_field(field) or is_scalar_sequence_field(field)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError

Just run the following

    pip install fastapi[all] --upgrade

# Spoiler alert:
Spoiler alert: you can also use Pydantic models to declare cookies and headers, but you will read about that later in the tutorial. 

# References:

1. [Annotated class at the typing][1]
2. [Literal class at the typing][2]
3. [Fields at the Pydantic][3]
4. [Forbid any extra fields at the query parameter][4]

[1]: https://docs.python.org/3/library/typing.html#typing.Annotated
[2]: https://docs.python.org/3/library/typing.html#typing.Literal
[3]: https://docs.pydantic.dev/latest/concepts/fields/
[4]: https://stackoverflow.com/questions/71837398/pydantic-validations-for-extra-fields-that-not-defined-in-schema
