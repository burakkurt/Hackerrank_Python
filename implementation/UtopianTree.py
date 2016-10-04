__author__ = 'burak'

def spring(height):
    height *= 2;
    return height;

def summer(height):
    height += 1;
    return height;

numTest = int(raw_input().strip());

for test in range(numTest):
    height = 1;
    numSeason = int(raw_input().strip());

    isSpring = True;
    for season in range(numSeason):
        if(isSpring):
            height = spring(height);
            isSpring = False;
        elif(isSpring == False):
            height = summer(height);
            isSpring = True;

    print height;
