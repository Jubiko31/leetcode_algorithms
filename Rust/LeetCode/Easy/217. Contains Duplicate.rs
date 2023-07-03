// ===========Contains Duplicate================

// ? Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example:
// Input: nums = [1,2,3,1]
// Output: true

use std::collections::HashSet;

pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    let nums_set: HashSet<i32> = nums.iter().cloned().collect();
    nums.len() != nums_set.len()
}

// Runtime:  84.08% | Memory: 70.31%