def sum_of_numbers(nums):
    sum = 0

    for num in nums:
        sum = sum + num
    
    return sum

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if self.head is None:
            return "playlist is empty"

        #if head.data equals data:
        if self.head.data == data:
            #move head to head.next and stop
            self.head = self.head.next

        #otherwise:
        else:
            #start current at head
            current = self.head

            #while current.next exists AND current.next.data != data:
            while current.next is not None and current.next.data != data:
                #move current forward
                current = current.next

            #if current.next is None: report "song not found"
            if current.next is None:
                return "song not found"
            #else: bypass it — current.next = current.next.next
            else:
                current.next = current.next.next
    
    def find(self, data):
        #start current at head
        current = self.head

        #while current exists:
        while current is not None:
            #if current.data equals data: return True
            if current.data == data:
                return True
            #move current forward
            current = current.next
        #return False
        return False
    
if __name__ == "__main__":
    def menu_loop():
        #show: 1-add song 2-remove song 3-find song
        #4-add to front 5-show playlist 6-quit
        playlist = LinkedList()
        quit = False

        while quit is not True:
            user_input = input("""
            1: Add Song
            2: Remove Song
            3: Find Song
            4: Add to front
            5: Show playlist
            6: Quit
            """)

            #read the choice with input()
            if user_input == "1":
                song_to_add = input("Enter song to add: ")
                playlist.append(song_to_add)
            elif user_input == "2":
                song_to_delete = input("Enter song to delete: ")
                playlist.delete(song_to_delete)
            elif user_input == "3":
                song_to_find = input("Enter song to find: ")
                print(playlist.find(song_to_find))
            elif user_input == "4":
                song_to_add_to_front = input("Enter song to add to the front: ")
                playlist.prepend(song_to_add_to_front)
            elif user_input == "5":
                playlist.display()
            elif user_input == "6":
                quit = True
            else:
                print("Invalid choice, please try again")

        #call the matching method and show what happened
    menu_loop()