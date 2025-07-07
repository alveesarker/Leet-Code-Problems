nums = [0,0,1,1,1,2,2,3,3,4]
t_num = nums[0]
for i in range(len(nums)-1, -1, -1):
    if nums[i] == t_num:
        nums.remove(nums[i])
        nums.append("_")
    else:
        t_num = nums[i]
        
print(nums)