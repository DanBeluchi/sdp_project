from flask import Blueprint
from gpiozero import CPUTemperature

cpu = Blueprint("cpu", __name__, url_prefix="/cpu")


@cpu.route("/temp")
def cpu_temp():
    '''
    This function provides the CPU temperature of the raspberry pi.
    Returns temperature in celsius. Return type of float.
    '''

    cpu = CPUTemperature()


    return str(cpu.temperature)
