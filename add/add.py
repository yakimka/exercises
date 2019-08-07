def add(*args):
    width = len(args[0][0])
    height = len(args[0])
    result = [[0 for _ in range(width)] for _ in range(height)]

    for matrix in args:
        if height != len(matrix) or any([width != len(row) for row in matrix]):
            raise ValueError('Given matrices are not the same size.')

        for x in range(height):
            for y in range(width):
                result[x][y] += matrix[x][y]

    return result
