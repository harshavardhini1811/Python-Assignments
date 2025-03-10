
class PublicClass:
    def _init_(self, name, age):
        self.name = name 
        self.age = age 

    def public_method(self):
        return f"Public Method Called: Name = {self.name}, Age = {self.age}"
class SamePackage:
    def access_public(self):
        obj = PublicClass("Priya", 22)
        print("Same Package Access:", obj.public_method())
class DifferentPackage:
    def access_public(self):
        obj = PublicClass("Ravi", 25)
        print("Different Package Access:", obj.public_method())
class UnrelatedClass:
    def access_public(self):
        obj = PublicClass("Kiran", 30)
        print("Unrelated Class Access:", obj.public_method())
if __name__ == "_main_":
    print("---- Access from Same Package ----")
    SamePackage().access_public()

    print("\n---- Access from Different Package ----")
    DifferentPackage().access_public()

    print("\n---- Access from Unrelated Class ----")
    UnrelatedClass().access_public()


