a = "Vijay Ganesan".lower().replace(" ", '')
# print(a)
res = {}
for val in a:
    # print(val)
    if val in res:
        res[val] = res[val] + 1
    else:
        res[val] = 1
print(res)
# from collections import Counter
# print(Counter(a))


