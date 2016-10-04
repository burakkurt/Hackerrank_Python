#ÇÖZÜLEMEDİ


fileOpen = open("input.txt", "r");

size = int(fileOpen.next());
numberLine = str(fileOpen.next());
numbers = numberLine.split(" ")
numbers[len(numbers)-1] = numbers[len(numbers)-1].strip("\n")

subtrahendLine = str(fileOpen.next());
subtrahends = subtrahendLine.split(" ")
subtrahends[len(subtrahends)-1] = subtrahends[len(subtrahends)-1].strip("\n")
p = int(subtrahends[0])
q = int(subtrahends[1])

numbers.sort()
print numbers

maxMin = 0
result = 0
for i in range(len(numbers)):
    tempMin = 0
    tempResult = 0
    if(p>numbers[i]):
        tempMin = abs(p-int(numbers[i]));
        tempResult = p;
    elif(q<numbers[i]):
        tempMin = abs(int(numbers[i])-q);
        tempResult = q;
    elif(numbers[i] >= p and numbers[i] <= q):
        print "elif"
        tempMin = 1;
        tempResult = numbers[i]

    if(tempMin > maxMin):
        maxMin = tempMin
        result = tempResult

    print "number : ",numbers[i],"tempMin",tempMin

print ""
print result