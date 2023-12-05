from hamcrest import assert_that, equal_to

from db.db_functions import add_run_result
from env import REQUIREMENTS_PATH


def check_that(actual_or_assertion, matcher=None, reason="", requirement_code=None):
    try:
        assert_that(actual_or_assertion, matcher=matcher, reason=reason)
    except AssertionError as e:
        add_run_result(requirement_code, 'FAIL')
        raise e
    add_run_result(requirement_code, 'PASS')


def import_requirements(path=REQUIREMENTS_PATH):
    import_requirements(path)


if __name__ == '__main__':
    check_that('a', equal_to('b'), requirement_code='r2')
