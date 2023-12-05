from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from env import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?"
engine = create_engine(SQLALCHEMY_DATABASE_URI + f"auth_plugin=mysql_native_password", pool_recycle=3600)
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
