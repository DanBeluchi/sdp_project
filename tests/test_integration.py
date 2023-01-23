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


@pytest.fixture()
def app():
    '''
    Create app fixture.
    '''

    app_fixture = flask_app.create_app()
    app_fixture.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app_fixture

    # clean up / reset resources here


@pytest.fixture()
def client(app_fixture):
    '''
    Return test client.
    '''
    return app_fixture.test_client()


@pytest.fixture()
def runner(app_fixture):
    '''
    Return test cli runner.
    '''
    return app_fixture.test_cli_runner()


@pytest.mark.integrationtest
def test_get_disk_usage_not_empty():
    """
    Test that return object is not null.
    """
    response = client.get("/disk/usage")
    assert response != ""


@pytest.mark.integrationtest
def test_get_cpu_temp_not_empty():
    """
    Test that return object is not null.
    """
    response = client.get("/cpu/temp")
    assert response != ""


@pytest.mark.integrationtest
def test_get_cpu_temp_error_not_empty():
    """
    Test that return object is not null.
    """
    response = client.get("/cpu/temp/error")
    assert response != ""
