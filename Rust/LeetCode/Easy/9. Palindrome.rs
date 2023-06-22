// ==============Palindrome================

// ? Given an integer x, return true if x is a palindrome, and false otherwise.

// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.

pub fn is_palindrome(x: i32) -> bool {
    if x < 0 || (x != 0 && x % 10 == 0) {
        return false; 
    }

    let mut reversed: i32 = 0;
    let mut length: i32 = x;

    while length > 0 {
        let digit = length % 10;
        reversed = (reversed * 10) + digit;
        length /= 10;
    }
    
    x == reversed
}

// Runtime: 100% | Memory: 91.63%