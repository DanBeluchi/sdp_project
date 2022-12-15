import sys

sys.path.insert(1, './sensor_api')

import disk

def test_disk_usage_type_str():
    """
    Test if the return type is string.
    """
    value = disk.disk_usage()
    assert isinstance(value, str)

def test_disk_usage_not_empty():
    """
    Test that return object is not empty.
    """
    value = disk.disk_usage()
    assert value != ""
