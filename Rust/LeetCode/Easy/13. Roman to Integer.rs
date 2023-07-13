// ===========Roman to Integer================

// ? Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
// ? Given a roman numeral, convert it to an integer.

// Input: s = "III"
// Output: 3
// Explanation: III = 3.

// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

pub fn roman_to_int(s: String) -> i32 {
    let ROMAN: std::collections::HashMap<char, i32> = [
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
    ]
    .iter()
    .cloned()
    .collect();

    let mut digit = 0;
    let mut initial = 0;

    for c in s.chars() {
        let current = ROMAN[&c];
        digit += current;
        if initial < current {
            digit -= initial * 2;
        }
        initial = current;
    }

    digit
}

// Runtime: 100.00% | Memory: 28.74%
