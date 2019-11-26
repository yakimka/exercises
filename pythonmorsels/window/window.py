from collections import deque


def window(numbers, n, *, fillvalue=None):
    if n == 0:
        return []

    prev = deque(maxlen=n)
    for num in numbers:
        prev.append(num)

        if len(prev) >= n:
            yield tuple(prev)

    if len(prev) < n:
        yield tuple(list(prev) + [fillvalue for _ in range(n - len(prev))])
