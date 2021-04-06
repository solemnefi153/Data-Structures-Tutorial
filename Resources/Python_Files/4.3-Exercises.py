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
        pass

    def find(self, value):
        pass

        


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




