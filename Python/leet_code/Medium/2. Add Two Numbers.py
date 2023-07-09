# ===========Add Two Numbers================

# ? You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list..

# ! You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def addTwoNumbers(l1: ListNode, l2:  ListNode) ->  ListNode:
    listnode = ListNode()
    curr = listnode
    carry = 0
    
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        carry, digit = divmod(sum, 10)
        curr.next = ListNode(digit)
        curr = curr.next
    
    return listnode.next

x = addTwoNumbers(l1=[2,4,3], l2=[5,6,4])
print(x)

# Runtime: 96.40% | Memory: 31.37%
