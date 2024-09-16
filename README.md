# Understanding Fast API - Library in Python
This project is to understand how to use FastAPI python library.

To understand deeply about Fast API is recommended to understand about Pydantic, in first place, because the whole Fast API is based about Pydantic([5]).

- https://docs.pydantic.dev/latest/

- https://github.com/HelloWounderworld/pydantic.git

## Using Fast API in Python using virtual environment in Python
First, we have to create a Python environment.

    https://fastapi.tiangolo.com/pt/virtual-environments/

If you prefer, with virtual environment, you can use uv to manage more easily versions os pythons that you want to use in a local directory

    https://docs.astral.sh/uv/

    https://github.com/astral-sh/uv

1. Checking python version:

        python --version or python3 --version

2. Checking if venv installed:

    Usually, Python 3.3 to above the venv comes together.

        python -m venv --help

3. Creating an virtual environment

    Choose the directory that you want to develop and digit the following command

        python -m venv environment_name

4. Activating the virtual environment:

    Window

        environment_name\Scripts\activate

    MacOs/Linux

        source environment_name/bin/activate

5. Now, you can install, using pip, fastapi package:

    The installation forms below is to ensure that other packages is installed with fastapi, for example, uvicorn

        pip install "fastapi[standard]" or pip install "fastapi[all]"

    If you want to install fastapi in classic form, just runs

        pip install fastapi
    
    but is recommended to install also uvicorn in following

        pip install "uvicorn[standard]"

    and the same form to other packages.

    If you have a requirements.txt, just copy it inside of virtual environment directory and run following command

        pip install -r requirements.txt

6. Freeze packages versions on the requirements.txt file:

    After installed packages that you need to your project is a good practice to freeze its in a requirements.txt files.

    To do it, you have, in first, digit

        pip freeze

    After this you have to create a requirements file and to make Ctrl+C and Ctrl+V about this file. Or, more fast

        pip freeze > requirements.txt

Now, you have an isolated virtual environment to start to develop your first fast api.

Just see references that I used to study about.

- [References](#references)

Tip: If you want to get out of the virtual environment just type

    deactivate

## Using Fast API by uv

## Using Fast API in docker container

## Text Editor:

- VS Code, one of most popular. (https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)

- I prefer to use Cursor, the most modern text Editor. Is like VSCode with ChatGPT. (https://www.cursor.com/s)

- PyCharm, like Intellji, who knows or already programed by Java. (https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

## References

1. [FastAPI Home Page][1]
2. [Fast API documentation to introduce to the concept step by step][2]
3. [Fast API Github to instal library and run in a server][3]
4. [Fast API CLI Documentation][4]
5. [Good practice using Pydantic with Fast API][5]
6. [Benchmark with Go language][6]
7. [If you want to use async/await without using the syntaxes async and await][7]
8. [Thread used before birth async and await. Unique form to handle asynchronous code][8]
9. [Callback hell at the ancient treatment about asynchronous code][9]
10. [How async and await works in background][10]
11. [More about environment to define new variable temporary][11]
12. [More about the environment variable][12]
13. [uv, management tool to handle everything in python][13]

[1]: https://fastapi.tiangolo.com/

[2]: https://fastapi.tiangolo.com/pt/virtual-environments/

[3]: https://github.com/fastapi/fastapi?tab=readme-ov-file#example-upgrade

[4]: https://fastapi.tiangolo.com/fastapi-cli/

[5]: https://docs.pydantic.dev/latest/

[6]: https://www.techempower.com/benchmarks/#section=data-r17&hw=ph&test=query&l=zijmkf-1

[7]: https://docs.python.org/3/library/asyncio-task.html#coroutine

[8]: https://www.gevent.org/

[9]: http://callbackhell.com/

[10]: https://fastapi.tiangolo.com/pt/async/#detalhes-muito-tecnicos

[11]: https://12factor.net/config

[12]: https://en.wikipedia.org/wiki/Environment_variable

[13]: https://docs.astral.sh/uv/
