class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        return self.top

    def pop(self):
        if self.top is None:
            return
        temp = self.top
        self.top =self.top.next
        temp.next = None
        return temp

    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()
stack.pop()
stack.print_stack()
print(stack.peek().value)
stack.pop()
stack.print_stack()
stack.pop()
stack.print_stack()
stack.pop()