/**
===========Single Number II================

* ? Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
* ! You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1: 
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

---------------------------------/*
/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNumber = (nums) => {
    const hashmap = new Map();

    for (let num of nums) {
        if (!hashmap.has(num)) {
            hashmap.set(num, 0)
        } else {
            hashmap.set(num, 1)
        }
    }
    return [...hashmap].find(([key, val]) => val == 0)[0]
};

// Beats: 67.49% | Memory: 44.2 MB 