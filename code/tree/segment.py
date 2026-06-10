from abc import ABC, abstractmethod

class BaseSegmentTree(ABC):
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [self.neutral_value] * (4 * self.n)
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    @property
    @abstractmethod
    def neutral_value(self):
        """The identity element for the operation (e.g., 0 for sum, 1 for product)"""
        pass

    @abstractmethod
    def _combine(self, left, right):
        """The operation defining how to combine two nodes"""
        pass

    def _build(self, tree_idx, start, end):
        if start == end:
            self.tree[tree_idx] = self.data[start]
            return
        mid = (start + end) // 2
        self._build(2 * tree_idx, start, mid)
        self._build(2 * tree_idx + 1, mid + 1, end)
        self.tree[tree_idx] = self._combine(self.tree[2 * tree_idx], self.tree[2 * tree_idx + 1])

    def update(self, target_idx, new_val):
        self._update(1, 0, self.n - 1, target_idx, new_val)

    def _update(self, tree_idx, start, end, target_idx, new_val):
        if start == end:
            self.tree[tree_idx] = new_val
            return
        mid = (start + end) // 2
        if start <= target_idx and target_idx <= mid:
            self._update(2 * tree_idx, start, mid, target_idx, new_val)
        else:
            self._update(2 * tree_idx + 1, mid + 1, end, target_idx, new_val)
        self.tree[tree_idx] = self._combine(self.tree[2 * tree_idx], self.tree[2 * tree_idx + 1])

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, tree_idx, start, end, l, r):
        if r < start or end < l:
            return self.neutral_value
        if l <= start and end <= r:
            return self.tree[tree_idx]
        mid = (start + end) // 2
        left_val = self._query(2 * tree_idx, start, mid, l, r)
        right_val = self._query(2 * tree_idx + 1, mid + 1, end, l, r)
        return self._combine(left_val, right_val)


class SumSegTree(BaseSegmentTree):
    neutral_value = 0

    def _combine(self, left, right):
        return left + right


class MinSegTree(BaseSegmentTree):
    neutral_value = float('inf')

    def _combine(self, left, right):
        return min(left, right)


class MaxSegTree(BaseSegmentTree):
    neutral_value = -float('inf')

    def _combine(self, left, right):
        return max(left, right)


class XorSegTree(BaseSegmentTree):
    neutral_value = 0

    def _combine(self, left, right):
        return left ^ right


class DivSegTree(BaseSegmentTree):
    neutral_value = 1.0

    def _combine(self, left, right):
        return left / right
