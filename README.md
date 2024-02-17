## fastapi

- [Preparing a virtual environment](#preparing-a-virtual-environment)
  - [Using pip](#using-pip)
- [Running an application](#running-an-application)
- [Swagger](#swagger)
- [Path parameters](#path-parameters)
- [Endpoint priority](#endpoint-priority)
- [Query parameters](#query-parameters)

# Preparing a virtual environment

```bash
# Create virtual environment

python3 -m venv .venv

# Activate virtual environment

. .venv/bin/activate

# Install packages

pip install fastapi
pip install uvicorn
```

## Using pip

`pip` is the package installer for Python. https://pypi.org/project/pip/

> ```bash
> # Installing packages
>
> pip install <package>
>
>
> # Uninstall packages
>
> pip uninstall <package>
>
> # Listing packages
>
> pip list 
>
> # Listing outdated packages
>
> pip list --outdated
> ```

# Running an application

```bash

mkdir books
cat > books/books.py <<EOF
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return "hello world"
EOF

# 1. Running app in PARENT_DIRECTORY & reloading if files change

uvicorn books.books:app --reload 
# SYNTAX
# books.books:app = (directory).(python_file):(name_of_app_instance)

# 2. Running app in CURRENT_DIRECTORY & reloading if files change

cd books
uvicorn books:app --reload
```

# Swagger 

FastAPI ships with swagger by default. http://localhost:8000/docs

https://swagger.io/solutions/api-design/

- Use verbose snake case names for api endpoint functions. Swagger will use the name as an endpoint 
- Function comments will be used as a description.

```py
@app.get("/books")
async def read_all_books():
    return BOOKS
```

![](/books/docs/img/swagger.png)



# Path parameters

You can declare path "parameters" with the same syntax used by Python format strings:

```py
@app.get("/books/{book}")
async def read_book(book: str):
    return {'book', book}
```



# Endpoint priority

Endpoint order matters, they are read from top to botoom. For example, the last endpoint below won't match because it overlaps with the endpoint above it. To fix this flip the order. Rule of thumb, add dynamic parameter endpoints last.
```py
@app.get("/books/{book}")
async def read_book(book:str):
    return {'book', book}

@app.get("/books/mybook")
async def read_book():
    return {'book', "my book"}
```

# Query parameters

Unlink path parameters, query parameters are not defined in the path but included in the function parameters. 
```python
@app.get("/books/{book}/")
async def read_book(book:str, query: str):
    return {'book', book, 'query': query}
```
