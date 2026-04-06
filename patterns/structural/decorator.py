# patterns/structural/decorator.py
from functools import wraps
import time

def base_logger_decorator(func):
    """
    Decorador base que registra la ejecución de una función.
    Demuestra el uso de cierres (closures) y funciones de orden superior.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finalizado: {func.__name__}")
        return result
    return wrapper