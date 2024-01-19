class StackArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

# Example Usage:
stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)

print("Stack using Array:", stack_array.items)
print("Pop item from Stack:", stack_array.pop())
print("Peek at the top of Stack:", stack_array.peek())
print("Stack size:", stack_array.size())
