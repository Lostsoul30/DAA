class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

# Example usage:
stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)
print("Top element:", stack_linked_list.peek())
print("Popped element:", stack_linked_list.pop())
print("Top element after pop:", stack_linked_list.peek())

