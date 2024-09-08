# Understanding Fast API - Library in Python
This project is to understand how to use FastAPI python library.

## Using Fast API in Python using virtual environment in Python
First, we have to create a Python environment.

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

        pip install "fastapi[standard]"

Now, you have an isolated virtual environment to start to develop your first fast api.

Just see references that I use to study about.

Tip: If you want to get out of the virtual environment just type

    deactivate

## Using Fast API in docker container

## References

[1]: https://fastapi.tiangolo.com/

[2]: https://fastapi.tiangolo.com/learn/

[3]: https://github.com/fastapi/fastapi

[4]: https://fastapi.tiangolo.com/fastapi-cli/
