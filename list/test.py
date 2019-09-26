from ListNode import ListNode
from Solution import Solution

head = [1,2,3,4,5]
head2 = [4, 5, 8, 9]
s = Solution()

print(s.deleteNode(ListNode.stringToListNode(head)))
print(ListNode.listNodeToString(s.removeNthFromEnd(ListNode.stringToListNode(head), 1)))  # 删除倒数第一个位置
print(ListNode.listNodeToString(s.reverseList(ListNode.stringToListNode(head))))  # 翻转
print(ListNode.listNodeToString(s.mergeTwoLists(ListNode.stringToListNode(head2), ListNode.stringToListNode(head))))  # 合并两个链表
print(s.isPalindrome(ListNode.stringToListNode(head)))
print(s.hasCycle(ListNode.stringToListNode(head)))