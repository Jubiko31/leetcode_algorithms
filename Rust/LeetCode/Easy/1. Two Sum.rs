// ===========Two Sum================

// ? Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// ! You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut hashmap: HashMap<i32, usize> = HashMap::new();

    for (i, &num) in nums.iter().enumerate() {
        let sub = target - num;
        if let Some(&index) = hashmap.get(&sub) {
            if i != index {
                return vec![i as i32, index as i32];
            }
        }
        hashmap.insert(num, i);
    }

    vec![];
}

// Runtime: 83.45% | Memory: 26.99%