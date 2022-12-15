from flask import Blueprint
from gpiozero import DiskUsage

disk = Blueprint("disk", __name__, url_prefix="/disk")

@disk.route("/usage")
def disk_usage():
    """
    This function provides disk usage information of the root partition.
    Returns usage in percent
    """
    
    disk = DiskUsage()
    
    return 'Current disk usage: {}%'.format(disk.usage)
