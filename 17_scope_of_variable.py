x = 20


def method_name():
    global x
    x = 10
    print(x)


method_name()
print(x)