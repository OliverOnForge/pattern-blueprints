import pytest
from domain_examples.sensor_factory import SensorFactory, TemperatureSensor, ThermalCamera

def test_sensor_creation_success():
    """Prueba que la fábrica crea los objetos correctos según el tipo."""
    temp_sensor = SensorFactory.create_sensor("TEMP", "SN-001")
    thermal_cam = SensorFactory.create_sensor("THERMAL", "CAM-99")
    
    assert isinstance(temp_sensor, TemperatureSensor)
    assert isinstance(thermal_cam, ThermalCamera)
    assert temp_sensor.sensor_id == "SN-001"

def test_sensor_data_output():
    """Prueba que los métodos de lectura devuelven el formato esperado."""
    sensor = SensorFactory.create_sensor("TEMP", "SN-001")
    lectura = sensor.read_data()
    
    assert "°C" in lectura  # Verifica que sea una lectura de temperatura válida

def test_invalid_sensor_type():
    """Prueba el manejo de errores ante tipos no registrados."""
    # Aquí demuestras tu habilidad en 'manejo de errores'
    with pytest.raises(ValueError) as excinfo:
        SensorFactory.create_sensor("PLC_UNKNOWN", "ID-000")
    
    assert "no soportado" in str(excinfo.value)

def test_case_insensitivity():
    """Prueba que la fábrica sea robusta a mayúsculas/minúsculas."""
    sensor = SensorFactory.create_sensor("temp", "SN-001")
    assert isinstance(sensor, TemperatureSensor)