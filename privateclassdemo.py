class MyClass:
    def _init_(self, name, age):
        self.__name = name
        self.__age = age 

    def __private_method(self):
        return f"Private Method Called: Name = {self._name}, Age = {self._age}"

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")
        print(self.__private_method()) 
if __name__ == "__main__":
    obj = MyClass("Priya", 22)
    obj.display()