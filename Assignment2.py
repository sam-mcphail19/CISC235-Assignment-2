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


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.numDuplicates = 1

    def __str__(self):
        return str(self.data) + "(" + str(self.numDuplicates) + ") "

    def getNumChildren(self):
        if self.left is None and self.right is None:
            return 0

        if self.left is None:
            return 1 + self.right.getNumChildren()

        if self.right is None:
            return 1 + self.left.getNumChildren()

        return 2 + self.left.getNumChildren() + self.right.getNumChildren()

    def getOwnWeightBalanceFactor(self):
        return abs((1 + self.left.getNumChildren()) - (1 + self.right.getNumChildren()))


class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def insert(self, node, root=""):
        if root == "":
            root = self.root

        if root.data == node.data:
            root.numDuplicates += 1
            return

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

    def searchPath(self, target):
        result = []
        current = self.root
        while current is not None:
            result.append(current.data)
            if current.data == target:
                return result

            if current.left is None and current.right is None:
                return "Value not found in tree"

            if target < current.data:
                current = current.left
            else:
                current = current.right

        return result

    def getTotalDepth(self, root, currentDepth=0):
        if root.left is None and root.right is None:
            return currentDepth
        if root.left is None:
            return currentDepth + self.getTotalDepth(root.right, currentDepth + 1)
        if root.right is None:
            return self.getTotalDepth(root.left, currentDepth + 1)

        return currentDepth + self.getTotalDepth(root.left, currentDepth + 1) + self.getTotalDepth(root.right, currentDepth + 1)

    def getWeightBalanceFactor(self, root):
        if root.left is None and root.right is None:
            return 0
        if root.left is None:
            return 1+root.right.getNumChildren()
        if root.right is None:
            return 1+root.left.getNumChildren()

        return max(self.getWeightBalanceFactor(root.left), root.getOwnWeightBalanceFactor(), self.getWeightBalanceFactor(root.right))

    def loadTreeFromFile(self, fileName):
        inFile = open(fileName, "r")
        if inFile is None:
            return

        stack = Stack()
        inLine = inFile.readline()
        left_tree = None
        right_tree = None
        while inLine != "":
            data = inLine.split()
            if int(data[2]) == 1:
                right_tree = stack.pop()
            if int(data[1]) == 1:
                left_tree = stack.pop()

            tree = BinarySearchTree(Node(int(data[0])))
            if left_tree is not None:
                tree.insert(left_tree.root)
            if right_tree is not None:
                tree.insert(right_tree.root)

            stack.push(tree)
            inLine = inFile.readline()

        inFile.close()
        return stack.pop()

    def __str__(self):
        return self.inOrderTraversal(self.root)

    def inOrderTraversal(self, root):
        result = ""
        if root is not None:
            result = self.inOrderTraversal(root.left)
            result += str(root)
            result += self.inOrderTraversal(root.right)
        return result


def main():
    stack = Stack()

    stack.push(5)
    stack.push(2)
    stack.push(4)
    print(stack)
    print("Top element is", stack.top())
    print("Size of stack:", stack.size())
    print("stack.isEmpty():", stack.isEmpty())

    stack.pop()
    print(stack)
    print("Top element is", stack.top())
    print("Size of stack:", stack.size())
    print("stack.isEmpty():", stack.isEmpty())

    stack.push(12)
    print(stack)
    print("Top element is", stack.top())
    print("Size of stack:", stack.size())
    print("stack.isEmpty():", stack.isEmpty())

    print()  # for formatting

    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    print("Top element is", stack.top())
    print("Size of stack:", stack.size())
    print("stack.isEmpty():", stack.isEmpty())

    print("\n")

    tree = BinarySearchTree(Node(8))
    tree.insert(Node(4))
    tree.insert(Node(9))
    tree.insert(Node(2))
    tree.insert(Node(7))
    tree.insert(Node(10))
    print(tree.searchPath(7))
    print(tree)

    print("Total depth:", tree.getTotalDepth(tree.root))
    print("Weight balance factor:", tree.getWeightBalanceFactor(tree.root))

    print()

    fileTree = tree.loadTreeFromFile("binarySearchTree.txt")
    print("Loading the tree from the text file...")
    print(fileTree)


main()
