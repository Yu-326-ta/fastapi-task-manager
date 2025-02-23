from sqlalchemy import create_engine
from api.models.task import Base
import os

DB_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@mysql:3306/{os.getenv('MYSQL_DATABASE')}?charset=utf8"

engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
