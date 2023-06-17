def kadane(nums):
    current_max = nums[0]
    max_so_far = nums[0]
    for num in nums[1:]:
        current_max = max(current_max + num, num)
        max_so_far = max(current_max, max_so_far)
    return max_so_far
