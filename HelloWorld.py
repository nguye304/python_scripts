#this file is my first python file

my_name = "Kevin Nguyen";
my_age = 23;

print("Hello World");
print("My name is "+ my_name);
print("My age is "+ str(my_age));

print("Starts at index" + str(my_name.index("Kevin")));
#.index allows you to search through your string and find where there is the "e"
#If you put more than just a character then it will return you where it starts

print("My new name is "+my_name.replace("Nguyen","Ngo"));
#you can use .replace(what to replace, what to replace with)
'''
#----------------------GETTING USER INPUTS------------------------------
your_name = input("Enter your name : ");
print("Hello " + your_name);

print("Lets use a calculator");
num1 = input("Enter first number: ");
num2 = input("Enter second number: ");

num3  = float(num1)+float(num2);
print("The sum is : " + str(num3));
'''
#----------------------LISTS--------------------------------------------
#you can put different types into the same list

my_friends = ["Ana","Jr","Daniel","Charles","Marielle"];
my_friends_2 = ["Carl","James","Luis"];
print("My Friends: "+str(my_friends)+"\n");#print entire array
print("The friend at index 0: "+str(my_friends[0])+"\n");#print certain index
print("Friends from index 0 to 2: "+ str(my_friends[0:3])+"\n");#print a certain range of index ie: from position 0 to 2 since it doesnt include 3

#list functions
anaIndex = my_friends.index("Ana");#returns the smallest index where Ana is.
#can be an easy way to find if something is in the list

print("check where Ana is in the list "+str(anaIndex));

my_friends.extend(my_friends_2);#adds multiple lists together
print("my_friends1 combined with my_friends_2 :"+ str(my_friends)+"\n");

my_friends.append("Joey");#adds another entry(only 1) into the array at the end
print("Appened Joey :"+ str(my_friends)+"\n");

my_friends.insert(1,"Mom");#inserts an entry at a certain index; It will push everyone after by one index
print("Inserted Mom at index 1 :"+ str(my_friends)+"\n");

my_friends_3 = my_friends.copy();#copys a list to another list (shallow copy)
print("my_friends copied :"+ str(my_friends_3)+"\n");

my_friends_3.clear();#removes all items from list
print("Cleared my firneds 3: "+str(my_friends_3)+"\n");

my_friends.remove("Joey");
print("\nRemoved Joey : " + str(my_friends));

my_friends_3 = my_friends.reverse();
print("\n my friends: "+ str(my_friends));
print("\n my friends 3: "+str(my_friends_3));

numKevin = my_friends.count("Ana");
print(numKevin);

my_friends.remove(my_friends[2]);
print(my_friends);

