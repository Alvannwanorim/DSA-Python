def trail():
    nums =[[1,2,3]]
    copy = list([lambda num: num, nums])
    print(copy)
    num = list(map(lambda num : num, nums[0])) + [4]
    print(num)
trail()