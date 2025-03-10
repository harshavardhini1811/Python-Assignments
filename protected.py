class ParentClass:
    def _init_(self, name, age):
        self._name = name
        self._age = age 

    def _protected_method(self):
        return f"Protected Method Called: Name = {self._name}, Age = {self._age}"
class SamePackage:
    def access_protected(self):
        obj = ParentClass("Priya", 22)
        print("Same Package Access:", obj._protected_method())
class ChildClass(ParentClass):
    def show_protected(self):
        print("Child Class Access:", self._protected_method())
class UnrelatedClass:
    def try_access(self):
        obj = ParentClass("Kiran", 30)
        print("Unrelated Class Access:", obj._protected_method())
if __name__ == "_main_":
    print("---- Access from Same Package ----")
    SamePackage().access_protected()
    print("\n---- Access from Child Class ----")
    ChildClass("Ravi", 25).show_protected()

    print("\n---- Access from Unrelated Class ----")
    UnrelatedClass().try_access() 
