# Learning FastAPI using blog https://mattermost.com/blog/building-a-crud-fastapi-app-with-sqlalchemy/

## Reference

    https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure
    https://www.uvicorn.org/
    https://amitness.com/2020/06/fastapi-vs-flask/

## venv

    setup-venv.bat
    pip list
    python -V  // 3.11.1

## Start service

    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    or 
    python main.py

## Test

    http://localhost:8000

## Swagger

    http://localhost:8000/docs

