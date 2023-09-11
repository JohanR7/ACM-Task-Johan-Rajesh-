def yo(n):
    a=1
    i=2
    while i*i<=n:
        if n%i:
            i+=1
        else:
            n//=i
            a=i
    if n>1:
        a=n
    return a
n=int(input("Enter a number:"))
print(yo(n))

