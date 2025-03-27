# Comprehensive AVL Tree Implementation

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            print(f"Inserted {key}")
            return AVLNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left Left Case
        if balance > 1 and key < root.left.value:
            print(f"Right rotation on {root.value} due to Left-Left imbalance")
            return self.rightRotate(root)
        # Right Right Case
        if balance < -1 and key > root.right.value:
            print(f"Left rotation on {root.value} due to Right-Right imbalance")
            return self.leftRotate(root)
        # Left Right Case
        if balance > 1 and key > root.left.value:
            print(f"Left rotation on {root.left.value} and Right rotation on {root.value} due to Left-Right imbalance")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Right Left Case
        if balance < -1 and key < root.right.value:
            print(f"Right rotation on {root.right.value} and Left rotation on {root.value} due to Right-Left imbalance")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):
        if not root:
            print(f"Delete {key}: Node not found")
            return root
        elif key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                print(f"Deleted {key}, no left child")
                return root.right
            elif not root.right:
                print(f"Deleted {key}, no right child")
                return root.left
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
            print(f"Deleted {key}, replaced with successor {temp.value}")

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Balancing after deletion
        if balance > 1 and self.getBalance(root.left) >= 0:
            print(f"Right rotation on {root.value} due to imbalance after deletion")
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            print(f"Left rotation on {root.value} due to imbalance after deletion")
            return self.leftRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            print(f"Left rotation on {root.left.value} and Right rotation on {root.value} after deletion")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            print(f"Right rotation on {root.right.value} and Left rotation on {root.value} after deletion")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, node):
        return node.height if node else 0

    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    def getMinValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root:
            print(f"Search {key}: Not Found")
            return False
        if root.value == key:
            print(f"Search {key}: Found")
            return True
        elif key < root.value:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        return (self.inorder(root.left) if root.left else []) + [root.value] + (self.inorder(root.right) if root.right else []) if root else []

# Comprehensive AVL Tree Tests
def test_avl():
    avl = AVLTree()
    root = None
    values_to_insert = [20, 4, 15, 70, 50, 100, 80, 90]

    print("\n--- Inserting Nodes ---")
    for val in values_to_insert:
        root = avl.insert(root, val)

    print("\n--- Searching Nodes ---")
    for val in [15, 90, 99]:
        avl.search(root, val)

    print("\n--- Deleting Nodes ---")
    for val in [70, 4, 100, 20, 999]:
        root = avl.delete(root, val)

    print("\n--- Final AVL Tree Inorder Traversal ---")
    inorder_result = avl.inorder(root)
    print(inorder_result)

if __name__ == "__main__":
    test_avl()
