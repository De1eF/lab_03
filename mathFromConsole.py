import sys

def checkArgs(argArr):
    if len(argArr) != 4:
        print("Мусить включати 3 аргументи що репрезентують довжину, висоту та ширину паралелепіпеда")
        quit()
        
    i = 1
    while i < len(argArr):
        for c in argArr[i]:
            if not c.isdigit():
                print("Аргументи мусять бути числами")
                quit()
        i+=1
    
    return argArr

def parseNumsFromArgs(argArr):
    numList = list()
    i = 1
    while i < len(argArr):
        numList.append(float(argArr[i]))
        i+=1
        
    return numList

def calculateArea(numArr):
    x = numArr[0]
    y = numArr[1]
    z = numArr[2]
    return x*y + x*z + y*z

def calculateValume(numArr):
    x = numArr[0]
    y = numArr[1]
    z = numArr[2]
    return x * y * z

numArr = parseNumsFromArgs(checkArgs(sys.argv))
area = str(calculateArea(numArr))
volume = str(calculateValume(numArr))
print("Surface area:" + area)
print("Volume:" + volume)