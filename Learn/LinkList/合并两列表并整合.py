from LinkList import *

def strlis2linklist(strlist):
    linklist = SingeLinkList()
    for i in strlist:
        linklist.append(eval(i))
    return linklist

def SLLmerge(l1, l2):
    l1_node = l1.head
    l2_node = l2.head
    l3 = SingeLinkList()
    while l1_node and l2_node:
        l1_node_next = l1_node.next
        l1_node.next = None
        l2_node_next = l2_node.next
        l2_node.next = None
        if l1_node.data < l2_node.data:
            l3.append_node(l1_node)
            l1_node = l1_node_next
            l2_node.next = l2_node_next
        elif l1_node.data > l2_node.data:
            l3.append_node(l2_node)
            l2_node = l2_node_next
            l1_node.next = l1_node_next
        else:
            l3.append_node(l1_node)
            l1_node = l1_node_next
            l2_node = l2_node_next
    if l1_node:
        l3.append_node(l1_node)
    elif l2_node:
        l3.append_node(l2_node)
    
    return l3

ll1 = strlis2linklist(input("输入list1: ").split())
ll2 = strlis2linklist(input("输入list2: ").split())

# ll1 = strlis2linklist(['1', '2', '3'])
# ll2 = strlis2linklist(['2', '3', '4'])

ll3 = SLLmerge(ll1, ll2)
print(ll3.nodeslist())

















