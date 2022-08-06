class A:

    def method_name(self):
        print("Called from A class")

class C:
    def method_name1(self):
        print("Called from C class")

class B(A, C):
    def hello(self):
        print("Hello")

obj = B()
obj.method_name1()

