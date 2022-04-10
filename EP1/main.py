import numpy as np


def initializeResults(n):
    arr = []
    for position in range(1, n + 1):
        arr.append(np.cos((2 * np.pi * position**2)/n**2))
    return np.array(arr)


def calculateValue(i, j, n):
    if i == j:
        return 2

    if i != n:
        if i == j + 1:
            return (2*i - 1)/(4*i)
        if i == j - 1:
            return 1 - (2*i - 1)/(4*i)

    if i == j + 1:
        return (2*i - 1)/(2*i)
    if i == j - 1:
        return 1 - (2*i - 1)/(2*i)
    return 0


def inicializeMatrix(n):
    matrix = []
    for row in range(1, n + 1):
        line = []
        # O enunciado trata as linhas e colunas como indo de 1 a n, enquanto o Python as trata como indo
        # de 0 a n - 1. Isso pode gerar algumas confusões, mas é o motivo pelo qual o range, por exemplo,
        # vai de 1 a n + 1 neste código.
        for column in range(1, n + 1):
            value = calculateValue(row, column, n)
            line.append(value)
        matrix.append(line)
    matrix[0][-1] = 0.25
    matrix[n - 1][0] = (1 - (2*n - 1)/2*n)
    return np.matrix(matrix)


def main():
    print(inicializeMatrix(20))
    print(initializeResults(20))


if __name__ == "__main__":
    main()
