class C():
    def _init(self, name, city): super().init_(name); self.city = city
    def abs_method(self): print(f"Abstract: {self.name}, {self.city}")

obj2 = C("Harsha", "Hyderabad")
obj2.non_abs_method()