# Studentnumber : 1716390
# Class : V2C

from queue import Queue

class BSTNode:
    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def insert(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e,None,None)
            else:
                parent.left = BSTNode(e,None,None)
        return not found


    """
    Method to insert a given value into the BST.
    Using child nodes of the current(self) node.
    This method calls a recursive function using the root node.

    Parameters
    ----------
    value : unkown
        The element the BSTNode you want to add to the BST.
    
    Returns
    -------
    boolean
        If the value was corretly inserted True.
        Otherwise the boolean will be False.
    """
    def rinsert(self, value):
        if self.element == value:
            return False

        if value < self.element:
            if self.left == None:
                newNode = BSTNode(value, None, None)
                self.left = newNode
                return True

            self.left.rinsert(value)
                          
        elif value > self.element:
            if self.right == None:            
                newNode = BSTNode(value, None, None)
                self.right = newNode
                return True
    
            self.right.rinsert(value)           


    def insertArray(self,a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
        mid = (low+high+1)//2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a,low,mid-1)
        if high > mid:
            self.insertArray(a,mid + 1,high)

    def search(self,e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    """
    Method to search for a given node in the BST.
    Using child nodes of the current(self) node.

    Parameters
    ----------
    value : unkown
        The element the BSTNode you're currently searching should have.
    
    Returns
    -------
    BSTNode/None
        If the value is found as a BSTNode element the method returns the BSTNode.
        Otherwise the method returns None.
    """
    def rsearch(self, value):
        if self.element == value:
            return self
        
        if self.right == None and self.left == None:
            return None

        if self.right != None:
            foundRight = self.right.rsearch(value)
            if foundRight != None:
                return foundRight
        
        if self.left != None:
            foundLeft = self.left.rsearch(value)       
            if foundLeft != None:
                return foundLeft

    def search2(self,e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None
        
    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self,e):
        parent = self.getParent(e)

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True

class BST:
    def __init__(self,a=None):
        if a:
            mid = len(a)//2
            self.root = BSTNode(a[mid],None,None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid+1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def search(self,e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None


    """
    Method to search for a given node in the BST.
    Using child nodes of the current(self) node.
    This method calls a recursive function using the root node.

    Parameters
    ----------
    value : unkown
        The element the BSTNode you're currently searching should have.
    
    Returns
    -------
    BSTNode/None
        If the value is found as a BSTNode element the method returns the BSTNode.
        Otherwise the method returns None.
    """
    def rsearch(self, value):
        if self.root and value:
            return self.root.rsearch(value)
        else:
            return None
    

    def insert(self,e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e,None,None)
                return True
        else:
            return False

    """
    Method to insert a given value into the BST.
    Using child nodes of the current(self) node.
    This method calls a recursive function using the root node.

    Parameters
    ----------
    value : unkown
        The element the BSTNode you want to add to the BST.
    
    Returns
    -------
    boolean
        If the value was corretly inserted True.
        Otherwise the boolean will be False.
    """
    def rinsert(self, value):
        if value:
            if self.root:
                return self.root.rinsert(value)
            else:
                self.root = BSTNode(value, None, None)
                return True
        else:
            return False


    def delete(self,e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree()
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False


    """
    Method used to get the maximum value currently in the BST.

    Returns
    -------
    unkown (any sortable value)
        The highest value in the BST.
    """
    def max(self):
        currentNode = self.root
        while(currentNode.right != None):
            currentNode = currentNode.right
        return currentNode.element

    """
    Method used to print all the elements on all the levels in the BST.

    Returns
    -------
    None
    """
    def showLevelOrder(self):
        levelQueue = Queue([self.root])
        newLevelAvailable = True


        levels = []
        while newLevelAvailable:
            level = []
            while len(levelQueue):
                level.append(levelQueue.dequeue())

            levels.append(level)

            if level != [None] * len(level):
                for node in level:
                    if node:
                        if node.left != None:
                            levelQueue.append(node.left)
                        else:
                            levelQueue.append(None)
            
                        if node.right != None:
                            levelQueue.append(node.right)
                        else:
                            levelQueue.append(None)
                    else:
                        levelQueue.append(None)
            else:
                newLevelAvailable = False

        levelDepth = len(levels)
        initialSpacing = levelDepth ** 2

        for level in levels:
     
            for node in level:
                print('', end=' ' * initialSpacing)
                if node:
                    print(node.element, end='')
                    pass
                else:
                    print(' ', end='')
                print('', end=' ' * initialSpacing)
            print()
            initialSpacing = int(initialSpacing*0.5)


if __name__ == '__main__':
    b = BST([1,2,3])
    print(b)
    print('----------------')
    b = BST([1,2,3,4])
    print(b)
    print('----------------')
    b = BST([1,2,3,4,5,6,7,8,9,10])
    print(b)
    print("Show level Order:")    
    b.showLevelOrder()    
    print('----------------')

    print(b.max())
    b.rinsert(12)
    print(b)
    print("Show level Order:")
    b.showLevelOrder()


    print(b.max())
    print('----------------')

    print(b.rsearch(7))
    print(b.rsearch(1))
    print(b.rsearch(2))
    print(b.rsearch(5))
    print(b.rsearch(10))
    print(b.rinsert(11))
    print(b.rinsert(13))
    print(b.rinsert(5))
    print('----------------')


    print('----------------')
    print(b)
    print('----------------')
    b = BST([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print(b)
    node = b.search(3)
    if node != None:
        print(node.element)
    node = b.search(4)
    if node != None:
        print(node.element)
    node = b.search(8)
    if node != None:
        print(node.element)
    node = b.search(11)
    if node != None:
        print(node.element)
    node = b.search(16)
    if node != None:
        print(node.element)
    b.insert(17)
    print(b)
    print('----------------')
    b.delete(14)
    print(b)
    print('----------------')

    print(b.insert(10))

    b = BST()
    for i in range(1,11):
        b.insert(i)
    print(b)
    print('----------------')

    b = BST(None)
    print(b)
    print('----------------')
    b = BST([])
    print(b)
    print('----------------')
    b = BST([0])
    print(b)
    print('----------------')

    b = BST()
    b.insert(3)
    b.insert(2)
    b.insert(10)
    b.insert(11)
    b.insert(9)
    b.insert(6)
    b.insert(7)
    b.insert(8)
    print(b)
    print('----------------')
    b.delete(3)
    print(b)
    print('----------------')
