import numpy as np


def initializeResults(n):
    array = np.empty((n))
    for position in range(1, n + 1):
        array[position - 1] = np.cos((2 * np.pi * position**2)/n**2)
    return array


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
    matrix = np.zeros((n, n))
    for row in range(1, n + 1):
        # O enunciado trata as linhas e colunas como indo de 1 a n, enquanto o Python as trata como indo
        # de 0 a n - 1. Isso pode gerar algumas confusões, mas é o motivo pelo qual o range, por exemplo,
        # vai de 1 a n + 1 neste código.
        for column in range(row - 1, row + 2):
            c = column % 20
            matrix[row - 1][c - 1] = calculateValue(row, column, n)
    return matrix


def main():
    print("---------------------------")
    print(inicializeMatrix(20))
    print(initializeResults(20))


if __name__ == "__main__":
    main()
