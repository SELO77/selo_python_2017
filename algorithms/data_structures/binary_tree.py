import pdb

# pdb.set_trace()

class Node(object):

    def __init__(self, key=None, val=None, size_of_subtree=1):
        self.key = key
        self.val = val
        self.size_of_subtree = size_of_subtree
        self.left = None
        self.right = None

    def __repr__(self):
        return "k: %s, v: %s" % (self.key, self.val)


class BinarySearchTree(object):
    """
    이진탐색트리
    * 각 노드에 값이 있다.
    * 각 노드의 키값은 모두 달라야 한다.
    * 값들은 전순서가 있다.
    * 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져 있다.
    * 노드의 오른쪽 서브트리에는 그 노드의 값보다 큰 값들을 지닌 노드들로 이루어져 있다.
    * 좌우 하위 트리는 각각이 다시 이진 탐색 트리여야 한다.
    * 중복된 노드가 없어야 한다.
    """

    def __init__(self):
        self.root = None

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size_of_subtree

    def size(self):
        return self._size(self.root)

    def _get(self, key, node):
        if node is None:
            return None

        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        else:
            return node.val

    def get(self, key):
        return self._get(key, self.root)

    def _put(self, key, val, node):
        if node is None:
            return Node(key, val)

        if key < node.key:
            node.left = self._put(key, val, node.left)
        elif key > node.key:
            node.right = self._put(key, val, node.right)
        else:
            node.val = val

        node.size_of_subtree = self._size(node.left) + self._size(node.right) + 1
        return node

    def put(self, key, val):
        self.root = self._put(key, val, self.root)

    def _min_node(self):
        min_node = self.root
        if min_node is None:
            return None

        while min_node.left is not None:
            min_node = min_node.left

        return min_node

    def min_key(self):
        min_node = self._min_node()
        if min_node is None:
            return None
        else:
            return min_node.key

    def _max_node(self):
        max_node = self.root
        if max_node is None:
            return None

        while max_node.right is not None:
            max_node = max_node.right

        return max_node

    def max_key(self):
        max_node = self._max_node()
        if max_node is None:
            return None
        else:
            return max_node.key

    def _floor_node(self, key, node):
        if node is None:
            return None

        if key < node.key:
            return self._floor_node(key, node.left)
        elif key > node.key:
            return self._floor_node(key, node.right)
        else:
            return node

    def floor_key(self, key):
        floor_node = self._floor_node(key, self.root)
        if floor_node is None:
            return None
        else:
            return floor_node.key

    def _ceiling_node(self, key, node):
        if node is None:
            return None

        if key < node.key:
            attempt_in_left = self._ceiling_node(key, node.left)
            if attempt_in_left is None:
                return node
            else:
                return attempt_in_left
        elif key > node.key:
            return self._ceiling_node(key, node.right)
        else:
            return node

    def ceiling_key(self, key):
        ceiling_node = self._ceiling_node(key, self.root)
        if ceiling_node is None:
            return None
        else:
            return ceiling_node.key

    def _rank(self, key, node):
        if node is None:
            return None

        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return self._rank(key, node.right)
        else:
            return self._size(node.left)

    def rank(self, key):
        return self._rank(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                old_node = node
                node = self._ceiling_node(key, node.right)
                node.right = self._delete_min(old_node.right)
                node.left = old_node.left
        node.size_of_subtree = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.size_of_subtree = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.size_of_subtree = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def _keys(self, node, keys):
        if node is None:
            return keys

        if node.left is not None:
            keys = self._keys(node.left, keys)

        keys.append(node.key)

        if node.right is not None:
            keys = self._keys(node.right, keys)

        return keys

    def keys(self):
        keys = []
        return self._keys(self.root, keys)