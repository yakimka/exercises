from collections import UserDict


class EasyDict(UserDict):
    def __init__(self, *args, normalize=False, **kwargs):
        self.normalize = normalize
        super().__init__(*args, **kwargs)

    def __getattr__(self, item):
        try:
            return self.data[self._normalized_key(item)]
        except KeyError:
            raise AttributeError(f"'EasyDict' object has no attribute '{item}'")

    def _normalized_key(self, key):
        return key.replace('_', ' ') if self.normalize else key

    def __setattr__(self, key, value):
        if key in ['data', 'normalize']:
            super().__setattr__(key, value)
        else:
            self.data[self._normalized_key(key)] = value
