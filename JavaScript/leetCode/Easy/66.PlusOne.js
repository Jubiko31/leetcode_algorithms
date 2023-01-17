/**---------------------------------
===========Plus One================

* ? You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
* ? The digits are ordered from most significant to least significant in left-to-right order. 
* ? The large integer does not contain any leading 0's.

Example 1: 
Input: digits = [1,2,3]
Output: [1,2,4]
* TODO Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

Example 2:
Input: digits = [9]
Output: [1,0]

---------------------------------/*

/**
 * @param {number[]} nums
 * @return {number[]}
 */

const plusOne = (nums) => {
    const num = BigInt(nums.join('')) + 1n
    return [...('' + num)].reduce((acc, n) => acc.concat(+n), []);
}

// Beats: 76.49% | Memory: 42.5 MB