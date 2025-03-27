# Red-Black Tree Implementation with Comprehensive Delete Operation

class RBNode:
    def __init__(self, value):
        self.value = value
        self.color = 'RED'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NULL_LEAF = RBNode(None)
        self.NULL_LEAF.color = 'BLACK'
        self.root = self.NULL_LEAF

    def insert(self, key):
        node = RBNode(key)
        node.left = node.right = self.NULL_LEAF
        parent, current = None, self.root

        while current != self.NULL_LEAF:
            parent = current
            current = current.left if key < current.value else current.right

        node.parent = parent
        if not parent:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        if not node.parent:
            node.color = 'BLACK'
            print(f"Inserted root {key}")
            return

        self.fix_insert(node)
        print(f"Inserted {key}")

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'RED':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'RED':
                    k.parent.color = u.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'RED':
                    k.parent.color = u.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)
        self.root.color = 'BLACK'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL_LEAF:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NULL_LEAF:
            node = node.left
        return node

    def delete(self, z_value):
        z = self.root
        while z != self.NULL_LEAF:
            if z_value == z.value:
                break
            z = z.left if z_value < z.value else z.right
        if z == self.NULL_LEAF:
            print(f"Delete {z_value}: Node not found!")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NULL_LEAF:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NULL_LEAF:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'BLACK':
            self.fix_delete(x)

        print(f"Deleted {z_value}")

    def fix_delete(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'RED':
                    s.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == s.right.color == 'BLACK':
                    s.color = 'RED'
                    x = x.parent
                else:
                    if s.right.color == 'BLACK':
                        s.left.color = 'BLACK'
                        s.color = 'RED'
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = s.right.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'RED':
                    s.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == s.left.color == 'BLACK':
                    s.color = 'RED'
                    x = x.parent
                else:
                    if s.left.color == 'BLACK':
                        s.right.color = 'BLACK'
                        s.color = 'RED'
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = s.left.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def search(self, value):
        current = self.root
        while current != self.NULL_LEAF:
            if current.value == value:
                print(f"Search {value}: Found ({current.color})")
                return True
            current = current.left if value < current.value else current.right
        print(f"Search {value}: Not Found")
        return False

    def inorder(self, node):
        return (self.inorder(node.left) if node.left != self.NULL_LEAF else []) + \
               [(node.value, node.color)] + \
               (self.inorder(node.right) if node.right != self.NULL_LEAF else []) if node != self.NULL_LEAF else []

# Enhanced Red-Black Tree Tests
def test_rbt():
    rbt = RedBlackTree()
    values_to_insert = [10, 20, 30, 15, 25, 5, 1]
    print("\n--- Inserting Nodes ---")
    for val in values_to_insert:
        rbt.insert(val)

    print("\n--- Searching Nodes ---")
    for val in [15, 100]:
        rbt.search(val)

    print("\n--- Deleting Nodes ---")
    for val in [20, 5, 100]:
        rbt.delete(val)

    print("\n--- Final Tree Inorder Traversal (Value, Color) ---")
    inorder_result = rbt.inorder(rbt.root)
    print(inorder_result)

if __name__ == "__main__":
    test_rbt()
