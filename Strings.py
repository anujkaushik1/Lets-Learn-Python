
print(r"I will be ignored "" ' ' ");
print("hello" + "world");
str = "Hello world";
print("length", len(str));
print("1st char = ", str[0]);
print("last char = ",str[-1]);  #last char

print();
print();

print("1st 3 char", str[0:3])  #substring
print("Every other char", str[0:-1])  #print all char till last
print("testing",str[0:-1:2]);

print();
print();
print();

print("you" in str)
print("you" not in str)

print("your index = ", str.find("you"))
print("     Hello    ".strip());
print("A string".split(", "))


