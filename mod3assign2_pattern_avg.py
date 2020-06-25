rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
    
    
n=int(input("Enter elements"))
a=[]
for i in range(0,n):
    elem=int(input("Enter element"))
    a.append(elem)
avg=sum(a)/n
print("Average",round(avg,2))   
    