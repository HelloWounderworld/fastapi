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

    If you have a requirements.txt, just copy it inside of virtual environment directory and run following command

        pip install -r requirements.txt

6. Freeze packages versions on the requirements.txt file:

    After installed packages that you need to your project is a good practice to freeze its in a requirements.txt files.

    To do it, you have, in first, digit

        pip freeze

    After this you have to create a requirements.file and to make Ctrl+C and Ctrl+V about this file.

Now, you have an isolated virtual environment to start to develop your first fast api.

Just see references that I use to study about.

Tip: If you want to get out of the virtual environment just type

    deactivate

## Using Fast API in docker container

## References

1. [FastAPI Home Page][1]
2. [Fast API documentation to introduce to the concept step by step][2]
3. [Fast API Github to instal library and run in a server][3]
4. [Fast API CLI Documentation][4]

[1]: https://fastapi.tiangolo.com/

[2]: https://fastapi.tiangolo.com/learn/

[3]: https://github.com/fastapi/fastapi

[4]: https://fastapi.tiangolo.com/fastapi-cli/
