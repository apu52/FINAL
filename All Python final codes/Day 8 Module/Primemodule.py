def prime(a):
    flag = 0
    for i in range (2,a):
        if a % i == 0:
            flag = 1
            break
    return flag