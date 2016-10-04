numTest = int(raw_input());

for i in range(numTest):
    word = raw_input();

    if(len(word)%2 == 1):
        print -1;
        continue;

    firstWord = word[:len(word)/2];
    secondWord = word[len(word)/2:];

    dictFirstWord = {}
    dictSecondWord = {}

    for letter in firstWord:
        dictFirstWord[letter] = dictFirstWord.get(letter,0) + 1;
    for letter in secondWord:
        dictSecondWord[letter] = dictSecondWord.get(letter,0) +1 ;

    numChange = 0
    for letter in dictSecondWord.keys():
        if(dictFirstWord.get(letter,0) != dictSecondWord.get(letter,0)):
            difference =  dictSecondWord.get(letter,0) - dictFirstWord.get(letter,0)
            if(difference > 0):
                numChange += difference;

    print numChange