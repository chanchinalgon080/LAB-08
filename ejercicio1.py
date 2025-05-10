class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

def balance_bst(bst):
    # Step 1: Get the inorder traversal of the tree (sorted list of nodes)
    inorder_nodes = bst.inorder()

    # Step 2: Build a balanced BST from the sorted list
    return _sorted_array_to_bst(inorder_nodes)

def _sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    node = Node(arr[mid])
    node.left = _sorted_array_to_bst(arr[:mid])
    node.right = _sorted_array_to_bst(arr[mid+1:])
    return node

# Helper function to print the tree inorder
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.value, end=' ')
        print_inorder(node.right)

# Test cases
def test_balance_bst():
    """Test the balance_bst function. ⚖️"""
    # Test Case 1: Already balanced tree 🌳
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)
    
    # Test Case 2: Right-skewed tree 📐➡️
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    
    # Test Case 3: Left-skewed tree 📐⬅️
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)
    
    # Test Case 4: Empty tree 🈳
    bst4 = BinarySearchTree()
    
    # Test Case 5: Single node tree 🌱
    bst5 = BinarySearchTree()
    bst5.insert(42)
    
    # Test Case 1: Balance the already balanced tree
    print("Balanced Tree 1 (already balanced):")
    balanced1 = balance_bst(bst1)
    print_inorder(balanced1)
    print()

    # Test Case 2: Balance the right-skewed tree
    print("Balanced Tree 2 (right skewed):")
    balanced2 = balance_bst(bst2)
    print_inorder(balanced2)
    print()

    # Test Case 3: Balance the left-skewed tree
    print("Balanced Tree 3 (left skewed):")
    balanced3 = balance_bst(bst3)
    print_inorder(balanced3)
    print()

    # Test Case 4: Balance the empty tree
    print("Balanced Tree 4 (empty):")
    balanced4 = balance_bst(bst4)
    print_inorder(balanced4)
    print()

    # Test Case 5: Balance the single node tree
    print("Balanced Tree 5 (single node):")
    balanced5 = balance_bst(bst5)
    print_inorder(balanced5)
    print()

# Run the tests
test_balance_bst()
