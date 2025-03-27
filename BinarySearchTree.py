# Binary Search Tree Implementation (Unbalanced)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return BSTNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)
        print(f"Inserted {value}")

    def search(self, value):
        def _search(node, value):
            if node is None:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return _search(node.left, value)
            return _search(node.right, value)
        result = _search(self.root, value)
        print(f"Search {value}: {'Found' if result else 'Not Found'}")
        return result

    def delete(self, value):
        def _minValueNode(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, value):
            if node is None:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = _minValueNode(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            return node

        self.root = _delete(self.root, value)
        print(f"Deleted {value}")

    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        result = _inorder(self.root)
        print(f"Inorder traversal: {result}")
        return result

# Comprehensive BST Tests
def test_bst():
    bst = BST()
    values = [10, 5, 15, 3, 7, 13, 18]
    print("\n--- Inserting ---")
    for v in values:
        bst.insert(v)

    print("\n--- Searching ---")
    search_values = [7, 17, 3, 10]
    for v in search_values:
        bst.search(v)

    print("\n--- Current BST (Inorder) ---")
    bst.inorder()

    print("\n--- Deleting ---")
    delete_values = [10, 5, 18]
    for v in delete_values:
        bst.delete(v)
        bst.inorder()

    print("\n--- Final BST (Inorder) ---")
    bst.inorder()

if __name__ == "__main__":
    test_bst()
