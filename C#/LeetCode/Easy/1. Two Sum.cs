// ===========Two Sum================

// ? Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// ! You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

using System;
using System.Collections.Generic;

public int[] TwoSum(int[] nums, int target) {
    Dictionary<int, int> hashmap = new Dictionary<int, int>();

    for (int i = 0; i < nums.Length; i++) {
        int sub = target - nums[i];
        if (hashmap.TryGetValue(sub, out int index) && i != index) {
            return new int[] { i, index };
        }
        hashmap[nums[i]] = i;
    }

    return new int[0];
}

// Runtime: 96.61% | Memory: 16.74%