# ===========Climbing Stairs================

# ? You are climbing a staircase. It takes n steps to reach the top.

# ? Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

def climbStairs(n: int):
    # Solution with Fibonacci: Fn = Fn-1 + Fn-2
    n = n + 1
    mem = {}
    
    def fibonacci_formula(n):
        φ = (1 + 5 ** 0.5) / 2
        Ψ = (1 - 5 ** 0.5) / 2        
        return int((1 / 5 ** 0.5) * (φ**n - Ψ**n))
    
    if n in mem:
        return mem[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_formula(n)
        mem[n] = result
        return result
    
# Runtime: 80.88% | Memory: 26.93%