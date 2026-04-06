
import pytest
from domain_examples.performance_monitor import monitor_industrial_process, simulate_plc_logic

def test_metadata_preservation():
    """Verifica que el decorador use functools.wraps para mantener el nombre original."""
    # Esto demuestra conocimiento de introspección en Python
    assert simulate_plc_logic.__name__ == "simulate_plc_logic"
    assert "PLC Siemens/Allen-Bradley" in simulate_plc_logic.__doc__

def test_decorator_success_return():
    """Verifica que la función decorada retorne el valor correcto en un caso exitoso."""
    resultado = simulate_plc_logic(10)
    assert "10 ciclos" in resultado

def test_decorator_error_handling():
    """
    Verifica que el decorador capture excepciones y retorne None en lugar de crashear.
    Esto es vital para la 'automatización y manejo de errores'.
    """
    # Al pasar -1, simulate_plc_logic lanza un ValueError
    resultado = simulate_plc_logic(-1)
    
    # El decorador debe capturar el error y devolver None según la implementación previa
    assert resultado is None

def test_custom_function_decoration():
    """Prueba que el decorador se pueda aplicar a funciones genéricas de cálculo técnico."""
    @monitor_industrial_process
    def calculate_vibration_average(data: list):
        return sum(data) / len(data)
    
    data = [0.5, 0.7, 0.6, 0.9]
    assert calculate_vibration_average(data) == 0.675