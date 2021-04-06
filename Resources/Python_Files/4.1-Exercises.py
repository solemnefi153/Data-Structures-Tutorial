import copy


class Stack():
    def __init__(self, data=[]):
        self.data = data

    def empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)

    def top(self):
        return self.data[-1]

    def push(self, newElement):
        self.data.append(newElement)

    def pop(self):
        return self.data.pop()

        

class StackOfActins:
    def __init__(self):
        #Notice that the stack is implemented with a list
        #You should only access the end of the list 
        self.actionStack = Stack()

    def addAction(self, newTask):
        """
        This function should add an action to the stack
        """
        pass
        
    def undo(self):
        """
        This function should take the action at the top of the stack,
        print it and remove it from the stack
        """
        pass
      
    def checkLastTask(self):
        """
        This function should print the the last task that was performed by the user
        """
        pass

    def viewAllTasks(self):
        """
        This function prints all the tasks in the stack 
        from last to first without changing the original order  the stack
        """
        pass

    def clearStack(self):
        """
        Clears all the tasks in the deck
        """
        pass


    def isStackOfActinsEmtpy(self):
        """
        Returns whather the deck is already empty
        """
        pass

    def getNumberOfTasks(self):
        """
        Returns the number of tasks in the stack
        """
        pass


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