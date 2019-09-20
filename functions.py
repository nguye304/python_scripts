def my_func(name,age):
    print("Hello from my_func");
    print("Hello from my_func again");
    print("Hello " +name);
    print("your age is : " +str(age));

def check(num1,num2,num3):
    if num1==num2 and num3==num2:
        return True;
    else:
        return False;
    
def do_math(num):
    num=num+num;
    return num;
    
my_func("kevin", 12);
result = do_math(10);
print(result);
areTheyEqual = check(2,2,2);
print(areTheyEqual);
