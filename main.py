from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:123@localhost/Training_DB", echo=True)
engine.connect()
print(engine)

