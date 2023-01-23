"""
Integrations tests for the flask application.
"""

# yapf: disable
import sys  # nopep8

sys.path.insert(1, './sensor_api')  # nopep8
# yapf: enable

# pylint: disable=C0413
import pytest
# pylint: disable=E0401
import flask_app  # type: ignore
# pylint: enable=E0401
# pylint: enable=C0413


@pytest.fixture(scope='module')
def test_client():
    '''
    Create test client.
    '''
    _flask_app = flask_app.create_app()
    _flask_app.config.update({
        "TESTING": True,
    })

    testing_client = _flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = _flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


# pylint: disable=W0621
@pytest.mark.integrationtest
def test_get_disk_usage_check_redirect(test_client):
    """
    Test that there was one redirect response.
    """
    response = test_client.get("/disk/usage")
    assert response.status_code == 200


@pytest.mark.integrationtest
def test_get_cpu_temp_check_redirect(test_client):
    """
    Test that there was one redirect response.
    """
    response = test_client.get("/cpu/temp", follow_redirects=True)
    assert response.status_code == 200


@pytest.mark.integrationtest
def test_get_cpu_temp_error_check_redirect(test_client):
    """
    Test that there was one redirect response.
    """
    response = test_client.get("/cpu/temp/error", follow_redirects=True)
    assert response.status_code == 200

# pylint: enable=W0621
