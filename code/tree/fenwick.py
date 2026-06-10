class BaseFenwickTree(ABC):
    def __init__(self, size):
        self.size = size
        self.tree = [self.neutral_value] * (size + 1)

    @property
    @abstractmethod
    def neutral_value(self): pass

    @abstractmethod
    def _merge(self, current, delta): pass

    @abstractmethod
    def _inverse(self, right_prefix, left_prefix): pass

    def update(self, idx, value):
        while idx <= self.size:
            self.tree[idx] = self._merge(self.tree[idx], value)
            idx = idx + (idx & (-idx))

    def query(self, idx):
        res = self.neutral_value
        while idx > 0:
            res = self._merge(res, self.tree[idx])
            idx = idx - (idx & (-idx))
        return res

    def range_query(self, left, right):
        return self._inverse(self.query(right), self.query(left - 1))


class SumFenwick(BaseFenwickTree):
    neutral_value = 0

    def _merge(self, current, delta):
        return current + delta

    def _inverse(self, r, l):
        return r - l


class XorFenwick(BaseFenwickTree):
    neutral_value = 0

    def _merge(self, current, delta):
        return current ^ delta

    def _inverse(self, r, l):
        # XOR is its own inverse, so we use ^ instead of -
        return r ^ l


class ProdFenwick(BaseFenwickTree):
    neutral_value = 1

    def _merge(self, current, delta):
        return current * delta

    def _inverse(self, r, l):
        # Using integer division to undo the prefix multiplications
        return r // l
