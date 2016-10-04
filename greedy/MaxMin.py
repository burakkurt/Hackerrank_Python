
size = int(raw_input());
k = int(raw_input());

numList = [int(raw_input()) for number in range(size)]
numList.sort()

minimum = 2000000000;
for i in range(size-(k-1)):
    tempMin = numList[i];
    tempMax = numList[i+(k-1)];
    subtract = tempMax -  tempMin;
    if ( subtract < minimum ):
        minimum = subtract;

print minimum;