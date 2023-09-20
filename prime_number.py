def prime(n):
    if n < 2 :
        return ("not a prime")
    for i in range(2,int(n**0.5)+1):
        if n%i==0 :
            return ("not a prime")
    return ("prime")
n=int(input())
print(prime(n))