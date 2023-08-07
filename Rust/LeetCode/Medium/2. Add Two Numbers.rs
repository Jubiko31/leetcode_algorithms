// ===========Add Two Numbers================

// ? You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list..

// ! You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]


pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut head = Box::new(ListNode::new(0));
    let mut curr = &mut head;
    let mut carry = 0;

    let (mut l1, mut l2) = (l1, l2);

    while l1.is_some() || l2.is_some() || carry != 0 {
        let mut sum = carry;
        if let Some(node) = l1.take() {
            sum += node.val;
            l1 = node.next;
        }

        if let Some(node) = l2.take() {
            sum += node.val;
            l2 = node.next;
        }

        carry = sum / 10;
        curr.next = Some(Box::new(ListNode::new(sum % 10)));
        curr = curr.next.as_mut().unwrap();
    }

    head.next
}

// Runtime: 64.81% | Memory: 56.84%
