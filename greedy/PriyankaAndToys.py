
numToys = int(raw_input());
toys = map(int, raw_input().split());
toys.sort();

priceLeft = toys[0];
priceRight = priceLeft + 4;

numToysToBuy=1;
for i in range(1,numToys):

    if(toys[i]>=priceLeft and toys[i]<=priceRight):
        continue;
    else:
        numToysToBuy += 1;
        priceLeft=toys[i];
        priceRight=priceLeft+4;

print numToysToBuy;
