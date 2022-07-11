# # given with square array, say if it's a magic square

# # square array n x n of numbers 1, 2, 3, ..., n**2
# # is called magic square if sums of numbers
# # in each row, column and diagonals are same

# creating matrix (casting str elements to int along the way):
side = int(input("Square side > "))
mtx: list = [[int(i) for i in input(f"Row {r + 1} > ").split()] for r in range(side)]


def magic(m: list[list]) -> bool:
    """func returns True if m is magic square else False"""

    # necessary constants:
    n: int = len(m)
    magic_const: int = int((n * (n ** 2 + 1)) / 2)      # magic constant (sum of any row, or column, or diagonal)

    # check if all nums of square form seq 1, 2, 3, ..., n**2
    all_nums = [elem for row in mtx for elem in row]
    if sorted(all_nums) != list(range(1, (n ** 2) + 1)):
        return False

    # check if sum-of-rows requirement met:
    for row in m:
        if sum(row) != magic_const:
            return False

    # check if sum-of-columns requirement met:
    for i in range(n):
        column = sum([m[j][i] for j in range(n)])
        if column != magic_const:
            return False

    # finally, check if sum-of-diagonals requirement met:
    major: list[int] = [m[i][i] for i in range(n)]
    minor: list[int] = [m[i][n - i - 1] for i in range(n)]
    if sum(major) != magic_const or sum(minor) != magic_const:
        return False

    # if all checks are good:
    return True


print(["Not a magic square", "Magic square"][magic(mtx)])
