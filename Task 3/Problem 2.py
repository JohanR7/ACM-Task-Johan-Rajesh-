def simpleArraySum(ar):
    total=sum(ar)
    return total
a=int(input('Enter the size of the array:'))
ar=list(map(int,input("Enter the array elements separated by space:").split()))
result=simpleArraySum(ar)
print(result)


    
