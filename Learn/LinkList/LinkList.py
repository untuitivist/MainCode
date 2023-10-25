
# 链表节点
class Node:
    def __init__(self, data = 0, next = None):
        self.data = data  # 数据域
        self.next = next  # 指针域


# 单向链表
class SingeLinkList:
    # 链表结构
    def __init__(self) -> None:
        self.head = None  # 头结点
        self._length = 0  # 长度

    # 判断链表是否为空
    def is_empty(self):
        return self.head == None

    # 链表长度
    def length(self):
        return self._length

    # 链表所有节点组成的列表
    def nodeslist(self):
        nodes_list = []
        node = self.head
        while node:
            nodes_list.append(node.data)
            node = node.next
        return nodes_list
    
    # 往链表头部添加节点
    def add_node(self, new_node):
        # 新节点指向头节点
        new_node.next = self.head
        # head指向新节点
        self.head = new_node
        # 长度加一
        self._length += 1

    # 往链表头部添加值为data的节点
    def add(self, data):
        # 新建节点
        new_node = Node(data)
        self.add_node(self, new_node)

    # 往链表尾部添加节点
    def append_node(self, new_node):
        # 头节点为空时直接添加
        if self._length == 0:
            self.head = new_node
        # 头节点不为空时遍历至最后一个节点添加
        else:
            last_node_next = self.head
            last_node = last_node_next
            while last_node_next:
                last_node = last_node_next
                last_node_next = last_node_next.next
            last_node.next = new_node
        # 长度加一
        self._length += 1
    
    # 往链表尾部添加值为data的节点
    def append(self, data):
        # 新建节点
        new_node = Node(data)
        self.append_node(new_node)

    # 往链表指定位置插入节点
    def insert(self, pos, new_node):
        pass

    # 删除第一个值为data的节点
    def remove(self, data):
        pass

    # 修改指定位置的节点的值
    def modify(self, pos, data):
        pass

    # 查找值为data的节点是否存在
    def search(self, data):
        pass



        

























