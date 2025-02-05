
from abc import ABC, abstractmethod
class Expression(ABC):
    @abstractmethod
    def calc(self):
        pass