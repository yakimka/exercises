import operator


class float_range:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            start, stop = 0.0, start
        self.start, self.stop, self.step = start, stop, step

        self.current = self.start
        self.operator = operator.lt if self.step > 0 else operator.gt

    def __iter__(self):
        while self.operator(self.current, self.stop):
            yield self.current
            self.current += self.step
