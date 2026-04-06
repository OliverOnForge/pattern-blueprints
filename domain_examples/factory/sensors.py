# domain_examples/sensor_factory.py
from patterns.creational.factory import BaseProduct
from typing import Dict

# Implementas tus sensores usando tu conocimiento en instrumentación
class TemperatureSensor(BaseProduct):
    def operation(self):
        return "Lectura de RTD: 25°C"

class SensorFactory:
    # Usas diccionarios para evitar ifs largos, demostrando nivel intermedio
    _registry = {"TEMP": TemperatureSensor}
    
    @staticmethod
    def get_sensor(type_code: str):
        return SensorFactory._registry[type_code]()