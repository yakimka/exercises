from collections import OrderedDict
from collections.abc import MutableSet, Sequence


class OrderedSet(Sequence, MutableSet):
    def __init__(self, items):
        self.items = OrderedDict.fromkeys(items)
        # or
        # (need to modify "add" and "discard" methods)
        # self.items = set()
        # self.order = []
        # self |= iterable

    def __repr__(self):
        return 'OrderedSet({})'.format(list(self.items.keys()))

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.items == other.items

        return super().__eq__(other)

    def __getitem__(self, item):
        return list(self.items)[item]

    def add(self, item):
        self.items[item] = None

    def discard(self, item):
        self.items.pop(item, None)
