# ===========Two Sum================

# ? Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# ! You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums: list[int], target: int) -> list[int]:
    
    for i in range(len(nums)):
        sub = target - nums[i]
        if sub in nums:
            if i != nums.index(sub):
                return [i, nums.index(sub)]
        
    return -1        

x = twoSum(nums=[2,7,11,15], target=9)
print(x)

# Runtime: 37.93% | Memory: 77.96%