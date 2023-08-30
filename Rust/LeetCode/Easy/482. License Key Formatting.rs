// ===========License Key Formatting================

// ? You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

// ? We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

// TODO Return the reformatted license key.

pub fn license_key_formatting(s: String, k: i32) -> String {
    let s = s.replace("-", "").to_uppercase();
    let chunk = s.len() % k as usize;

    let mut result = String::new();
    if chunk > 0 {
        result.push_str(&s[0..chunk]);
    }

    for i in (chunk..s.len()).step_by(k as usize) {
        if !result.is_empty() {
            result.push('-');
        }
        result.push_str(&s[i..i + k as usize]);
    }

    result
}

// Runtime:  72.00% | Memory: 100.00%