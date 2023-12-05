from datetime import datetime

from addict import Dict
from sqlalchemy.orm import close_all_sessions

from db.config import session
from db.models import Requirement, RunResult
from helpers import read_requirements
from logger import LOGGER


def close_session(func):
    def wrapper(*args, **kwargs):
        try:
            if not session.is_active:
                session.begin()
            response = func(*args, **kwargs)
            close_all_sessions()
            return response
        except Exception as err:
            LOGGER.error(f"SQL error: {err}")
            session.rollback()
            close_all_sessions()

    return wrapper


@close_session
def add_run_result(requirement_code, result):
    if requirement_code:
        try:
            requirement = get_requirement(requirement_code)
            session.merge(RunResult(code=requirement.code, result=result))
            session.commit()
        except Exception as e:
            LOGGER.error(f'Error during assertion processing: \n{e}')


@close_session
def get_requirement(requirement_code):
    return session.query(Requirement).where(Requirement.code == requirement_code).order_by(
        Requirement.date.desc()).first()


@close_session
def import_requirements(path):
    requirements = read_requirements(path)
    for requirement in requirements:
        session.merge(Requirement(**requirement, status='active', date=datetime.utcnow()))
    session.commit()


def get_components():
    return [component.component for component in session.query(Requirement.component).distinct().all()]


def get_requirements_stat_by_component(component):
    requirements_results = session.query(Requirement, RunResult).where(Requirement.component == component).outerjoin(
        RunResult, RunResult.code == Requirement.code).all()
    passed_requirements = len([result for result in requirements_results if result[1] and result[1].result == 'PASS'])
    failed_requirements = len([result for result in requirements_results if result[1] and result[1].result == 'FAIL'])
    return Dict(na_requirements=len(requirements_results) - passed_requirements - failed_requirements,
                passed_requirements=passed_requirements,
                failed_requirements=failed_requirements)


def get_components_stat():
    return {component: get_requirements_stat_by_component(component) for component in get_components()}


if __name__ == '__main__':
    a = get_components_stat()
