import datetime

from models import Todo
from models import session

all = session.query(Todo).all()
print(len(all))
for e in all:
    print(e)

todo1 = Todo(text=f"One {datetime.datetime.now()}", is_done=False)
todo2 = Todo(text=f"Two {datetime.datetime.now()}", is_done=False)

session.add_all([todo1, todo2])
session.commit()

all = session.query(Todo).all()
print(len(all))
for e in all:
    print(e)