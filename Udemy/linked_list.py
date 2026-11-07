class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head

        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp

ll = LinkedList(1)
ll.append(2)
ll.append(3)
print(ll.pop_first().value)
print(ll.pop_first().value)
print(ll.pop_first().value)
print(ll.head)
print(ll.tail)
print(ll.length)