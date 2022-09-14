def removeDuplicates(s:str):
    stack = []
    for c in s:
        if stack and stack[-1] ==c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

print(removeDuplicates("azxxzy"))