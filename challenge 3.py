from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

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

            if index < len(values) and values[index] is not None:
                current.left = Node(values[index])
                queue.append(current.left)
            index += 1

            if index < len(values) and values[index] is not None:
                current.right = Node(values[index])
                queue.append(current.right)
            index += 1

def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if root.val == p or root.val == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# ============================
# Test Cases
# ============================

def test_lowest_common_ancestor():
    print("Running test cases...")

    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    lca1 = lowest_common_ancestor(tree1.root, 4, 6)
    if lca1:
        assert lca1.val == 1, f"Test case 1 failed: expected 1, got {lca1.val}"
    else:
        print("Test case 1 failed: LCA not found.")
    print("Test case 1 passed")

    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    lca2 = lowest_common_ancestor(tree2.root, 2, 4)
    if lca2:
        assert lca2.val == 2, f"Test case 2 failed: expected 2, got {lca2.val}"
    else:
        print("Test case 2 failed: LCA not found.")
    print("Test case 2 passed")

    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    lca3 = lowest_common_ancestor(tree3.root, 2, 3)
    if lca3:
        assert lca3.val == 1, f"Test case 3 failed: expected 1, got {lca3.val}"
    else:
        print("Test case 3 failed: LCA not found.")
    print("Test case 3 passed")

    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    lca4 = lowest_common_ancestor(tree4.root, 1, 3)
    if lca4:
        assert lca4.val == 1, f"Test case 4 failed: expected 1, got {lca4.val}"
    else:
        print("Test case 4 failed: LCA not found.")
    print("Test case 4 passed")

    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3])
    lca5 = lowest_common_ancestor(tree5.root, 2, 99)
    if lca5 is None:
        print("Test case 5 passed (node not found, as expected)")
    else:
        print(f"Test case 5 failed: Expected None, got {lca5.val}")

    print("All test cases completed.")

# Call the test function
test_lowest_common_ancestor()
