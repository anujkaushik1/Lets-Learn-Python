
# recursion question -> print decreasing

def printDec(n):
    if (n == 0) :
        return;

    print(n);
    printDec(n-1);


n = int(input());
printDec(n);

def mult_by(num):
    return lambda x : x * num
print("3 * 5 = ",(mult_by(3)(5)));



