#find the nth fibs
# 0 1 1 2 3 5 ....
from datetime import datetime

test = int(input("Which fib do you want? : "));
whichfib = int(input("Which fib method? 1 or 2?: "));

#Base Implementation 
def fib(x):
    if x <0:
        print("Incorrect Input");
    elif x == 1:
        return 0;
    elif x == 2:
        return 1;
    else:
        return fib(x-1)+fib(x-2);


#Dynamic Programming / More efficient Implementation

fibArray=[0,1];

def fib2(n):
    if(n < 0 ):
        print("Incorrect Input");
    elif (n <= len(fibArray)):
        return fibArray[n-1];
    else:
        temp = fib2(n-1)+fib2(n-2)
        fibArray.append(temp);
        return temp;

if whichfib == 2:
    startTime2=datetime.now();
    print("\nFib2: "+ str(fib2(test)));
    print("The time it took to run fib2: "+ str(datetime.now()-startTime2));
elif whichfib == 1:
    startTime=datetime.now();
    print("\nFib: " + str(fib(test)));
    print("The time it took to run fib: "+ str(datetime.now()-startTime));
elif whichfib ==3:
    startTime2=datetime.now();
    print("\nFib2: "+ str(fib2(test)));
    print("The time it took to run fib2: "+ str(datetime.now()-startTime2));
    startTime=datetime.now();
    print("\nFib: " + str(fib(test)));
    print("The time it took to run fib: "+ str(datetime.now()-startTime));
else:
    print("you didnt put 1 or 2");




