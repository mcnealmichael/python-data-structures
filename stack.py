class Stack:
    def __init__(self, items=None):
        # Best practice: Default to None to avoid shared mutable state
        if items is None:
            self.items = []
        else:
            self.items = list(items) # Creates a copy so external changes don't affect the stack
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Stack()
    string = "{["
    pairs = {"}":"{", "]":"[", ")":"("}
    is_successful = True

    for char in string:
        if char in "([{":
            s.push(char)

        if char in "}])":
            if s.is_empty():
                print("There are no opening brackets")
                is_successful = False
                break

            if pairs.get(char) == s.peek():
                s.pop()
            else:
                print("Brackets are out of order")
                is_successful = False
                break

    if is_successful and s.is_empty():
        print("All Matched")
    elif not s.is_empty():
        print("There are no closing brackets")