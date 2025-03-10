class A:
    def _init_(self):
        self.value = "Value in A"
class B(A):
    def _init_(self):
        super()._init_()
        self.value = "Value in B" 

class C(B):
    def _init_(self):
        super()._init_()
        self.value = "Value in C" 
obj_b = B()
ref_a1 = obj_b
print(ref_a1.value) 
obj_c = C()
ref_a2 = obj_c 
print(ref_a2.value)
