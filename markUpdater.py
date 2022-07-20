markDict = {}
markList = []

while True:
    newValue = True
    name = input("Enter the name: ")    # arivunila
    if name == "exit":  # arivunila == exit
        break
    mark = int(input("Enter the mark: "))  # 10
    markDict['name'] = name
    markDict['mark'] = mark
    if len(markList) == 0:
        markList.append(markDict)
        markDict = {}
    else:
        for a in markList:
            if a['name'] == name:
                a['mark'] = a['mark'] + mark
                newValue = False
        if newValue:
            markList.append(markDict)
            markDict = {}

print(markList)
