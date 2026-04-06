# patterns/creational/factory.py
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def operation(self):
        pass

class BaseFactory(ABC):
    @abstractmethod
    def create_product(self, item_type):
        pass