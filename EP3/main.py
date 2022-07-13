######################################################
###                                                ###
###  Arthur de Azevedo e Almeida Maia - 11819921   ###
###  Caio Balreira Nascimento - 11805342           ###
###  Exercicio-Programa 3                          ###
###  Professor: Renato Vicente                     ###
###  Turma: 02                                     ###
###                                                ###
######################################################

import numpy as np

n10 = [(-0.1488743389816312108848260, 0.2955242247147528701738930), (-0.4333953941292471907992659, 0.2692667193099963550912269), (-0.6794095682990244062343274, 0.2190863625159820439955349), (-0.8650633666889845107320967, 0.1494513491505805931457763), (-0.9739065285171717200779640, 0.0666713443086881375935688),
       (0.1488743389816312108848260, 0.2955242247147528701738930), (0.4333953941292471907992659, 0.2692667193099963550912269), (0.6794095682990244062343274, 0.2190863625159820439955349), (0.8650633666889845107320967, 0.1494513491505805931457763), (0.9739065285171717200779640, 0.0666713443086881375935688)]


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


def dupla(a, b, c, d, f):
    h1 = (b-a)/2
    h2 = (b+a)/2
    J = 0

    for i in range(len(n)):
        JX = 0
        r1 = n10[i][0]
        w1 = n10[i][1]
        x = h1*r1 + h2
        c1 = c(x)  # definir c(x) para cada exemplo
        d1 = d(x)  # definir d(x) para cada exemplo
        k1 = (d1 - c1)/2
        k2 = (d1 + c1)/2

        for j in range(len(n)):
            r2 = n10[j][0]
            w2 = n10[j][1]
            y = k1*r2 + k2
            Q = f(x, y)
            JX = JX + w2*Q

        J = J + w1*k1*JX

    J = h1*J
    return(J)


def main():

    return 0


if __name__ == "__main__":
    main()
