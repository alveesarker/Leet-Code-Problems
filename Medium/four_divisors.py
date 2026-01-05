nums = [1,2,3,4,5]


sum = 0
for i in nums:
    sum_in = i
    count = 1
    for j in range(1, (i//2)+1):
        if i % j == 0:
            count += 1
            # print(count)
            sum_in += j
        if count == 5:
            break
    if count == 4:
        sum+=sum_in
        
print(sum)