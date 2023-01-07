"""
Unit tests for disk usage.
"""

# yapf: disable
import sys  # nopep8

sys.path.insert(1, './sensor_api')  # nopep8
# yapf: enable

# pylint: disable=C0413
# pylint: disable=E0401
import disk  # type: ignore
# pylint: enable=E0401
# pylint: enable=C0413


def test_disk_usage_not_null():
    """
    Test that return object is not null.
    """
    value = disk.disk_usage_in_percent()
    assert value != 0


def test_disk_usage_str_not_empty():
    """
    Test that return object is not empty.
    """
    value = disk.disk_usage_str()
    assert value != ""
