from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.orm import declarative_base, relationship

from db.config import engine

base = declarative_base(cls=DeferredReflection)


class Requirement(base):
    __tablename__ = "requirements"

    code = Column(String(255), primary_key=True)
    value = Column(String(1020))
    status = Column(String(255))
    component = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)

    run_results = relationship('RunResult', backref='requirements', cascade='save-update, merge, delete')


class RunResult(base):
    __tablename__ = "run_results"

    code = Column(String(255), ForeignKey('requirements.code'), primary_key=True)
    result = Column(String(255))


base.metadata.create_all(engine)
base.prepare(engine)
