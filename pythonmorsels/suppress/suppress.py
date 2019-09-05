from functools import wraps


class _Context:
    exception = None
    traceback = None


class suppress:
    def __init__(self, *args):
        self._context = _Context()
        self._exceptions = args

    def __enter__(self):
        return self._context

    def __exit__(self, type, value, traceback):
        self._context.exception = value
        self._context.traceback = traceback
        return isinstance(value, self._exceptions)

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return inner
