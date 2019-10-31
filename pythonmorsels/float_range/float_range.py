from math import ceil


class float_range:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            start, stop = 0.0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        current = self.start
        for _ in range(len(self)):
            yield current
            current += self.step

    def __len__(self):
        return max(ceil((self.stop - self.start) / self.step), 0)

    def __reversed__(self):
        current = self.start + self.step * (len(self) - 1)
        for _ in range(len(self)):
            yield current
            current -= self.step

    def __eq__(self, other):
        if isinstance(other, (type(self), range)):
            return self._get_attrs(self) == self._get_attrs(other)

        return NotImplemented

    @staticmethod
    def _get_attrs(instance):
        if len(instance) == 0:
            return ()
        start = next(iter(instance))
        stop = next(iter(reversed(instance)))
        return start, stop, len(instance)
