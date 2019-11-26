from collections import deque
from itertools import islice, chain, repeat


def window(numbers, n, *, fillvalue=None):
    if n == 0:
        return []

    inumbers = iter(numbers)
    window_ = deque(islice(chain(inumbers, repeat(fillvalue)), n), maxlen=n)
    yield tuple(window_)
    for num in inumbers:
        window_.append(num)
        yield tuple(window_)
