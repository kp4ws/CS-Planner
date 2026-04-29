from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

'''
Engine manages the connection to the database and handles query execution.
'''
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# TODO: Needs updating

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()