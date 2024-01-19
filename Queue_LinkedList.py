class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

# Example usage:
queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)
print("Dequeued element:", queue_linked_list.dequeue())
print("Front element after dequeue:", queue_linked_list.front.data)
