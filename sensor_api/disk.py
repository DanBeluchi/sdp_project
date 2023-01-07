"""
Shutil lib used to get disk information.
"""
import shutil
from flask import Blueprint

disk = Blueprint("disk", __name__, url_prefix="/disk")


def disk_usage_in_percent():
    """
    This function provides disk usage information of the root partition.
    Returns usage in percent.
    """
    disk_object = shutil.disk_usage("/")

    return (100 / disk_object.free) * disk_object.used


@disk.route("/usage")
def disk_usage_str():
    """
    This function provides disk usage information of the root partition.
    Returns usage in percent of type string.
    """

    return f"{disk_usage_in_percent():0.2f}%"
