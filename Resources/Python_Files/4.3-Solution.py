class Node():
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

class BST():
    def __init__(self):
        self.numOfElements = 0
        self.root = None

    def insert(self, newValue):
        newNode = Node(newValue)
        if(self.root == None):
            self.root = newNode
            self.numOfElements = self.numOfElements + 1
            return
        currentVisitedNode = self.root
        while currentVisitedNode != None: 
            if (currentVisitedNode.value <= newValue ):
                if (currentVisitedNode.right_child == None):
                    newNode.parent = currentVisitedNode
                    currentVisitedNode.right_child = newNode
                    self.numOfElements = self.numOfElements + 1
                    return
                else:
                    currentVisitedNode = currentVisitedNode.right_child
            else:
                if(currentVisitedNode.left_child == None):
                    newNode.parent = currentVisitedNode
                    currentVisitedNode.left_child = newNode
                    self.numOfElements = self.numOfElements + 1
                    return
                else:
                    currentVisitedNode = currentVisitedNode.left_child

    def find(self, value):
        currentVisitedNode = self.root
        while currentVisitedNode != None:
            if(currentVisitedNode.value == value):
                return True
            if(currentVisitedNode.value <= value):
                currentVisitedNode = currentVisitedNode.right_child
            else:
                currentVisitedNode = currentVisitedNode.left_child
        return False


        


# Test 1
print("\n=========== TESTS 1 ===========")
sortedNumbers = BST()
sortedNumbers.insert(1)
sortedNumbers.insert(2)
sortedNumbers.insert(3)
sortedNumbers.insert(4)
print(sortedNumbers.numOfElements) # 4

# Test 2
print("\n=========== TESTS 2 ===========")
print(sortedNumbers.find(5)) # False
print(sortedNumbers.find(3)) # True




