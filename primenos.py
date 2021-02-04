def count_primes(num):
    if num==0 or num==1:
        return 0
    #To check whether a no is prime and then append it to a list
    prime=[]
    c=2
    while c<=num:
        fact=0
        for i in range(num+1):
            if i>c:
                break
            elif i<=c:
                if i%c==0 or c%i==0:
                   fact=fact+1
        if fact==3:
            prime.append(c)
        c=c+1
    #To count the no of prime numbers
    count=0
    for j in prime:
        count=count+1
    return count

print(count_primes(100))
