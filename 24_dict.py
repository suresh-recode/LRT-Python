a = {"Name": "Suresh",
     "Age": "25",
     }
a.update({'Phone': 123456789})
a['Gender'] = "Male"
# print(a['Gender'])
for val in a.items():
     print("{0} = {1}".format(val[0], val[1]))
# a.pop('Name')
# a.popitem()
# print(a)
# del a['Name']
# print(a)
# if 'Name' in a:
#      print("Yes")
# print(a['Age'])
# print(a.get('Age1'))
# print(a.keys())
# print(a.values())
# print(a.items())
# if 'Suresh1' in a.values():
#      print("Yes")
