// ==============Length of Last Word================

// ? Given a string s consisting of words and spaces, return the length of the last word in the string.
// ! A word is a maximal substring consisting of non-space characters only.

// Input: s = "Hello World"
// Output: 5
// Explanation: The last word is "World" with length 5.

// Input: s = "   fly me   to   the moon  "
// Output: 4
// Explanation: The last word is "moon" with length 4.

pub fn length_of_last_word(s: String) -> i32 {
    let vector_of_s: Vec<&str> = s.split_whitespace().collect();
    if let Some(last_element) = vector_of_s.last() {
        return last_element.len() as i32;
    } else {
        0
    }
}

// Runtime: 100% | Memory: 94.95%
