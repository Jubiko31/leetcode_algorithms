# ===========Fizz Buzz================

# ? Given an integer n, return a string array answer (1-indexed) where:

# ? answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# ? answer[i] == "Fizz" if i is divisible by 3.
# ? answer[i] == "Buzz" if i is divisible by 5.
# ? answer[i] == i (as a string) if none of the above conditions are true.

# Example:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
    
    
def fizzBuzz(n: int) -> list[str]:
    fizzbuzz = []
    
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0: fizzbuzz.append("FizzBuzz")
        elif num % 3 == 0: fizzbuzz.append("Fizz")
        elif num % 5 == 0: fizzbuzz.append("Buzz")
        else: fizzbuzz.append(f"{num}")
    
    return fizzbuzz
    
# Runtime: 61.15% | Memory: 94.15%