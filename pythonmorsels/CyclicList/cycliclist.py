from collections import UserList
from itertools import cycle


class CyclicList(UserList):

    def __iter__(self):
        return cycle(self.data)
    
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(self._slice_generator(item))
        return super().__getitem__(self._get_cyclic_item(item))

    def _slice_generator(self, slice_):
        start = slice_.start or 0
        stop = len(self) if slice_.stop is None else slice_.stop
        if start < 0 and slice_.stop is None:
            stop = 0
        step = 1 if slice_.step is None else slice_.step

        for i in range(start, stop, step):
            yield self[i]

    def _get_cyclic_item(self, item):
        return item % len(self.data)

    def __setitem__(self, key, value):
        return super().__setitem__(self._get_cyclic_item(key), value)
