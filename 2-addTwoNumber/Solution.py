from list.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 链表转成列表
        a1 = []
        a2 = []
        while (l1):
            a1.append(l1.val)
            l1 = l1.next
        while (l2):
            a2.append(l2.val)
            l2 = l2.next

        # 列表转成字符串
        s1 = ''
        for i in range(len(a1) - 1, -1, -1):
            s1 = s1 + str(a1[i])
        s2 = ''
        for j in range(len(a2) - 1, -1, -1):
            s2 = s2 + str(a2[j])

        # 字符串转成整数
        m1 = int(s1)
        m2 = int(s2)
        # 整数之和转成字符串
        m3 = str(m1 + m2)

        # 新建两个空链表
        tmp_node = ListNode(None)
        node = ListNode(None)
        # 从后往前遍历和字符串，插入链表
        for x in m3[::-1]:
            # print(x)
            if not tmp_node.val:
                tmp_node.val = x
                node = tmp_node
                # print(node)
            else:
                tmp_node.next = ListNode(x)
                tmp_node = tmp_node.next

        return node