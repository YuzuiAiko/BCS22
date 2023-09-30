class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


input_values = [6, 3, 4, 2, 1]
my_linked_list = LinkedList()

for value in input_values:
    my_linked_list.insert(value)

print("Original Linked List:")
my_linked_list.display()


my_linked_list.swap_nodes(3, 4)

print("\nLinked List after Swapping 3 and 4:")
my_linked_list.display()
