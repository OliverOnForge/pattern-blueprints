
import pytest
from domain_examples.alert_system import PressureSensor, ControlPanel, DataLogger

class MockObserver:
    """Un observador de prueba para capturar las notificaciones."""
    def __init__(self):
        self.received_messages = []

    def update(self, message: str):
        self.received_messages.append(message)

def test_observer_subscription_logic():
    """Verifica que los observadores se añadan y eliminen correctamente."""
    sensor = PressureSensor()
    mock = MockObserver()
    
    sensor.attach(mock)
    assert mock in sensor._observers
    
    sensor.detach(mock)
    assert mock not in sensor._observers

def test_notification_flow():
    """Verifica que el mensaje llegue a múltiples observadores simultáneamente."""
    sensor = PressureSensor()
    ui_mock = MockObserver()
    db_mock = MockObserver()
    
    sensor.attach(ui_mock)
    sensor.attach(db_mock)
    
    # Forzamos una notificación de alerta
    sensor.notify("Test Alert")
    
    assert "Test Alert" in ui_mock.received_messages
    assert "Test Alert" in db_mock.received_messages

def test_industrial_pressure_logic():
    """Prueba que la alerta solo se dispare cuando la presión supera el umbral (90 PSI)."""
    sensor = PressureSensor()
    mock = MockObserver()
    sensor.attach(mock)
    
    # Caso 1: Presión normal (No debería haber mensajes)
    sensor.check_pressure(50.0)
    assert len(mock.received_messages) == 0
    
    # Caso 2: Presión crítica (Debería disparar alerta)
    sensor.check_pressure(95.0)
    assert len(mock.received_messages) == 1
    assert "Crítica" in mock.received_messages[0]