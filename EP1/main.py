import numpy as np


def initializeResults(n, manual=True):
    array = np.empty((n))
    if(manual):
        for i in range(0, n):
            array[i] = input(f"insira d{str(i + 1)}: ")

        return array

    for position in range(1, n + 1):
        array[position - 1] = np.cos((2 * np.pi * position**2)/(n**2))

    print("O vetor contendo os valores d obtido é: ", array, "\n")

    return array


def initializeMatrix(n, manual=True):
    a = np.zeros((n))
    b = np.zeros((n))
    c = np.zeros((n))

    if (manual):
        for i in range(0, n):
            a[i] = np.float64(input(f"Insira a{str(i + 1)}: "))

        for i in range(0, n):
            b[i] = np.float64(input(f"Insira b{str(i + 1)}: "))

        for i in range(0, n):
            c[i] = np.float64(input(f"Insira c{str(i + 1)}: "))

        if (a[0] == 0 and c[n - 1] == 0):
            return a, b, c, False

        return a, b, c, True

    for i in range(1, n):
        a[i - 1] = (2*i - 1)/(4*i)

    a[n - 1] = (2*n - 1)/(2*n)
    b += 2
    c = 1 - a

    print("O vetor contendo os valores a obtido é: ", a, "\n")
    print("O vetor contendo os valores b obtido é: ", b, "\n")
    print("O vetor contendo os valores c obtido é: ", c, "\n")

    return a, b, c, True


def tridiagonalLU(n, a, b, c, cyclic):

    if (cyclic):
        a = a[:n - 1]
        a[0] = 0
        b = b[:n - 1]
        c = c[:n - 1]
        c[n - 2] = 0
        n = n - 1

    L = np.zeros((n, n))
    U = np.zeros((n, n))
    u = np.zeros((n))
    l = np.zeros((n))
    u[0] = b[0]

    for i in range(1, n):
        l[i] = a[i]/u[i-1]
        u[i] = b[i] - l[i]*c[i-1]

    for i in range(0, n):
        L[i][i] = 1
        U[i][i] = u[i]
        if i < n - 1:
            L[i+1][i] = l[i+1]
            U[i][i+1] = c[i]

    return L, U


def tridiagonalSolution(n, a, b, c, d):  # Ax = d
    y = np.zeros((n))
    x = np.zeros((n))
    # Ly = d
    L, U = tridiagonalLU(n, a, b, c, False)

    y[0] = d[0]
    for i in range(1, n):
        y[i] = d[i]-L[i][i - 1]*y[i-1]

    # Ux = y
    x[n-1] = y[n-1]/U[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i]-U[i][i+1]*x[i+1])/U[i][i]

    return x


def cyclicTridiagonalSolution(n, a, b, c, d):
    # Ax = d

    v = np.zeros(n-1)
    x = np.zeros(n)
    x_til = np.zeros(n-1)
    d_til = d[:n-1]
    y_til = np.zeros(n-1)
    z_til = np.zeros(n-1)

    v[0] = a[0]
    v[n-2] = c[n - 2]

    y_til = tridiagonalSolution(n - 1, a, b, c, d_til)

    z_til = tridiagonalSolution(n - 1, a, b, c, v)

    x[n-1] = (d[n-1]-c[n-1]*y_til[0] - a[n-1]*y_til[n-2]) / \
        (b[n-1] - c[n-1]*z_til[0] - a[n-1]*z_til[n-2])

    x_til = y_til - x[n-1]*z_til

    x[0:n-1] = x_til

    return x


def solveSystem(n, a, b, c, d, cyclic):
    if(cyclic):
        return cyclicTridiagonalSolution(n, a, b, c, d)

    return tridiagonalSolution(n, a, b, c, d)


def main():
    print("")
    print("Bem-vindo ao programa de decomposição LU para matrizes tridiagonais escrito por Arthur Maia e Caio Balreira. \n")
    print("Neste programa, existem 4 funcionalidades:\n 1) Decomposição LU de uma matriz \n 2) Resolução de um sistema matricial por decomposição LU \n 3) Resolução do sistema matricial de teste, fornecido no enunciado \n 0) Encerrar o programa \n")

    while True:
        while True:
            try:
                choice = int(
                    input("Escolha a funcionalidade que deseja executar: "))
                print("")
                if (choice < 0 or choice > 3):
                    raise ValueError()
                break
            except ValueError:
                print("Esta funcionalidade não é válida. Por favor, tente outra \n")

        if (choice == 1):
            dim = int(input("Insira a dimensão da matriz: "))
            A, B, C, cyclic = initializeMatrix(dim)
            L, U = tridiagonalLU(dim, A, B, C, cyclic)
            print(f"A matriz L obtida foi: \n {L}", "\n")
            print(f"A matriz U obtida foi: \n{U}", "\n")

        if (choice == 2):
            dim = int(input("Insira a dimensão da matriz: "))
            A, B, C, cyclic = initializeMatrix(dim)
            D = initializeResults(dim)
            r = solveSystem(dim, A, B, C, D, cyclic)
            print(
                f"O vetor de resultados obtido para o sistema foi: {r}", "\n")

        if (choice == 3):
            dim = int(input("Insira a dimensão da matriz: "))
            A, B, C, _ = initializeMatrix(dim, False)
            D = initializeResults(dim, False)
            r = solveSystem(dim, A, B, C, D, True)
            print(
                f"O vetor de resultados obtido para o sistema foi: {r}", "\n")

        if (choice == 0):
            print("Programa encerrado.", "\n")
            break

        print("Seguem as opções novamente: \n 1) Decomposição LU de uma matriz \n 2) Resolução de um sistema matricial por decomposição LU \n 3) Resolução do sistema matricial de teste, fornecido no enunciado \n 0) Encerrar o programa \n")


if __name__ == "__main__":
    main()
