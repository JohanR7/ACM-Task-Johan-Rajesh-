def yo(n):
    a,b=1,1
    sum=0
    while b<=n:
        if b%2==0:
            sum+=b
        a,b=b,a+b
    return sum
n=int(input("Enter the number"))
print(yo(n))
