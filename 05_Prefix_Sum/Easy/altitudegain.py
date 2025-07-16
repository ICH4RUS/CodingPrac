gain = [-5, 1, 5, 0, -7]
maxalt=currentalt=0
for i in gain:
    currentalt+=i   #Here is where prefix sum is used 
    if currentalt>maxalt:
        maxalt=currentalt
print(maxalt) 
