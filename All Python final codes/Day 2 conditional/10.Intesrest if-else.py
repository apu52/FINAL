p = float(input("Enter the Principal amount: "))
t = int(input("enter the time of the amount: "))

if(p<200000):
    I=(p*10*t)/100
elif(p>200000 and p<1000000):
    I=(p*12*t)/100
elif(p>1000000):
    I=(p*15*t)/100
else:
    print("NO AMOUNT WILL BE REFUNDED")

print("The Interest is: ",I)