def findDuplicates(numbers):
    slow,fast = 0,0
    while True:
        slow = numbers[slow]
        fast = numbers[numbers[fast]]
        if slow == fast:
            break
    
    slow2 = 0
    while True:
        slow = numbers[slow]
        slow2 = numbers[slow2]
        if slow == slow2:
            return slow