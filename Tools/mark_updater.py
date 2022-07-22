markDict = {}
markList = []

while True:
    newValue = True
    name = input("Enter the name: ")
    if name == "exit":
        break
    markDict['name'] = name
    markDict['mark'] = 10
    if len(markList) == 0:
        markList.append(markDict)
        markDict = {}
    else:
        for a in markList:
            if a['name'] == name:
                a['mark'] = a['mark'] + 10
                newValue = False
        if newValue:
            markList.append(markDict)
            markDict = {}

print(markList)