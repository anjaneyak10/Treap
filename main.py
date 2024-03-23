import random
import time

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

# in_order_traversal function
# This function accepts the root node as an argument and prints the keys and priorities in an in-order traversal of the tree
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root)
        in_order_traversal(root.right)

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

# x = insert(None, Treap('a'))
# a= insert(x, Treap('b'))
# z = insert(a, Treap('c'))
# y = insert(z, Treap('d'))
# in_order_traversal(y)
# print(search(y, 'a'))
# print(search(y, 'e'))

# question3 function
# This function creates a treap from the input list and performs an in-order traversal of the tree
def question3():
    treapInputList =['Z','Y','X','W','V','B','U','G','M','R','K','J','D','Q','E','C','S','I','H','P','L','A','N','O','T','F']
    root = None
    for i in treapInputList:
        root = insert(root, Treap(i))
    in_order_traversal(root)
    return root


def question4(rootNode):
    with open('FellowshipOfTheRing.txt', 'r') as file:
        found=0
        notFound=0
        s = set()
        for line in file:
            for letter in line:
                if letter.isalpha():
                    if letter.islower():
                        letter = letter.upper()
                    if not search(rootNode, letter):
                        notFound+=1
                        s.add(letter)
                    else:
                        found+=1



times = []
for i in range(10):
    root = question3()
    start = time.time()
    question4(root)
    end = time.time()
    times.append(end-start)
print(f'Times: {times}', f'Average Time: {sum(times)/len(times)}')
