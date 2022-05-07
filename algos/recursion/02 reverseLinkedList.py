# ============= Help Functions ===============
class Node:
  def __init__(self, val = None, next=None):
    self.val = val
    self.next = next

def LinkedList(mylist):
    head = Node(-1, None)
    p = head
    for i in mylist:
        p.next = Node(i, None)
        p = p.next
    return head.next

def traverseLinkedList(head):
    while head:
        print(head.val, end=", ")
        head = head.next

# ============== Solution ====================

linked_list = LinkedList([1,2,3,4,5])

def reverseList(head):

    if not head or not head.next:
        return head

    next_p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return next_p

traverseLinkedList(reverseList(linked_list))
