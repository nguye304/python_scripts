print("Anagram Solver")
'''
Find All Anagrams in a String
Returns the index where the anagram starts
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
'''

s = input("Please enter a word: ")
p = input ("\nPlease enter a second word to check if there is an anagram: ")
#s="cbaeba"
#p = "bae"

def findAnagrams(origin, goal):
    #print("The origin is: " +origin + ". The goal is: "+ goal);
    answers = [];

    size = len(goal);# size of goal
    w = 0 ;
    x= 0;
    #I need to somehow split origin into chunks of goal's size
    #the code below chunks it into all possibe combinations of each size
    while x <= len(origin)-size: #while there is enough letters left for a possible anagram
        chunk = [];
        shouldIContinue=True;
        w=x;#w is the index of the word
        
        #this code below gets one chunk
        while shouldIContinue == True:
            if len(chunk) < size:
                chunk.append(origin[w]);
                shouldIContinue = True;
                w+=1;
            else:
                shouldIContinue = False;

        word1 = chunk;
        word1 = sorted(word1);
        word2 = sorted(goal);
        #print("word1: " + str(word1) + "    word2: " + str(word2));
        result = isItAnagram(word1,word2);

        if result == True:
            answers.append(x);
        x+=1;

    print(answers);
  
def isItAnagram(word1,word2):
    if word1 == word2:
        return True;
    else:
        return False;
    
findAnagrams(s,p);

