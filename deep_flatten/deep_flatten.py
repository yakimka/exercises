from collections.abc import Iterable


def deep_flatten(seq):
    for item in seq:
        if not isinstance(item, Iterable) or isinstance(item, str):
            yield item
        else:
            yield from deep_flatten(item)
