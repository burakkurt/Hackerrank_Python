
#return maximum number of toys we can buy with our money
def maxToys(priceArr, money):
    #number of toys can be bought
    toysBought = 0;

    #iterating over toy prices
    for toyPrice in priceArr:
        #checking whether toy can be affordable. if it is, buy
        if(money >= toyPrice):
            toysBought += 1;
            money -= toyPrice;

    return toysBought;


#mapping informations
numToys, money = map(int, raw_input().split());
priceArr = map(int, raw_input().split());

#sorting price of toys in order to buy from the cheapest toy
priceArr.sort();

#calling and printing the result of method
print maxToys(priceArr, money);