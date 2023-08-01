/**
===========Pascal's Triangle II================

* ? Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Example 1: 
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input rowIndex = 1
Output: [1,1]

---------------------------------/*
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
const pascalTriangleII = (rowIndex) => {
    const triangle = []

    while (triangle.length <= rowIndex) {
        triangle.unshift(1)
        for (let idx = 1; idx < triangle.length - 1; idx++) {
            triangle[idx] += triangle[idx + 1]
        }
    }

    return triangle;
};

// Runtime: 90.15% | Memory: 97.43%