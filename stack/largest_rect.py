def largest_rect(heights:list):
    
    stack = []
    maxArea =0
    for i,h in enumerate(heights):
        newIndex =i 
        while stack and stack[-1][1] > h:

            index, height =stack.pop()
            maxArea= max(maxArea, height * (i - index))
            newIndex = index
        stack.append((newIndex,h))

    print(stack)
    for i,h in stack:
        currArea = h* (len(heights) - i)
        maxArea = max(maxArea, currArea)
    return maxArea

print(largest_rect([1,3,4,2,1,]))