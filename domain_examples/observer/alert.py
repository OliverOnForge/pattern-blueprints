
from patterns.behavioral.observer import Subject, Observer

# --- Observadores Concretos ---

class ControlPanel(Observer):
    """Simula una interfaz gráfica (UI/UX) que muestra alertas."""
    def update(self, message: str):
        print(f"[UI Panel] ALERTA VISUAL: {message}")

class DataLogger(Observer):
    """Simula el guardado de eventos en un log o base de datos SQLite."""
    def update(self, message: str):
        print(f"[SQLite Log] Guardando evento en historial: {message}")

# --- Sujeto Concreto ---

class PressureSensor(Subject):
    """Sensor que monitorea presión en una línea neumática/hidráulica."""
    def check_pressure(self, value: float):
        print(f"--- Monitoreo: {value} PSI ---")
        if value > 90.0:
            self.notify(f"¡Presión Crítica detectada!: {value} PSI")

# --- Ejecución ---

if __name__ == "__main__":
    # Configuración del sistema de control
    sensor_presion = PressureSensor()
    panel = ControlPanel()
    logger = DataLogger()

    # Suscribimos los módulos
    sensor_presion.attach(panel)
    sensor_presion.attach(logger)

    # Simulación de lecturas
    sensor_presion.check_pressure(45.0)  # Todo normal
    sensor_presion.check_pressure(95.5)  # Dispara notificaciones