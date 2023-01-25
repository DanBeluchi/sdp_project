"""
This module provides cpu temperature information.
"""

from flask import Blueprint
import psutil

cpu = Blueprint("cpu", __name__, url_prefix="/cpu")


@cpu.route("/temp")
def cpu_temp():
    '''
    This function provides the CPU temperature of the raspberry pi.
    Returns temperature in celsius.
    '''

    temp = psutil.sensors_temperatures()["cpu_thermal"][0]

    return str(temp.current)
