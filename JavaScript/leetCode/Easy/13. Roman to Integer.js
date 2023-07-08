/**---------------------------------
===========Roman to Integer================

* ? Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
* ? Given a roman numeral, convert it to an integer.

Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

---------------------------------/*
/**
 * @param {string} s
 * @return {number}
 */

const romanToInt = function(s) {
    const roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    let result = 0;
    let prevValue = 0;
    
    for (const char of s) {
        const currentValue = roman[char];
        result += currentValue;

        if (prevValue < currentValue) {
            result -= prevValue * 2;
        }
        prevValue = currentValue;
    }

    return result;
};

// Runtime: 97.97% | Memory: 70.92%