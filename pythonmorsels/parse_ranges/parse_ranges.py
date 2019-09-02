import re


def parse_ranges(numbers: str):
    cleaned = re.sub(r'->.*?,', ',', numbers.replace(' ', ''))
    parts = cleaned.split(',')

    for part in parts:
        int_parts = [int(p) for p in part.split('-')]
        if len(int_parts) == 1:
            start = end = int_parts[0]
        else:
            start, end = int_parts

        yield from range(start, end + 1)
