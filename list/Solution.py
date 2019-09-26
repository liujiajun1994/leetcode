from ListNode import ListNode

class Solution(object):
    # 删除链表中的节点
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # print(listNodeToString(node))
    # 删除链表的倒数第N个节点
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listNode = []
        while head:# 将每个节点存放在列表中
            listNode.append(head)
            head = head.next
        if 1 <= n <= len(listNode):# 如果n在列表个数之内的话
            n = len(listNode) - n# n原本是倒数位置，现在赋值为正方向位置
            if n == 0:# 如果是删除第1个位置的节点
                if len(listNode) > 1:# 如果节点总数大于1
                    listNode[0].val = listNode[1].val# 删除第1个位置
                    listNode[0].next = listNode[1].next
                else:
                    return None# 因为节点一共就1个或0个，所以删除1个直接返回None
            else:
                listNode[n - 1].next = listNode[n].next# 将该节点的上一个节点的后节点赋值为该节点的后节点，即删除该节点
        return listNode[0]
    # 反转链表
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listNode = []
        while head:
            listNode.append(head)
            head = head.next
        if len(listNode) == 0:
            return None
        for i in range(int(len(listNode) / 2)):# 将节点的值收尾分别调换
            listNode[i].val, listNode[len(listNode) - i - 1].val = listNode[len(listNode) - i - 1].val, listNode[i].val
        return listNode[0]
    # 合并两个有序链表
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newList = ListNode(0)
        newList.next = l1
        prev= newList# 获得新链表

        while l2:
            if not l1:# 如果l1不存在，直接返回l2即可
                prev.next = l2
                break
            if l1.val > l2.val:# 1，判断l1和l2哪个大，如果l2小，则将新节点的后面设为l2的头节点，并将头节点的后面设置为l1，反之l1小，则直接将头节点的后面设置为l1，并将节点后移
                temp = l2
                l2 = l2.next
                prev.next = temp
                temp.next = l1
                prev = prev.next#
            else:# 反之l2大于l1，则是l1节点向后移
                l1, prev = l1.next, l1
        return newList.next
    # 回文链表
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listNode = []
        while head:
            listNode.append(head)
            head = head.next
        for i in range(int(len(listNode) / 2)):# 判断两头的值是否一样大
            if listNode[i].val != listNode[len(listNode) - i - 1].val:
                return False
        return True
    # 环形链表
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1=p2=head
        while p2.next and p2.next.next:# p1走1步，p2走两步，如果在链表没走完的情况下，找到完全相同的节点，就是找到环了
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        return False
