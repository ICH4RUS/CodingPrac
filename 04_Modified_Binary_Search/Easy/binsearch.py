nums=[2,4,5,6,8,10]
target=8
left,right=0,len(nums)-1
while left<=right: #so as to check the last element as well
    mid=(left+right)//2
    if nums[mid]==target:
        print("The number was found in index:",mid)
        break
    
    elif target>nums[mid]:
        left=mid+1
    else:
        right=mid-1 
else:
    print(-1)


