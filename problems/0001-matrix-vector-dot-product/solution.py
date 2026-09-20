def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Check if dimensions are compatible
    if len(a[0]) != len(b):
        return -1

    result = []

    # Go through each row of the matrix
    for row in a:
        total = 0

        # Multiply corresponding elements and add them
        for i in range(len(b)):
            total += row[i] * b[i]

        result.append(total)

    return result