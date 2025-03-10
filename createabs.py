from abc import ABC, abstractmethod

class A(ABC):
    def _init_(self, name): self.name = name  
    @abstractmethod
    def abs_method(self): pass
    def non_abs_method(self): print(f"Non-abstract: {self.name}")

class B(A):
    def _init(self, name, age): super().init_(name); self.age = age  
    def abs_method(self): print(f"Abstract: {self.name}, {self.age}")

obj = ("Priya", 22)
obj.abs_method()
obj.non_abs_method()


