def compact(seq):
    prev = None
    for i, item in enumerate(seq):
        if i == 0 or prev != item:
            yield item
        prev = item
