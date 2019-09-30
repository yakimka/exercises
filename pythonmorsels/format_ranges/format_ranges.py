from collections import Counter


def format_ranges(sequence):
    sequence = Counter(sorted(sequence))
    ranges = []

    while sequence:
        start = end = None
        for n in sequence:
            sequence[n] -= 1
            if start is None:
                start = n
            elif n - end != 1:
                ranges.append((start, end))
                start = n
            end = n

        ranges.append((start, end))
        sequence += Counter()

    ranges.sort()


    return ','.join(f'{s}' if s == e else f'{s}-{e}' for s, e in ranges)
