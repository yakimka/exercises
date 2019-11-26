def window(numbers, n):
    if n == 0:
        return []

    numbers = list(numbers)
    args = [numbers[i:] for i in range(n)]

    return list(zip(*args))

