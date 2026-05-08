from abc import ABC, abstractmethod

class HashAlgorithm(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def hash(self, text: str) -> str:
        pass