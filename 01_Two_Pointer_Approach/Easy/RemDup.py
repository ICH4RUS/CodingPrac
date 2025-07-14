#To remove duplicates from a sorted array
a=[1,1,2,3,3,4]
i=1
for j in range(1,len(a)):
    if a[j]!=a[i-1]:
        a[i]=a[j]
        i+=1
print(i)
print(a[:i])