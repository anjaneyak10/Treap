import random
import time
import matplotlib.pyplot as plt

# Treap Class
# This class has the following attributes:
# key: The key of the node
# priority: The priority of the node
# parent: The parent of the node
# left: The left child of the node
# right: The right child of the node
# The class also has a __str__ method that returns a string representation of the node
class Treap:
    def __init__(self, key='', priority=-1,parent=None ,left=None, right=None):
        self.key=key
        self.priority = random.randint(0, 100)
        if priority==-1:
            self.priority = random.randint(0, 100)
        else:
            self.priority = priority
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        parent_key = self.parent.key if self.parent else "None"
        parent_priority = self.parent.priority if self.parent else "None"

        left_child_key = self.left.key if self.left else "None"
        left_child_priority = self.left.priority if self.left else "None"

        right_child_key = self.right.key if self.right else "None"
        right_child_priority = self.right.priority if self.right else "None"

        return (f"Key: {self.key}, Priority: {self.priority}, "
                f"Parent Key: {parent_key}, Parent Priority: {parent_priority}, "
                f"Left Child Key: {left_child_key}, Left Child Priority: {left_child_priority}, "
                f"Right Child Key: {right_child_key}, Right Child Priority: {right_child_priority}")
# left_rotate function
# This function accepts a node as an argument and performs a left rotation on the node
def left_rotate(tnode):
    if not tnode.right:
        tnode.right = tnode.parent
        tnode.right.left = None
    else:
        rightNode = tnode.right
        tnode.right = tnode.parent
        tnode.right.left = rightNode
        rightNode.parent = tnode.right
    tnode.parent = tnode.parent.parent
    tnode.right.parent = tnode

    if tnode.parent:
        if tnode.parent.left == tnode.right:
            tnode.parent.left = tnode
        else:
            tnode.parent.right = tnode
    return tnode


# right_rotate function
# This function accepts a node as an argument and performs a right rotation on the node
def right_rotate(tnode):
    if not tnode.left:
        tnode.left = tnode.parent
        tnode.left.right = None
    else:
        leftNode = tnode.left
        tnode.left = tnode.parent
        tnode.left.right = leftNode
        leftNode.parent = tnode.left
    tnode.parent = tnode.parent.parent
    tnode.left.parent = tnode
    if tnode.parent:
        if tnode.parent.left == tnode.left:
            tnode.parent.left = tnode
        else:
            tnode.parent.right = tnode
    return tnode
# insert function
# This function accepts the root node and a new node as arguments and inserts the new node into the tree
# The function returns the root node of the tree
def insert(root,newNode):
    key = newNode.key
    priority = newNode.priority
    if root is None:
        return Treap(key, priority)
    if key == root.key:
        return root
    traverse = root
    alreadyPresent = False
    while traverse:
        if key == traverse.key:
            alreadyPresent = True
            break
        if key<traverse.key:
            if not traverse.left:
                traverse.left = newNode
                traverse.left.parent = traverse
                traverse = traverse.left
                break
            traverse = traverse.left
        else:
            if not traverse.right:
                traverse.right = newNode
                traverse.right.parent = traverse
                traverse = traverse.right
                break
            traverse = traverse.right
    if alreadyPresent:
        while root.parent:
            root = root.parent
        return root
    while traverse.parent and traverse.priority> traverse.parent.priority:
        if traverse == traverse.parent.left:
            traverse=left_rotate(traverse)
        else:
            traverse=right_rotate(traverse)
    while root.parent:
        root = root.parent
    return root


# search function
# This function accepts the root node and a key as arguments and searches for the key in the tree
# The function returns True if the key is found and False otherwise
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root)
        in_order_traversal(root.right)


# visualize_tree function
# This function accepts the root node of a tree and generates a DOT representation of the tree
# The function prints the DOT representation to the console
def visualize_tree(root):
    dot = 'digraph tree {\nnode [shape=circle, fontname="Arial", fontsize=10];\n'

    def add_node(node, label):
        nonlocal dot
        dot += f'{node.key}{node.priority}[label="{label}"];\n'
        if not node.left and not node.right:
            return
        if not node.left:
            dot+=f'{node.key}{node.priority} -> {node.key}LNE;\n'
        for child in [node.left, node.right]:
            if child:
                dot += f'{node.key}{node.priority} -> {child.key}{child.priority};\n'
                add_node(child, "Key = "+child.key+" Priority ="+str(child.priority))
        if not node.right:
            dot+=f'{node.key}{node.priority} -> {node.key}RNE;\n'
    add_node(root, "Key = "+root.key+" Priority ="+str(root.priority))
    dot += '}\n'

    print(dot)



# question3 function
# This function creates a treap from the input list and performs an in-order traversal of the tree
def question3():
    treapInputList =['Z','Y','X','W','V','B','U','G','M','R','K','J','D','Q','E','C','S','I','H','P','L','A','N','O','T','F']
    root = None
    for i in treapInputList:
        root = insert(root, Treap(i))
    visualize_tree(root)
    return root

# searchInTextFile function
# This function reads the text file 'FellowshipOfTheRing.txt' and searches for the characters in the tree
def searchInTextFile(rootNode):
    with open('FellowshipOfTheRing.txt', 'r') as file:
        found=0
        notFound=0
        s = set()
        for line in file:
            for letter in line:
                if letter.isalpha():
                    if letter.islower():
                        letter = letter.upper()
                    search(rootNode, letter)


# This function calculates the time for searching the text file
def calculateTimeForSearch(root):
    times = []
    for i in range(10):
        start = time.time()
        searchInTextFile(root)
        end = time.time()
        times.append(end-start)
    print(f'Times: {times}')
    print(f'Average Time: {sum(times)/len(times)}')

# This function creates a tree with given priority
# Corresponds to q5
def createTreeWithGivenPriority():
    characters = ['A','B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U','V','W','X','Y','Z']
    priorities = [24,7,14,17,26,10,8,18,22,4,5,16,13,19,23,12,2,20,21,25,15,6,11,3,9,1]
    treapInputList =['Z','Y','X','W','V','B','U','G','M','R','K','J','D','Q','E','C','S','I','H','P','L','A','N','O','T','F']
    map = {}
    for i in range(len(characters)):
        map[characters[i]] = priorities[i]
    root = None
    for i in treapInputList:
        root = insert(root, Treap(i, map[i]))
    visualize_tree(root)
    return root


# This function creates a tree with same priority
# Corresponds to q6
def createTreeWithSamePriority():
    characters =['Z','Y','X','W','V','B','U','G','M','R','K','J','D','Q','E','C','S','I','H','P','L','A','N','O','T','F']
    root = None
    for i in range(len(characters)):
        root = insert(root, Treap(characters[i],1))
    visualize_tree(root)
    return root

# main function
# This function creates a treap and inserts nodes into it
def main():
    # Verifying the values
    root = question3()
    # in_order_traversal(root)

    # Calculating the time for searching the text file Q4
    calculateTimeForSearch(root)

    print()
    print("Creating a tree with given priority and calculting the time for searching the text file")
    root = createTreeWithGivenPriority()
    calculateTimeForSearch(root)


    print()
    print("Creating a tree with same priority and calculting the time for searching the text file")
    root = createTreeWithSamePriority()
    calculateTimeForSearch(root)


main()





