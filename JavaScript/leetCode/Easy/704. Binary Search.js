/**
===========Binary Search================

* ? Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
* ! You must write an algorithm with O(log n) runtime complexity.

Example 1: 
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 Exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

---------------------------------/*
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const divideAndConquer = (nums, target) => {
    let start = 0;
    let end = nums.length - 1;

    while (start <= end) {
        const midIndex = Math.floor((start + end) / 2);
        const pointer = nums[midIndex] // middle element we are pointing
        if (pointer === target) {
            return midIndex;
        } else if (pointer < target) {
            start = midIndex + 1;
        } else {
            end = midIndex - 1;
        }
    }
    return -1;
};

// Runtime: 82.70% | Memory: 90.17%