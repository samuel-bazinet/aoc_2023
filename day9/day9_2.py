from typing import List

def is_all_zero(nums: List[int]):
    for i in nums:
        if i != 0:
            return False
    return True

def recursive_process(nums: List[int]) -> int:
    print(nums)
    if is_all_zero(nums):
        return 0
    new_nums = []
    for i in range(len(nums) -1):
        new_nums.append(nums[i+1] - nums[i])

    result = nums[0] - recursive_process(new_nums)
    print(result)
    return result

with open('input.txt', 'r') as file:
    lines = file.readlines()

    total = 0

    for line in lines:
        numbers = list(map(lambda x: int(x), line.strip().split(' ')))
        result = recursive_process(numbers)
        total += result

    print(total)