arr=[0,1,5,3,6,2]

n=len(arr)

expected=n*(n+1)//2

actual=sum(arr)


print(expected-actual)