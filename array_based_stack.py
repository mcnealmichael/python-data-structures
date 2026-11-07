class ArrayBasedStack:
    def __init__(self, optional_max_length = None):
        self.stack_list = []
        self.max_length = optional_max_length
        self.top = -1

    def pop(self):
        if self.top == -1:
            return
        self.top -= 1
        return self.stack_list.pop()

    def peek(self):
        if self.top == -1:
            return
        return self.stack_list[self.top]

    def push(self, item):
        if len(self.stack_list) == self.max_length:
            return False
        self.top += 1
        self.stack_list.append(item)
        return True

    def print_stack(self):
        for i in range(self.top, -1, -1):
            print(self.stack_list[i])

array_stack = ArrayBasedStack()
array_stack.push(1)
array_stack.push(2)
array_stack.push(3)
array_stack.print_stack()
array_stack.pop()
array_stack.print_stack()
array_stack.pop()
array_stack.print_stack()
array_stack.pop()
array_stack.print_stack()
array_stack.push(5)
array_stack.print_stack()
print(array_stack.peek())
array_stack.push(7)
print(array_stack.peek())
array_stack.print_stack()