# patterns/behavioral/observer.py

from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    """Interfaz para los observadores que deben ser notificados."""
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    """Clase base que gestiona la suscripción y notificación."""
    def __init__(self):
        self._observers: List[Observer] = [] # Lista de suscriptores

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)