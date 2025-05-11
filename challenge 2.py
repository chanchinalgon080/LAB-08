from collections import deque

# Node definition for a binary tree
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Binary tree class with helper to build tree from level-order list
class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        if not values:
            return

        self.root = Node(values[0])
        queue = deque([self.root])
        index = 1

        while queue and index < len(values):
            current = queue.popleft()

            # Left child
            if index < len(values) and values[index] is not None:
                current.left = Node(values[index])
                queue.append(current.left)
            index += 1

            # Right child
            if index < len(values) and values[index] is not None:
                current.right = Node(values[index])
                queue.append(current.right)
            index += 1

# Serialize a binary tree to a string using level-order traversal
def serialize(root):
    if not root:
        return ""

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    return ",".join(result)

# Deserialize a string back to a binary tree
def deserialize(data):
    if not data:
        return None

    values = data.split(",")
    root = Node(int(values[0]))
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        if values[index] != "null":
            current.left = Node(int(values[index]))
            queue.append(current.left)
        index += 1

        if index < len(values) and values[index] != "null":
            current.right = Node(int(values[index]))
            queue.append(current.right)
        index += 1

    return root

# Helper to compare two binary trees
def trees_equal(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2 and node1.val == node2.val:
        return trees_equal(node1.left, node2.left) and trees_equal(node1.right, node2.right)
    return False

def test_serialize_deserialize():
    print("Running test cases...")

    # Case 1: Normal binary tree
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    serialized1 = serialize(tree1.root)
    deserialized1 = deserialize(serialized1)
    assert trees_equal(tree1.root, deserialized1), "Test case 1 failed"
    print("Test case 1 passed")

    # Case 2: Empty tree
    tree2 = BinaryTree()
    serialized2 = serialize(tree2.root)
    deserialized2 = deserialize(serialized2)
    assert deserialized2 is None, "Test case 2 failed"
    print("Test case 2 passed")

    # Case 3: Single node tree
    tree3 = BinaryTree()
    tree3.build_tree_from_list([42])
    serialized3 = serialize(tree3.root)
    deserialized3 = deserialize(serialized3)
    assert trees_equal(tree3.root, deserialized3), "Test case 3 failed"
    print("Test case 3 passed")

    # Case 4: Left-skewed tree
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, None, 3, None, None, None, 4])
    serialized4 = serialize(tree4.root)
    deserialized4 = deserialize(serialized4)
    assert trees_equal(tree4.root, deserialized4), "Test case 4 failed"
    print("Test case 4 passed")

    # Case 5: Right-skewed tree
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
    serialized5 = serialize(tree5.root)
    deserialized5 = deserialize(serialized5)
    assert trees_equal(tree5.root, deserialized5), "Test case 5 failed"
    print("Test case 5 passed")

    print("All test cases passed.")

# Run tests
test_serialize_deserialize()
