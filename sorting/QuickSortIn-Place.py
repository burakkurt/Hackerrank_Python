
def quickSort(numArr, l, r):
    if(l>=r):
        return;

    m = partition(numArr, l, r);

    quickSort(numArr, l, m-1);
    quickSort(numArr, m+1, r);




def partition(numArr, l, r):
    pivot = numArr[r];
    j=l-1;

    for i in range(l,r):
        if(numArr[i] <= pivot):
            j+=1;
            swap(numArr, i, j);

    swap(numArr, r, j+1);

    for item in numArr:
        print item,
    print

    return j+1;

def swap(numArr, i, j):
    temp = numArr[i];
    numArr[i] = numArr[j];
    numArr[j] = temp;

size = raw_input();
numArr = map(int, raw_input().split());

quickSort(numArr, 0, len(numArr)-1);

