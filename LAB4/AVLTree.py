class AVLNode(object): 
    def __init__(self, word, key, left = None, parent = None, right = None): 
        self.word = word #extra attribute needed to run the program 
        self.key = 0
        self.left = None
        self.parent = None
        self.right = None
        self.height = -1
        
class AVLTree(object): 

    def __init__(self, root = None): 
        self.root = None     

    def avlTree_insert(self, words, key): 
        node = AVLNode(words, key)
        node.key = key
        if (self.root == None): 
            self.root = node
            node.parent = None 
            return 
        cur = self.root 
        while (cur != None): 
            if (node.key < cur.key): 
                if (cur.left == None): 
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if (cur.right == None): 
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        node = node.parent
        while (node != None): 
            self.avlTree_rebalance(node)
            node = node.parent

    def avlTree_setChild(self, parent, which_child, child): 
            if (which_child != "left" and which_child != "right"):
                return False
            if (which_child == "left"):
                parent.left = child
            else:
                parent.right = child
            if (child != None):
                child.parent = parent
            self.avlTree_updateHeight(parent)
            return True
    
    def avlTree_replaceChild(self, parent, curr_child, new_child): 
        if (parent.left == curr_child):
            return self.avlTree_setChild(parent, "left", new_child)
        elif (parent.right == curr_child):
            return self.avlTree_setChild(parent, "right", new_child)
        return False

    def avlTree_updateHeight(self, node): 
        leftHeight = -1
        if (node.left != None):
            leftHeight = node.left.height 
        rightHeight = -1
        if (node.right != None):
            rightHeight = node.right.height
        node.height = max(leftHeight, rightHeight) + 1    
        
    def avlTree_getBalance(self, node): 
        leftHeight = -1
        if (node.left != None):
            leftHeight = node.left.height
        rightHeight = -1
        if (node.right != None):
            rightHeight = node.right.height
        return leftHeight - rightHeight
    
    def avlTree_rotateRight(self, node): 
        left_right_child = node.left.right
        if (node.parent != None):
            self.avlTree_replaceChild(node.parent, node, node.left)
        else: # node is root
            self.root = node.left
            self.root.parent = None
    
        self.avlTree_setChild(node.left, "right", node)
        self.avlTree_setChild(node, "left", left_right_child)

    def avlTree_rotateLeft(self, node): 
        right_left_child = node.right.left
        if (node.parent != None):
            self.avlTree_replaceChild(node.parent, node, node.right)
        else: 
            self.root = node.right
            self.root.parent = None
        self.avlTree_setChild(node.right, "left", node)
        self.avlTree_setChild(node, "right", right_left_child)
        
    def avlTree_rebalance(self, node): 
        self.avlTree_updateHeight(node)        
        if (self.avlTree_getBalance(node) == -2): 
            if (self.avlTree_getBalance(node.right) == 1): 
                self.avlTree_rotateRight(node.right)
            return self.avlTree_rotateLeft(node)
        elif (self.avlTree_getBalance(node) == 2): 
            if (self.avlTree_getBalance(node.left) == -1):  
                self.avlTree_rotateLeft(node.left)
            return self.avlTree_rotateRight(node)
        return node
    
