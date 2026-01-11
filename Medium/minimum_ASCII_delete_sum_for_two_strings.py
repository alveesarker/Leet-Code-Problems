heights = [2,1,5,6,2,3]
left_smallest_value = []
s =[]
for j in range(len(heights)):
    print(j, s)
    while len(s) > 0 and heights[s[-1]] >= heights[j]:
        s.pop(-1)
    if len(s) == 0:
        left_smallest_value.append(-1)
    else:
        left_smallest_value.append(s[-1])
    s.append(j)
    
print(left_smallest_value)

print(s)