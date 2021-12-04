
while True:
    try:
        number = int(input("Please enter a number"));
        break
    except ValueError:
        print("you din't enter the number");
    except:
        print("An unknown error");
print("thank you");