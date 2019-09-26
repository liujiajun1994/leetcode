# 链表节点
class ListNode(object):
    def __init__(self, x):
        self.val = x # 节点值
        self.next = None

    # 将列表转换成链表
    def stringToListNode(input):
        numbers = input
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)  # 分别将列表中每个数转换成节点
            ptr = ptr.next
        ptr = dummyRoot.next
        return ptr

    # 将链表转换成字符串
    def listNodeToString(node):
        if not node:
            return "[]"
        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"