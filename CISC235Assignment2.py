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

def stackMain():
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

    print()#for formatting

    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    print("Top element is", stack.top())
    print("Size of stack:", stack.size())
    print("stack.isEmpty():", stack.isEmpty())


#stackMain()


#nodes for the queue
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#a queue to allow for level order traversal of the binary search tree
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.isEmpty():
            self.head = Node(data)
            self.tail = self.head
        else:
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return None

        if self.head.next is None:
            temp = self.head
            self.head = None
            return temp

        temp = self.head
        self.head = self.head.next
        return temp

    def isEmpty(self):
        return self.head is None


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.numDuplicates = 0

    def insert(self, data):
        if self.data == data:
            self.numDuplicates += 1
            return

        if data < self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.insert(data)

    def searchPath(self, target):
        result = []
        current = self
        while current is not None:
            result.append(current.data)
            if current.data == target:
                return result

            if current.left is None and current.right is None:
                return "Value not found in tree"

            if target < current.data:
                current = current.left
            elif target > current.data:
                current = current.right

        return result

    def getTotalDepth(self, currentDepth=0):
        if self.left is None and self.right is None:
            return currentDepth
        if self.left is None:
            return currentDepth + self.right.getTotalDepth(currentDepth+1)
        if self.right is None:
            return self.left.getTotalDepth(currentDepth+1)
        return currentDepth + self.left.getTotalDepth(currentDepth+1) + self.right.getTotalDepth(currentDepth+1)

    def getWeightBalanceFactor(self):
        if self.left is None and self.right is None:
            return 0
        if self.left is None:
            return 1 + self.right.getWeightBalanceFactor()
        if self.right is None:
            return -1 + self.left.getWeightBalanceFactor()
        return self.left.getWeightBalanceFactor() + self.right.getWeightBalanceFactor()

    def loadTreeFromFile(self, fileName):
        return

    def __str__(self):
        return str(self.data)

    def display(self):
        queue = Queue()
        queue.enqueue(self)
        while not queue.isEmpty():
            current = queue.dequeue()
            print(str(current.data), end=" ")

            if current.data.left is not None:
                queue.enqueue(current.data.left)

            if current.data.right is not None:
                queue.enqueue(current.data.right)

        print()


def binarySearchTreeMain():
    tree = BSTNode(6)
    tree.insert(4)
    tree.insert(9)
    tree.insert(5)
    tree.insert(8)
    tree.insert(7)
    print(tree.searchPath(7))

    print("Total depth:", tree.getTotalDepth())
    print("Weight balance factor:", tree.getWeightBalanceFactor())

    tree.display()


binarySearchTreeMain()
