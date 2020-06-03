class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # ------------------------------    Insert into BST   -------------------------------------
    # Complexity is Worst Case O(n) as it may compare up to n nodes to correctly insert the Node in order
    def insertNode(self, data):
        # Prevent Duplicates
        if self.data == data:
            print(data, ' -  Thats a duplicate data entry' )
            return False        

        #If data < Root Node then place in left subtree
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insertNode(data)
            else:
                self.leftChild = TreeNode(data)
                return True

        # Else place in right subtree
        else:
            if self.rightChild:
                return self.rightChild.insertNode(data)
            else:
                self.rightChild = TreeNode(data)
                return True

    # -----------------------------    Delete from BST   ---------------------------------------
    # Complexity is Worst Case O(n) as it may need to search through n nodes to find the data to delete
    def minValueNode(self, node):
        current = node

        # Loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def deleteNode(self, data):
        if self is None:
            return None

        # if current node < root node, then search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.deleteNode(data)
        elif data > self.data:
            self.rightChild = self.rightChild.deleteNode(data)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.deleteNode(temp.data)

        return self

    # -------------------------------    Search BST   --------------------------------------
    # Complexity is Worst Case O(n) because it may have to search through n nodes to find the data
    
    def searchBST(self, data):
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.searchBST(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.searchBST(data)
            else:
                return False

    # --------------------------    Traversal Activities     ---------------------------------
    
    # All in-order/pre-order and post-order traversals are worst case O(n) as they are Depth-First Traversals
    # and the maximum number of edges to each node in a Binary Tree is 2
    
    def preorder(self):
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

    

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insertNode(data)
        else:
            self.root = TreeNode(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.deleteNode(data)

    def find(self, data):
        if self.root:
            return self.root.searchBST(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
            
            
            
# Testing Area
myTree = Tree()

# Initialising and Inserting into Tree

myTree.insert(25)
myTree.insert(36)
myTree.insert(20)
myTree.insert(10)
myTree.insert(22)
myTree.insert(30)
myTree.insert(40)
myTree.insert(5)
myTree.insert(12)
myTree.insert(28)
myTree.insert(38)
myTree.insert(48)
myTree.insert(1)
myTree.insert(8)
myTree.insert(15)
myTree.insert(45)
myTree.insert(50)

# Attempting a duplicate data insert
myTree.insert(45)

# Traversals

# Preorder
myTree.preorder()
    
# In Order
myTree.inorder()

# Post Order
myTree.postorder()

# Deleting a Node
myTree.delete(1)
print('\n\n Is 1 still in the tree?')
# Finding a Node
print(myTree.find(1))


