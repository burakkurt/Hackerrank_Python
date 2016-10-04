def depthFirstSearch(matrix, startCoord):
    coordSet = set();
    stack = [startCoord];
    coordSet.add(startCoord);
    matrix[startCoord[0]][startCoord[1]] = 'X';

    regionSize = 1;

    while(len(stack) > 0):
        coord = stack.pop(0);

        neighborList = findNeighbors(matrix, coord)


        for neighbor in neighborList:
            if not coordSet.__contains__(neighbor):
                stack.insert(0, neighbor);
                coordSet.add(neighbor);
                matrix[neighbor[0]][neighbor[1]] = 'X';
                regionSize += 1;

    return regionSize

def findNeighbors(matrix, coordinate):
    rowSize = len(matrix);
    colSize = len(matrix[0]);

    y = coordinate[0];
    x = coordinate[1];

    neighborList = []
    if(y > 0 and matrix[y-1][x] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y-1,x));
    if(x > 0 and matrix[y][x-1] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y,x-1));
    if(y < rowSize-1 and matrix[y+1][x] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y+1,x));
    if(x < colSize-1 and matrix[y][x+1] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y,x+1));
    if(x > 0 and y > 0 and matrix[y-1][x-1] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y-1,x-1));
    if(x < colSize-1 and y > 0 and matrix[y-1][x+1] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y-1,x+1));
    if(x > 0 and y < rowSize-1 and matrix[y+1][x-1] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y+1,x-1));
    if(x < colSize-1 and y < rowSize-1 and matrix[y+1][x+1] == '1' and (matrix[y][x] == '1' or matrix[y][x] == 'X')):
        neighborList.append((y+1,x+1));

    return neighborList;


matrix = []

rowSize = int(raw_input());
colSize = int(raw_input());

for row in range(rowSize):
    line = str(raw_input());
    line = line.split(' ');
    line[len(line)-1] = line[len(line)-1].strip('\r');
    matrix.append(line);

biggestRegion = 0;
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if(matrix[row][col] == '1'):
            dfs = depthFirstSearch(matrix, (row,col));
            if(biggestRegion < dfs):
                biggestRegion = dfs;

print biggestRegion