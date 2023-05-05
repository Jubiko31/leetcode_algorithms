# ===========Sqrt(x)================

# ? Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# ! You must not use any built-in exponent function or operator.

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

def sqrt(x):
    """
    :type x: int
    :rtype: int
    """
    res = precision = 0.0001
    while res*res <= x:
        res -= 1
        while res*res < x:
            res += precision
    
    return res
    
# Runtime: 27.49% | Memory: 98.56%