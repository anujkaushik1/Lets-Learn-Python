
l1 = [1,3.14,"Derek",True];

print("Length", len(l1));
print("First",l1[0]);
print("last",l1[-1]);

l1[0] = 4;
l1[2:4] = ["Bob",False];  #2,3
l1[2:2] = ["paul",9]  #insert at this position without deleting

l2 = l1 + ["Egg,4"];
l2.remove("paul");
l2.pop(0);
print("l2===",l2);

l3 = [[1,2],[2,4]];
print("[1,1]",l3[1][1]);

print("1 exists",1 in l1);
print("Min", min[1,2,3]);
print("Max", max(1,2,3));
print("Reverse", l1[::-1]);

