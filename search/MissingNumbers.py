#Numbers from both dictionaries will be stored here
allItems = set();

#Dictionaries which will store their numbers
dictionary1 = {};
dictionary2 = {};

#Size of dictionary1
size1 = int(raw_input());

#Reading line, splitting string and adding number to the list
line1 = str(raw_input());
line1 = line1.split(' ');

#Adding numbers to the dictionary1
for number in line1:
    if (dictionary1.get(number, 0) == 0):
        dictionary1[number] = 1;
        allItems.add(number);
    else:
        dictionary1[number] += 1;

#Size of dictionary2
size2 = int(raw_input());

#Reading line, splitting string and adding number to the list
line2 = str(raw_input());
line2 = line2.split(' ');

#Adding numbers to the dictionary2
for number in line2:
    if (dictionary2.get(number, 0) == 0):
        dictionary2[number] = 1;
        allItems.add(number);
    else:
        dictionary2[number] += 1;

#missing numbers will be stored here
missingNumbers = [];

#checking for whether there is a number which doesn't exist in one of dictionary
for item in allItems:
    #If there is a number which doesn't exist in dictionary1. This number will be added to
    #missingNumbers list and will be removed from the dictionary1.
    #Same thing will be implemented for dictionary2
    if(dictionary1.get(item) != None and dictionary2.get(item) == None):
        missingNumbers.append(item);
        del dictionary1[item];
    elif(dictionary1.get(item) == None and dictionary2.get(item) != None):
        missingNumbers.append(item);
        del dictionary2[item];

#checking values of numbers for both dictionaries. If they are not equal to each other
#this number will be added to missingNumbers List
for number in dictionary1:
    if(dictionary1[number] != dictionary2[number]):
        missingNumbers.append(number);

#printing result
missingNumbers = sorted(missingNumbers);
for result in missingNumbers:
    print result,