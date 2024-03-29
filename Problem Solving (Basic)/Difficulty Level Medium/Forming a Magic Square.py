# https://www.hackerrank.com/challenges/magic-square-forming

def calculate_cost(matrix, magic_square):
    return sum(abs(matrix[i][j] - magic_square[i][j]) for i in range(3) for j in range(3))


def formingMagicSquare(matrix):
    all_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    min_cost = float('inf')

    for magic_square in all_magic_squares:
        cost = calculate_cost(matrix, magic_square)
        min_cost = min(min_cost, cost)

    return min_cost