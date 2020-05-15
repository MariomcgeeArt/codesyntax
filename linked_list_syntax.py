

#This is the coding syntax with my corrections made in google doc
#code does not run 


from linkedlist import LinkedList

class Stack(LinkedList):
    def _init_(self):
        self.head = None;

    def push(self,new_item):
        """Insert the given item on top of this stack"""
        # prepend given item before head node
        self.prepend(new_item)


    def peek(self):
        """Return the item on the top of this stack"""
        if self.is_empty():
            return None
        else:
            return self.head.data

    def pop(self, item):
        """Remove and return the item on the top of this stack"""
        item = self.peek()
        self.delete(item)
        return item


# if __name__ == '__main__':
new_stack = Stack()

new_stack.push(33)
new_stack.push(22)
new_stack.push(44)


top = new_stack.peek()
# Print top element of stack
print("Top element is {}.".format(top))

# # Delete top elements of stack
new_stack.pop(66)
new_stack.pop(99)

top = new_stack.peek()
# # Print top element of stack
print("Top element is {}.".format(top))


#recieved Help from Anastasia G on links to code site for code linters aswell as personal revision 