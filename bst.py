class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def add(self, key, value):
        if self.key == key:
            return False       

        elif key < self.key:
           if self.leftChild:
               return self.leftChild.add(key, value)
           else: 
                self.leftChild = Node(key, value)
                self.leftChild.parent = self
                return True    
        
        elif key > self.key:
           if self.rightChild:
               return self.rightChild.add(key, value)
           else:
                self.rightChild = Node(key, value)     
                self.rightChild.parent = self
                return True

    def preorder(self, pre_list):
        pre_list.append(self.key)
        if self.leftChild:
            self.leftChild.preorder(pre_list)
        if self.rightChild:
            self.rightChild.preorder(pre_list)
        return pre_list

    def postorder(self, post_list):
        if self.leftChild:
            self.leftChild.postorder(post_list)
        if self.rightChild:
            self.rightChild.postorder(post_list)
        post_list.append(self.key)
        return post_list
    
    def inorder(self, in_list):
        if self.leftChild:
            self.leftChild.inorder(in_list)
        in_list.append(self.key)
        if self.rightChild:
            self.rightChild.inorder(in_list)
        return in_list
    
    def min_node_in_subtree(self, x):
        if x.leftChild:
            while x.leftChild is not None:
                x = x.leftChild
        else:
            x = x
        return x

    def replace(self, nodeToDelete, nodeToReplace):
        if nodeToDelete.parent is None:
            nodeToDelete = nodeToReplace
        elif nodeToDelete == nodeToDelete.parent.leftChild:
            nodeToDelete.parent.leftChild = nodeToReplace
        else:
            nodeToDelete.parent.rightChild = nodeToReplace
        if nodeToReplace is not None:
            nodeToReplace.parent = nodeToDelete.parent	
    
    def delete(self, x, k):
        if x.key == k:
            if x.leftChild is None:
                self.replace(x, x.rightChild)
            elif x.rightChild is None:
                self.replace(x, x.leftChild)
            else:
                nodeToReplace = self.min_node_in_subtree(x.rightChild)
                if nodeToReplace.parent != x:
                    self.replace(nodeToReplace, nodeToReplace.rightChild)
                    nodeToReplace.rightChild = x.rightChild
                    nodeToReplace.rightChild.parent = nodeToReplace
                self.replace(x, nodeToReplace)
                nodeToReplace.leftChild = x.leftChild
                nodeToReplace.leftChild.parent = nodeToReplace
        elif k < x.key:
            return self.delete(x.leftChild, k)
        else:
            return self.delete(x.rightChild, k)

class BinarySearchTree(object): 
    def __init__(self):
        self.root = None
        self.tree_size = 0

    def add(self, key, data):
        if self.root:
            self.tree_size += 1
            return self.root.add(key, data)
        else:
            self.root = Node(key, data)
            self.tree_size += 1
            return True
        
    def preorder_walk(self):
        if self.root is not None:
            return self.root.preorder(pre_list=[])

    def inorder_walk(self):
        if self.root is not None:
            return self.root.inorder(in_list=[])

    def postorder_walk(self):
        if self.root is not None:
            return self.root.postorder(post_list=[])

    def remove(self, h):
        self.tree_size -= 1
        return self.root.delete(self.root, h)

    def size(self):
        return self.tree_size

    def search(self, _key):
        r = self.root
        while r is not None and _key != r.key:
            if _key > r.key:
                r = r.rightChild
            else:
                r = r.leftChild
        if r is not None:
            return r.value
        return False

    def smallest(self):		
        k = self.root
        while k.leftChild is not None:
            k = k.leftChild
        return (k.key, k.value)	

    def largest(self):
        k = self.root
        while k.rightChild is not None:
            k = k.rightChild
        return (k.key, k.value)		
    
    def search(self, _key):
        k = self.root
        while k is not None and _key != k.key:
            if _key < k.key:
                k = k.leftChild
            else:
                k = k.rightChild
        if k is not None:
            return k.value
        return False

