class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return '\0'  # Return null character for an empty stack
        else:
            popped_element = self.top.data
            print("Popped element is:", popped_element)
            print("----------------")
            self.top = self.top.next
            return popped_element

    def display(self):
        if self.top is None:
            print("Stack is Empty")
            print("------------------")
        else:
            print("Elements of the stack are:")
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is:", self.top.data)
            print("------------------")

def is_palindrome(sentence):
    sentence = sentence.lower()
    sentence = ''.join([ch for ch in sentence if ch.isalpha()])  # Remove non-alphabetic characters
    stack = Stack()

    for ch in sentence:
        stack.push(ch)

    reversed_sentence = ''
    while stack.top is not None:
        reversed_sentence += stack.pop()

    return sentence == reversed_sentence


if __name__ == "__main__":
    s = Stack()

    while True:
        print("Enter the option below")
        print("1 - Check Palindrome\n2 - Display\n3 - Exit")
        option = int(input())

        if option == 1:
            print("Enter a sentence to check if it's a palindrome:")
            user_input = input()
            if is_palindrome(user_input):
                print("The sentence is a palindrome!")
            else:
                print("The sentence is not a palindrome.")
        elif option == 2:
            print("Display")
            print("----------")
            s.display()
        else:
            break
