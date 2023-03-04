# db
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine_url = URL.create(
    drivername='mysql+pymysql',
    username='test',
    password='test',
    host='mysql',
    database='test',
    port=3306,
)
engine = create_engine(engine_url)
Session = sessionmaker(bind=engine)
session = Session()

# models
Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)
