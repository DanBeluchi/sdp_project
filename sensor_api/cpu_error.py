from flask import Blueprint
from gpiozero import CPUTemperature

cpu_error = Blueprint("cpu_error", __name__, url_prefix="/cpu")


@cpu_error.route("/query")
def cpu_temp_error():
    '''
    This function provides the CPU temperature of the raspberry pi.
    Returns temperature in celsius. Return type of float.
    '''

    cpu = CPUTemperature()

    temp = cpu.temperature

    if(temp > 60):
        return "CPU temperature is too hot!"

    else:
        return "CPU temperature is fine!"

