import uvicorn
from fastapi import FastAPI
from sqlalchemy import URL

app = FastAPI()

engine_url = URL.create(
    drivername='mysql+pymysql',
    username='test',
    password='test',
    host='mysql',
    database='test',
    port=3306,
)


@app.on_event("startup")
async def startup_event():
    print('Starting up')


@app.get('/')
def home():
    return {'message': 'UP'}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5001, reload=True)
