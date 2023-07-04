def Moore(nums):
    ele = None
    vote = 0
    for i in range(len(nums)):
        if vote == 0:
            ele = nums[i]
        if nums[i] == ele:
            vote += 1
        else:
            vote -= 1
    
    return ele
