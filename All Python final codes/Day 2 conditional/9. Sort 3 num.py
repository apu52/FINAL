a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if(a>b and a>c):
    print(a,"is the largest no.")
    if(b>c):
        print(b,"is the second largest no")
        print(c,"is the smallest no.")
    else:
        print(c,"is the second largest no")
        print(b,"is the smallest no.")
if(b>a and b>c):
    print(b,"is the largest no.")
    if(a>c):
        print(a,"is the second largest no")
        print(c,"is the smallest no.")
    else:
        print(c,"is the second largest no")
        print(a,"is the smallest no.")
if(c>a and c>b):
    print(c,"is the largest no.")
    if(a>b):
        print(a,"is the second largest no")
        print(b,"is the smallest no.")
    else:
        print(b,"is the second largest no")
        print(a,"is the smallest no.")