class StackArray:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

# Example usage:
stack_array = StackArray(5)
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)
print("Top element:", stack_array.peek())
print("Popped element:", stack_array.pop())
print("Top element after pop:", stack_array.peek())
