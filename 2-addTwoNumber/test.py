from list.ListNode import ListNode
from Solution import Solution
head = [2, 4, 3]
head2 = [5, 6, 4]
s = Solution()

print(ListNode.listNodeToString(s.addTwoNumbers(ListNode.stringToListNode(head),ListNode.stringToListNode(head2))))