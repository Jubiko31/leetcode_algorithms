/**
===========Single Number================

* ? Given a non-empty array of integers numbers, every element appears twice except for one. Find that single one.
* ! You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1: 
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

---------------------------------/*
/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNumber = (nums) => {
    let xorsum = 0;
    for(let num of nums) {
        xorsum = xorsum ^ num;
    }
    return xorsum;
};

// Runtime: 83.47% | Memory: 68.20%