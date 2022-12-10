from flask import Blueprint
import shutil

disk = Blueprint("disk", __name__, url_prefix="/disk")

@disk.route("/usage")
def disk_usage():
    """
    This function provides disk usage information of the root partition.
    Returns usage in bytes. Return type of string.
    """
    
    disk_object = shutil.disk_usage("/")
    
    return str(disk_object.used)
    