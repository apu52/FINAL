import Primemodule as p
l1 = int(input("Enter lower limit: "))
l2 = int(input("Enter upper limit: "))
c=0
for i in range(l1+1,l2):
    if p.prime(i) == 0:
        print(i, end = " ")
        c+=1
if c==0 :
    print("There are no prime numbers between", l1,"&",l2)