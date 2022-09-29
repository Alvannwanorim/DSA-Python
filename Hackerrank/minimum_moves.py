def minimumMove(arr1, arr2):
    nMoves1, num1,num2 = 0,0,0
    digit1, digit2 =0,0

    for i in range(len(arr1)):
        num1 = arr1[i]
        num2 = arr2[i]
        while num1 >0:
            digit1 = num1 %10
            digit2 = num2 %10
            nMoves1 = abs(digit1 - digit2)
            num1 = (num1 - digit1)//10
            num2 = (num2 - digit2)//10
    return nMoves1
print(minimumMove([123,543],[321, 279])) 