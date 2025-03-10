class A:
    def method_a1(self):
        print("Method A1")

    def method_a2(self):
        print("Method A2")

    def override_method(self):
        print("Override method in A")
class B(A):
    def method_b1(self):
        print("Method B1")

    def method_b2(self):
        print("Method B2")

    def override_method(self):
        print("Override method in B")

# Subclass C of B
class C(B):
    def method_c1(self):
        print("Method C1")

    def method_c2(self):
        print("Method C2")

    def override_method(self):
        print("Override method in C")
class Main:
    def main(self):
        obj_a = A()
        obj_b = B()
        obj_c = C()
        print("Class A methods:")
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.override_method()

        print("\n")
        print("Class B methods:")
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.method_a1()
        obj_b.method_a2()
        obj_b.override_method()
        print("\n")
        print("Class C methods:")
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.method_b1()
        obj_c.method_b2()
        obj_c.method_a1()
        obj_c.method_a2()
        obj_c.override_method()
main_obj = Main()
main_obj.main()



