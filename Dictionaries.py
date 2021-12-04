
# list of key value pair

details = {
    "Name" : "Anuj Kaushik",
    "Age" : 10,

}
print("length",len(details));
print(details["Name"]);

details["Blood Group"] = "O+";

print(list(details.items()));
print(list(details.keys()));
print(list(details.values()));

del details["Blood Group"]
print(list(details.items()));

for k in details:
    print(k)

for v in details.values():
    print(v)


