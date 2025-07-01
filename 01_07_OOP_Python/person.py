from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name
    @abstractmethod
    def display_info(self):
        pass
    def __del__(self):
        name = getattr(self, "_name", None)
        if name:
            print(f"Has removed object: {name}")
        else:
            print("End program")
