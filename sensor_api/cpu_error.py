"""
This module provides information about the cpu temperature!
"""

from flask import Blueprint
import psutil

cpu_error = Blueprint("cpu_error", __name__, url_prefix="/cpu/temp")


def cpu_temp_error_msg(temp):
    '''
    Return cpu temp error message.
    '''

    if temp > 60:
        return "CPU temperature is too hot!"

    else:
        return "CPU temperature is fine!"


@cpu_error.route("/error")
def cpu_temp_error():
    '''
    This function tells the user if the cpu temperature is running too hot.
    '''

    temp = psutil.sensors_temperatures()['cpu_thermal'][0]

    return cpu_temp_error_msg(temp.current)
