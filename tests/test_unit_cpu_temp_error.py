"""
Unit tests for disk usage.
"""

# yapf: disable
import sys  # nopep8

sys.path.insert(1, './sensor_api')  # nopep8
# yapf: enable

# pylint: disable=C0413
import pytest
# pylint: disable=E0401
import cpu_error  # type: ignore
# pylint: enable=E0401
# pylint: enable=C0413


@pytest.mark.unittest
def test_cpu_temp_error_msg_to_hot():
    """
    Test that return object is not null.
    """
    msg = cpu_error.cpu_temp_error_msg(61)
    assert msg == "CPU temperature is too hot!"


@pytest.mark.unittest
def test_cpu_temp_error_msg_is_fine():
    """
    Test that return object is not null.
    """
    msg = cpu_error.cpu_temp_error_msg(60)
    assert msg == "CPU temperature is fine!"


@pytest.mark.unittest
def test_cpu_temp_error():
    """
    Test that return object is not empty.
    """
    msg = cpu_error.cpu_temp_error()
    assert msg != ""
