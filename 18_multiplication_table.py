mul = int(input("Enter the multiplication table: "))
start = int(input("Enter the start point: "))
end = int(input("Enter the end point: "))

for i in range(start, end + 1):
    print("{} X {} = {}".format(mul, i, mul * i))   # 5 X 10 = 50