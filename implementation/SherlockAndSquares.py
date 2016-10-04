__author__ = 'burak'

import math

numTest = int(raw_input().strip());

for test in range(numTest):
    first,second = raw_input().strip().split(' ');
    first, second = [int(math.ceil(math.sqrt(float(first)))),int(math.floor(math.sqrt(float(second))))];

    intSquare = second-first+1;

    print intSquare;