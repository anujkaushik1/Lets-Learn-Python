
age = 30;

if age > 40:
    print("age is greater than 40");
elif age > 20:
    print("age is greater than 20");
else:
    print("all conditions failed");


if age < 5:
    print("stay home");
elif (age >=5) and (age<=6):
    print("go to school");
else:
    print("college")

#------------------------------------------------------------------------

canVote = True if age >=18 else False;
print(canVote)