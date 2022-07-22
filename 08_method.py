def method_name(val, data):
    print("I'm called with {0} and {1}".format(val, data))
    val = val + 20
    return val

a = method_name(10, 'suresh')
print(a)