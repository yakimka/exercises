from collections import UserDict


class PermaDict(UserDict):
    def __init__(self, *args, silent=False, **kwargs):
        self.silent = silent
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key not in self:
            super().__setitem__(key, value)
        elif not self.silent:
            raise KeyError(f'"{key}" already in dictionary.')

    def force_set(self, key, value):
        super().__setitem__(key, value)

    def update(self, *args, force=False, **kwargs):
        if force:
            self.data.update(*args, **kwargs)
        else:
            super().update(*args, **kwargs)
