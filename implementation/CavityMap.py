def checkGreater(arr, arrInd, strInd):
    isGreater = True;
    if(arr[arrInd][strInd] <= arr[arrInd][strInd+1]):
        isGreater = False;
    elif(arr[arrInd][strInd] <= arr[arrInd][strInd-1]):
        isGreater = False;
    elif(arr[arrInd][strInd] <= arr[arrInd+1][strInd]):
        isGreater = False;
    elif(arr[arrInd][strInd] <= arr[arrInd-1][strInd]):
        isGreater = False;
    return isGreater;

arrSize = int(raw_input());
cavityMap = [ raw_input() for i in range(arrSize)]

for arrInd in range(1,arrSize-1):
    charList = list(cavityMap[arrInd]);
    for strInd in range(1, arrSize-1):
        if(checkGreater(cavityMap, arrInd, strInd)):
            charList[strInd] = "X";
            strArrElement = ''.join(charList);
            cavityMap[arrInd] = strArrElement;

for arrElem in cavityMap:
    print arrElem