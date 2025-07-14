class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        n1 = Node(value)
        if self.root is None:
            self.root = n1
        else:
            n2 = self.root
            while n2 is not None:
                if value > n2.data:
                    if n2.right is None:
                        n2.right = n1
                        break
                    n2 = n2.right
                elif value < n2.data:
                    if n2.left is None:
                        n2.left = n1
                        break
                    n2 = n2.left
                else:
                    print("Try again! This value already exists in the tree.")
                    break
    def find(self, value):
        n1 = self.root
        while n1 is not None:
            if value > n1.data:
                n1 = n1.right
            if value < n1.data:
                n1 = n1.left
            if value == n1.data:
                break
        return n1
    def remove(self, value):
        if self.find(value) is None:
            return
        else:
            n1 = self.root
            while n1 is not None:
                if value > n1.data:
                    if n1.right.data == value:
                        break
                    n1 = n1.right
                if value < n1.data:
                    if n1.left.data == value:
                        break
                    n1 = n1.left
            if value > n1.data:
                n3 = n1.right
                if n3.right is None and n3.left is None:
                    n1.right = None
                    return
                n2 = n3
            elif value < n1.data:
                n3 = n1.left
                if n3.right is None and n3.left is None:
                    n1.left = None
                    return
                n2 = n3
            if n2.right is None:
                n2 = n2.left
                while n2.right is not None:
                    n2 = n2.right
                n4 = n3.left
                while n4.right is not n2:
                    n4 = n4.right
                n4.right = None
            else:
                n2 = n2.right
                while n2.left is not None:
                    n2 = n2.left
                n4 = n3.right
                while n4.left is not n2:
                    n4 = n4.left
                n4.left = None
            if value > n1.data:
                n1.right = n2
                n2.right = n3.right
                n2.left = n3.left
            elif value < n1.data:
                n1.left = n2
                n2.right = n3.right
                n2.left = n3.left
    def equals(self, tree):
        return self._equal_helper(self.root, tree.root)
    def _equal_helper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1.data is not node2.data:
            return False
        return self._equal_helper(node1.right, node2.right) and self._equal_helper(node1.left, node2.left)
    def print_tree(self):
        l = []
        self._print_helper(self.root, l, 0)
        for value in l:
            print(value)
    def _print_helper(self, node, l, level):
        if node is None:
            return
        if len(l) < (level +1):
            l.append([])
        l[level].append(node.data)
        self._print_helper(node.left, l , level + 1)
        self._print_helper(node.right, l, level + 1)
if __name__ == "__main__":
    t = Tree()
    t.insert(2)
    t.insert(4)
    t.insert(6)
    t.insert(8)
    t.insert(10)
    t.insert(9)
    t.insert(7)
    t.insert(5)
    t.insert(3)
    t.insert(1)
    t.remove(3)
    t.remove(6)

    b = Tree()
    b.insert(2)
    b.insert(4)
    b.insert(6)
    b.insert(8)
    b.insert(10)
    b.insert(9)
    b.insert(7)
    b.insert(5)
    b.insert(3)
    b.insert(1)

    print(t.equals(b))
    print(t.equals(t)) 