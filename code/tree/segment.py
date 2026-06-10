from abc import ABC, abstractmethod
import math

class AbstractSegmentTree(ABC):
    def __init__(self, data):
        self.n = len(data)
        # Allocate 2N space initialized to the operation's identity value
        self.tree = [self.identity] * (2 * self.n)
        self.build(data)

    @property
    @abstractmethod
    def identity(self):
        """The neutral element for the operation (e.g., 0 for sum, 1 for product)"""
        pass

    @abstractmethod
    def _combiner(self, a, b):
        """The actual operation to merge two nodes (e.g., addition, min, xor)"""
        pass

    def build(self, data):
        # 1. Fill leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        
        # 2. Build parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self._combiner(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        
        while pos > 1:
            pos //= 2
            self.tree[pos] = self._combiner(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        
        # Initialize result with the identity element
        res = self.identity
        
        while left <= right:
            if left % 2 == 1:
                res = self._combiner(res, self.tree[left])
                left += 1
            if right % 2 == 0:
                res = self._combiner(res, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
            
        return res


# ----------------------------------------------------
# 1. SUM SEGMENT TREE
# ----------------------------------------------------
class SumSegmentTree(AbstractSegmentTree):
    @property
    def identity(self): return 0
    def _combiner(self, a, b): return a + b


# ----------------------------------------------------
# 2. XOR SEGMENT TREE
# ----------------------------------------------------
class XorSegmentTree(AbstractSegmentTree):
    @property
    def identity(self): return 0  # x ^ 0 = x
    def _combiner(self, a, b): return a ^ b


# ----------------------------------------------------
# 3. MIN SEGMENT TREE
# ----------------------------------------------------
class MinSegmentTree(AbstractSegmentTree):
    @property
    def identity(self): return float('inf')  # min(x, inf) = x
    def _combiner(self, a, b): return min(a, b)


# ----------------------------------------------------
# 4. MAX SEGMENT TREE
# ----------------------------------------------------
class MaxSegmentTree(AbstractSegmentTree):
    @property
    def identity(self): return float('-inf')  # max(x, -inf) = x
    def _combiner(self, a, b): return max(a, b)


# ----------------------------------------------------
# 5. PRODUCT (MULTIPLICATION) SEGMENT TREE
# ----------------------------------------------------
class ProductSegmentTree(AbstractSegmentTree):
    @property
    def identity(self): return 1  # x * 1 = x
    def _combiner(self, a, b): return a * b


# ----------------------------------------------------
# 6. DIVISION SEGMENT TREE
# ----------------------------------------------------
class DivisionSegmentTree(AbstractSegmentTree):
    @property
    def identity(self): return 1.0  # x / 1 = x
    def _combiner(self, a, b): 
        # Float division tracking accumulated steps left-to-right
        return a / b
