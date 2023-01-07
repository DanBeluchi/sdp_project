"""
This module provides information about the cpu temperature.
"""

from flask import Blueprint
from gpiozero import CPUTemperature

cpu_error = Blueprint("cpu_error", __name__, url_prefix="/cpu")


@cpu_error.route("/query")
def cpu_temp_error():
    '''
    This function tells the user if the cpu temperature is running too hot.
    '''

    cpu = CPUTemperature()

    temp = cpu.temperature

    if temp > 60:
        return "CPU temperature is too hot!"

    else:
        return "CPU temperature is fine!"
