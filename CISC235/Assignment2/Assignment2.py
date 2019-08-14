'''
Written by: Sam McPhail
Student Number: 20051336
'''


class Stack:

    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.isEmpty():
            return None

        return self.data.pop(-1)

    def top(self):
        if self.isEmpty():
            return None

        return self.data[-1]

    def size(self):
        return len(self.data)

    def __str__(self):
        if self.isEmpty():
            return "The stack is empty"

        result = ""
        for i in range(len(self.data)):
            result = str(self.data[i]) + "\n" + result
        return "\n" + result


#a subclass of a binary search tree to allow each node to be more easily controlled
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.numDuplicates = 1 #if multiple of the same value are added, just increment this instead of inserting a new node

    def __str__(self):
        return str(self.data) + "(" + str(self.numDuplicates) + ") "

    #helper function to get a nodes weight balance factor
    #count the number of immediate children and recursively add it to its childrens children
    def getNumChildren(self):
        if self.left is None and self.right is None:
            return 0

        if self.left is None:
            return 1 + self.right.getNumChildren()

        if self.right is None:
            return 1 + self.left.getNumChildren()

        return 2 + self.left.getNumChildren() + self.right.getNumChildren()

    #helper function to determine a trees weight balance factor
    #add 1 to the number of children to count the node's immediate children (ie self.left)
    def getOwnWeightBalanceFactor(self):
        return abs((1 + self.left.getNumChildren()) - (1 + self.right.getNumChildren()))


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    #3 cases, there is no root, the value being inserted already exists, the value is new
    def insert(self, node, root=""):
        if self.root is None:
            self.root = node
            return

        #special case for the first call of the function (called on the entire tree, not a subtree)
        if root == "":
            root = self.root

        #the value being added already exists
        if root.data == node.data:
            root.numDuplicates += 1
            return

        #if at a leaf/node with only 1 child and the new node is correctly less than or greater than,
        #make the new node a child of the current node
        #else recursively call insert on the current node's children
        if node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                self.insert(node, root.left)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(node, root.right)

    #traverse through the tree following the same algorithm as a binary search, adding every node passed
    #to a list
    #return the list when the value is found, or we are at a leaf node
    def searchPath(self, target):
        result = []
        current = self.root
        while current is not None:
            result.append(current.data)
            if current.data == target or (current.left is None and current.right is None):
                return result

            if target < current.data:
                current = current.left
            else:
                current = current.right

        return result

    #emulate "tail recursion" by keeping the current nodes depth as a parameter
    #and incrementing it when recursively calling on a child
    def getTotalDepth(self, root="", currentDepth=0):
        if root == "":#case for the first call of the function (called on the entire tree, not a subtree)
            root = self.root
        if root.left is None and root.right is None:
            return currentDepth
        if root.left is None:
            return currentDepth + self.getTotalDepth(root.right, currentDepth + 1)
        if root.right is None:
            return currentDepth + self.getTotalDepth(root.left, currentDepth + 1)

        return currentDepth + self.getTotalDepth(root.left, currentDepth + 1) + self.getTotalDepth(root.right, currentDepth + 1)

    #a nodes weight balance factor is the absolute value of its left nodes-right nodes
    #weight balance factor of a tree the weight balance factor of the node with the greatest factor in the tree
    #recursively keep the max of a nodes factor and its children's factor until reaching a leaf node
    def getWeightBalanceFactor(self, root=""):
        if root == "":#case for the first call of the function (called on the entire tree, not a subtree)
            root = self.root
        if root.left is None and root.right is None:
            return 0
        if root.left is None:
            return 1+root.right.getNumChildren()
        if root.right is None:
            return 1+root.left.getNumChildren()

        return max(self.getWeightBalanceFactor(root.left), root.getOwnWeightBalanceFactor(), self.getWeightBalanceFactor(root.right))

    #iterate through each line in the file until no lines left
    #if the line has a right child pop the top of the stack and save the pop as the right tree
    #if the line has a left child pop the top of the stack and save the pop as the left tree
    #make a tree from the line's data and the saved right and left tree
    #push the tree to the stack
    #when the loop is complete, return the one element left in the stack
    def loadTreeFromFile(self, fileName):
        inFile = open(fileName, "r")
        if inFile is None:
            return

        stack = Stack()
        inLine = inFile.readline()
        while inLine != "":
            leftTree = None
            rightTree = None
            data = inLine.split()
            if int(data[2]) == 1:
                rightTree = stack.pop()
            if int(data[1]) == 1:
                leftTree = stack.pop()

            tree = BinarySearchTree(Node(int(data[0])))
            if leftTree is not None:
                tree.insert(leftTree.root)
            if rightTree is not None:
                tree.insert(rightTree.root)

            stack.push(tree)
            inLine = inFile.readline()

        inFile.close()
        return stack.pop()

    def __str__(self):
        return self.inOrderTraversal(self.root)

    #to allow the tree to be printed visually
    def inOrderTraversal(self, root):
        result = ""
        if root is not None:
            result = self.inOrderTraversal(root.left)
            result += str(root)
            result += self.inOrderTraversal(root.right)
        return result

#test code
def main():

    tree = BinarySearchTree()
    tree = tree.loadTreeFromFile("binarySearchTree.txt")
    print("Loading the tree from the text file...")
    print("The tree:", end=" ")
    print(tree)
    print("Total depth:", tree.getTotalDepth())
    print("Weight balance factor:", tree.getWeightBalanceFactor(), "\n")

    print("Inserting a new node")
    tree.insert(Node(5))
    print("The updated tree:", end=" ")
    print(tree, "\n")

    print("Searching for 5...")
    print("The search path for 5:", end=" ")
    print(tree.searchPath(5))

    print("Total depth:", tree.getTotalDepth())
    print("Weight balance factor:", tree.getWeightBalanceFactor())


main()
