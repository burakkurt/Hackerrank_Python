import string

lowercase = string.lowercase;
uppercase = string.uppercase;
lowercaseDict = {};
uppercaseDict = {};

i=0;
for char in lowercase:
    lowercaseDict[char] = i;
    i+=1;

i=0;
for char in uppercase:
    uppercaseDict[char] = i;
    i+=1;

stringSize = int(raw_input());
string = raw_input();
encryptionKey = raw_input();

encryptedWord = "";
for char in string:
    if(lowercaseDict.has_key(char)):
        charNum = lowercaseDict.__getitem__(char)
        encryptedCharNum = (charNum + int(encryptionKey)) % 26;
        encryptedWord += lowercase[encryptedCharNum]
    elif(uppercaseDict.has_key(char)):
        charNum = uppercaseDict.__getitem__(char)
        encryptedCharNum = (charNum + int(encryptionKey)) % 26;
        encryptedWord += uppercase[encryptedCharNum]
    else:
        encryptedWord += char

print encryptedWord