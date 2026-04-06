
import pytest
from domain_examples.config_manager import ConfigurationManager

def test_singleton_identity():
    """Verifica que dos instancias creadas por separado sean el mismo objeto en memoria."""
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    
    # Comprobación de identidad (ID de memoria)
    assert config1 is config2
    assert id(config1) == id(config2)

def test_singleton_shared_state():
    """Verifica que los datos modificados en una instancia se reflejen en la otra."""
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    
    # Simulamos carga de datos en la instancia 1
    config1.settings = {"threshold_temp": 75.0, "unit": "Celsius"}
    
    # La instancia 2 debe tener los mismos datos automáticamente
    assert config2.get_setting("threshold_temp") == 75.0
    assert config2.get_setting("unit") == "Celsius"

def test_singleton_attribute_persistence():
    """Verifica que añadir un atributo nuevo persista en todas las referencias."""
    instance_a = ConfigurationManager()
    instance_a.custom_flag = True
    
    instance_b = ConfigurationManager()
    assert hasattr(instance_b, "custom_flag")
    assert instance_b.custom_flag is True