# domain_examples/performance_monitor.py
import time
from functools import wraps
from patterns.structural.decorator import base_logger_decorator

def monitor_industrial_process(func):
    """
    Decorador avanzado para telemetría de procesos.
    Mide tiempo de ejecución y captura errores de sensores.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            # Ejecución del proceso (ej. lectura de PLC o renderizado)
            result = func(*args, **kwargs)
            status = "SUCCESS"
        except Exception as e:
            status = f"FAILED: {str(e)}"
            result = None
        
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        print(f"--- Telemetría: {func.__name__} ---")
        print(f"Estado: {status}")
        print(f"Tiempo: {duration:.4f} segundos")
        print("-------------------------------")
        return result
    return wrapper

# Ejemplo de uso en un entorno de ingeniería
@monitor_industrial_process
def simulate_plc_logic(cycles: int):
    """Simula el procesamiento de lógica en un PLC Siemens/Allen-Bradley."""
    time.sleep(0.5) # Simulación de carga de trabajo
    if cycles < 0:
        raise ValueError("Los ciclos no pueden ser negativos")
    return f"Procesados {cycles} ciclos de control"

if __name__ == "__main__":
    simulate_plc_logic(100)
    simulate_plc_logic(-1) # Prueba de manejo de errores