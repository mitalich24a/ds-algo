from abc import ABC, abstractmethod

class BaseFenwickTree(ABC):
    def __init__(self, size):
        self.size = size
        self.tree = [self.neutral_value] * (size + 1)

    @property
    @abstractmethod
    def neutral_value(self): 
        pass

    @abstractmethod
    def _combine(self, current, delta): 
        """Combines the current tree value with an incoming update."""
        pass

    @abstractmethod
    def _difference(self, right_prefix, left_prefix): 
        """Calculates the difference to isolate the range query."""
        pass

    def update(self, idx, value):
        while idx <= self.size:
            self.tree[idx] = self._combine(self.tree[idx], value)
            idx = idx + (idx & (-idx))

    def query(self, idx):
        res = self.neutral_value
        while idx > 0:
            res = self._combine(res, self.tree[idx])
            idx = idx - (idx & (-idx))
        return res

    def range_query(self, left, right):
        return self._difference(self.query(right), self.query(left - 1))


class SumFenwick(BaseFenwickTree):
    neutral_value = 0

    def _combine(self, current, delta):
        return current + delta

    def _difference(self, right_prefix, left_prefix):
        return right_prefix - left_prefix


class XorFenwick(BaseFenwickTree):
    neutral_value = 0

    def _combine(self, current, delta):
        return current ^ delta

    def _difference(self, right_prefix, left_prefix):
        # XORing a prefix cancels it out, serving as the "difference"
        return right_prefix ^ left_prefix


class ProdFenwick(BaseFenwickTree):
    neutral_value = 1

    def _combine(self, current, delta):
        return current * delta

    def _difference(self, right_prefix, left_prefix):
        # Using integer division to find the difference between product prefixes
        return right_prefix // left_prefix
