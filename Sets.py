

s1 = set(["Anuj Kaushil",1]);
s2 = {"Paul",1};

print("Length",len(s2));
s3 = s1 | s2;
print(s3);
s3.add("Sough");
s3.discard("Anuj Kaushik");
print("Random",s3.pop());
print(s1.intersection(s2));


