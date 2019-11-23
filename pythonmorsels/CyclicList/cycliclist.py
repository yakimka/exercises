from collections import UserList


class CyclicList(UserList):
    def __getitem__(self, item):
        return super().__getitem__(self._get_cyclic_item(item))

    def _get_cyclic_item(self, item):
        return item % len(self.data)

    def __setitem__(self, key, value):
        return super().__setitem__(self._get_cyclic_item(key), value)
