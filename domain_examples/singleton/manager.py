
import json
from patterns.creational.singleton import SingletonMeta

class ConfigurationManager(metaclass=SingletonMeta):
    """
    Carga y gestiona la configuración del sistema desde un JSON.
    Al ser Singleton, garantizamos que no se lea el archivo múltiples veces.
    """
    def __init__(self):
        self.settings = {}
        self._is_loaded = False

    def load_config(self, file_path: str):
        # Manejo de errores para robustez industrial
        try:
            with open(file_path, 'r') as f:
                self.settings = json.load(f)
                self._is_loaded = True
                print(f"--- Configuración cargada desde {file_path} ---")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {file_path}")

    def get_setting(self, key: str):
        return self.settings.get(key, "Default_Value")

# Ejemplo de uso en tu sistema de instrumentación
if __name__ == "__main__":
    # Primera vez que accedemos
    config1 = ConfigurationManager()
    config1.load_config("config_sensores.json") # Supongamos que existe

    # Segunda vez en otra parte del código (ej. un módulo de control de PLC)
    config2 = ConfigurationManager()

    # Comprobación de que son la MISMA instancia
    print(f"¿Son la misma instancia?: {config1 is config2}") 
    print(f"Umbral de alerta: {config2.get_setting('threshold_temp')}")