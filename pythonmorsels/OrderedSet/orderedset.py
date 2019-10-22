from collections import OrderedDict
from collections.abc import Set


class OrderedSet(Set):
    def __init__(self, items):
        self.items = OrderedDict.fromkeys(items)

    def __repr__(self):
        return '{}({})'.format(type(self), list(self.items.keys()))

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.items == other.items
        elif isinstance(other, Set):
            return set(self.items) == other
        else:
            return NotImplemented

    def __getitem__(self, item):
        return list(self.items)[item]

    def add(self, item):
        self.items[item] = None

    def discard(self, item):
        self.items.pop(item, None)
