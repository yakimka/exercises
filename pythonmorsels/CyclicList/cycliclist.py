from collections import UserList


class CyclicList(UserList):
    def __getitem__(self, item):
        item = item % len(self.data)
        return self.data[item]
