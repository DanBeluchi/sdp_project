"""
Test fixture of the flask app.
"""

# yapf: disable
import sys  # nopep8

sys.path.insert(1, './sensor_api')  # nopep8
# yapf: enable

# pylint: disable=C0413
import pytest
# pylint: disable=E0401
import disk  # type: ignore
# pylint: enable=E0401
# pylint: enable=C0413

# to be done!
