"""
Unit tests for cpu temp.
"""

# yapf: disable
import sys  # nopep8

sys.path.insert(1, './sensor_api')  # nopep8
# yapf: enable

# pylint: disable=C0413
import pytest
# pylint: disable=E0401
import cpu  # type: ignore
# pylint: enable=E0401
# pylint: enable=C0413


@pytest.mark.unittest
def test_disk_usage_str_not_empty():
    """
    Test that return object is not empty.
    """
    value = cpu.cpu_temp()
    assert value != ""
