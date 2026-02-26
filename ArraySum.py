nums = [2,7,11,15]
target = 9
# print(len(nums))
for i in range (0,len(nums)):
    for j in range(i+1, len(nums)):
        c = nums[i]
        d = nums[j]
        sum = c + d 
        if(sum==target):
            print([i,j])
    
 
