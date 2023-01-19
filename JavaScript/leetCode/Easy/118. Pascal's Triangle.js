/**
===========Pascal's Triangle================

* ? Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1: 
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

---------------------------------/*
/**
 * @param {number} numRows
 * @return {number[][]}
 */
const pascalTriangle = (numRows) => {
    const triangle = []

    for (let i = 1; i <= numRows; i++) {
        row = []
        for (let j = 0; j < i; j++) {
            if (j === 0 || j === i - 1) {
                row.push(1)
            } else {
                row.push(triangle[i - 2][j - 1] + triangle[i - 2][j])
            }
        }
        triangle.push(row)
    }
    return triangle;
};

// Runtime: 55.73% | Memory: 24.97%