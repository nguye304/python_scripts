#do string maniupatlions
# reverse , see how many vowels,
#palindrome = see if word spelled backwards and forwards is the samme

usersinput = input("Please enter a word to see if it is a palindrome: ");

def isItPalindrome2(word):
    reversedword = word[::-1];#this reverses a string 
    if reversedword==word:
        return True;
    else:
        return False;

     
def isItPalindrome(word):
    wordarr=[];
    wordarr2=[];
    for letter in word:
        if letter != ' ':
            wordarr.insert(0,letter);
            wordarr2.append(letter);
    if wordarr == wordarr2:
        return True;
    else:
        return False;
    
   


result = isItPalindrome2(usersinput);
if result == True:
    print("The word " + usersinput +" is a palindrome!");
else:
    print("The word " + usersinput +" is not a palindrome!");
