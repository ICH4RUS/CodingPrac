nums = [5,-1, 3, 2, 7, 4]
k = 3
s=sum(nums[:k])
m=s
for i in range(k,len(nums)):
    s+=nums[i]-nums[i-k]
    if s>m:
        m=s
print(m/k)
