class A:
    def show(self):
        print("Method in A (Superclass)")

class B(A):
    def show(self):
        print("Method in B (Subclass of A)")

class C(B):
    def show(self):
        print("Method in C (Subclass of B)")
obj_b = B()
ref_a1 = obj_b
ref_a1.show()
obj_c = C()
ref_a2 = obj_c 
ref_a2.show() 