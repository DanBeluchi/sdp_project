import shutil

def disk_usage():
    """
    This function provides disk usage information of the root partition.
    Returns usage in bytes.
    """
    
    disk_object = shutil.disk_usage("/")
    
    return disk_object.used
    