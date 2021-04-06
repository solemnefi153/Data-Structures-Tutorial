class Node():
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.numOfElements = 0
        self.head = None
        self.tail = None
    
    def empty(self):
        pass

    def push_back(self, newValue):
        pass

    def pop_back(self):
        pass

    def size(self):
        pass

    def copy(self):
        newLinkedList = LinkedList()
        currentCopiedNode = self.tail
        while currentCopiedNode != None:
            newLinkedList.push_back(currentCopiedNode.value)
            currentCopiedNode = currentCopiedNode.next
        return newLinkedList
        


class Stack():
    def __init__(self , data = LinkedList()):
        self.data = data

    def empty(self):
        pass
    
    def size(self):
        pass

    def top(self):
        pass

    def push(self, newElement):
        self.data.push_back(newElement)

    def pop(self):
        return self.data.pop_back()

    def copy(self):
        return  Stack(self.data.copy())

        

    

class StackOfActins:
    def __init__(self):
        #Notice that the stack is implemented with a list
        #You should only access the end of the list 
        self.actionStack = Stack()

    def addAction(self, newTask):
        """
        This function should add an action to the stack
        """
        self.actionStack.push(newTask)
        
    def undo(self):
        """
        This function should take the action at the top of the stack,
        print it and remove it from the stack
        """
        lastTask = self.actionStack.pop()
        print("Task undone: " + str(lastTask))
      
    def checkLastTask(self):
        """
        This function should print the the last task that was performed by the user
        """
        lastTask = self.actionStack.top()
        print("Last Task: " + str(lastTask))

    def viewAllTasks(self):
        """
        This function prints all the tasks in the stack 
        from last to first without changing the original order  the stack
        """
        stack2 = self.actionStack.copy()
        while not stack2.empty():
            print(stack2.pop())

    def clearStack(self):
        """
        Clears all the tasks in the deck
        """
        while not self.actionStack.empty():
            self.actionStack.pop()


    def isStackOfActinsEmtpy(self):
        """
        Returns whather the deck is already empty
        """
        return self.actionStack.empty()

    def getNumberOfTasks(self):
        """
        Returns the number of tasks in the stack
        """
        return self.actionStack.size()


# Test 1
print("\n=========== TESTS 1 ===========")
actionsStack = StackOfActins()
actionsStack.addAction('Type: Hello world')
actionsStack.addAction('Type: How are you?')
actionsStack.addAction('Erase: How are you?')
actionsStack.addAction('Type: You are awesome')
print(actionsStack.getNumberOfTasks()) # 4

# Test 2
print("\n=========== TESTS 2 ===========")
actionsStack.undo() # Task undone: Type: You are awesome
actionsStack.undo() # Task undone: Erase: How are you?
print(actionsStack.getNumberOfTasks()) # 2


# Test 3
print("\n=========== TESTS 3 ===========")
actionsStack.addAction('Add Image: /users/thebest/image1.jpg')
actionsStack.addAction('Change text: Type: How are you? -> How are they?')
actionsStack.checkLastTask() #Last Task: Change text: Type: How are you? -> How are they?

# Test 4
print("\n=========== TESTS 4 ===========")
actionsStack.viewAllTasks() 
# Change text: Type: How are you? -> How are they?
# Add Image: /users/thebest/image1.jpg
# Type: How are you?
# Type: Hello world


# Test 5
print("\n=========== TESTS 5 ===========")
actionsStack.clearStack()
print(actionsStack.isStackOfActinsEmtpy()) # True
actionsStack.viewAllTasks() # Should not print 




