/**---------------------------------
===========Add Binary================

* ? Given two binary strings a and b
* TODO return their sum as a binary string.

Example 1: 
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

---------------------------------/*
/**
 * @param {string} a
 * @param {string} b
 * @return {string} 
 */

const addBinary = (a, b) => {
    return (BigInt(`0b${a}`) + BigInt(`0b${b}`)).toString(2)
};

// Beats: 89.79% | Memory: 42.3 MB