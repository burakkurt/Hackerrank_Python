import string

charDict = {};
i=1;
for char in string.lowercase:
    charDict[char] = i;
    i+=1;

numTest = int(raw_input());
for test in range(numTest):
    word = raw_input();
    upperbound = (len(word) / 2);

    firstPart = word[:upperbound];
    if(len(word) % 2 == 0):
        secondPart = word[len(word)-1:upperbound-1:-1];
    else:
        secondPart = word[len(word)-1:upperbound:-1];

    numOperation = 0;
    for index in range(len(firstPart)):
        if(firstPart[index] != secondPart[index]):
            #print firstPart[index] + " ! " + secondPart[index];
            numOperation += abs(charDict.__getitem__(firstPart[index]) - charDict.__getitem__(secondPart[index]));

    print numOperation;