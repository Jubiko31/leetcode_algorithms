# ===========24 Game================

# ? You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

# ? You are restricted with the following rules:

# ! The division operator '/' represents real division, not integer division.
# ! For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# ! Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# ! For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# ! You cannot concatenate numbers together
# ! For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.

# TODO: Return true if you can get such expression that evaluates to 24, and false otherwise.


def judgePoint24(self, cards: list[int]) -> bool:    
    length = len(cards)
    
    if length == 1:
        return abs(cards[0] - 24) < 1e-6

    for i in range(length):
        for j in range(i + 1, length):
            a, b = cards[i], cards[j]
            shuffled_cards = [cards[n] for n in range(length) if n != i and n != j]

            if judgePoint24(self, shuffled_cards + [a + b]): # check addition
                return True 
            if judgePoint24(self, shuffled_cards + [a - b]): # check subscription
                return True 
            if judgePoint24(self, shuffled_cards + [b - a]): # check subscription
                return True
            if judgePoint24(self, shuffled_cards + [a * b]): # check multiply
                return True

            if b != 0 and judgePoint24(self, shuffled_cards + [a / b]): # check division
                return True 
            if a != 0 and judgePoint24(self, shuffled_cards + [b / a]): # check division
                return True

    return False

# Runtime: 95.06% | Memory: 52.03%
