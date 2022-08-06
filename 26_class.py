class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method_name(self):
        print("Hello {0}, his age is {1}".format(self.name,
                                                 self.age))


obj1 = ClassName('Jean', 10)
# print(obj1.x)
obj1.method_name()