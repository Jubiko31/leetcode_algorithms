// ===========Two Sum================

// ? Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// ! You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

var twoSum = function(nums, target) {
    let numbers = new Map();
    for (let i = 0; i < nums.length; i++) {
        let a = nums[i];
        let b = target - nums[i];
        if (numbers.has(b)) {
            return [i, numbers.get(b)]
        }
        numbers.set(a,i);
    }
};

// Runtime: 53.18% | Memory: 29.16%