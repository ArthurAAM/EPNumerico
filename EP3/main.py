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
from math import e
import matplotlib.pyplot as plt

n6 = [(-0.2386191860831969086305017, 0.4679139345726910473898703), (-0.6612093864662645136613996, 0.3607615730481386075698335), (-0.9324695142031520278123016, 0.1713244923791703450402961),
      (0.2386191860831969086305017, 0.4679139345726910473898703), (0.6612093864662645136613996, 0.3607615730481386075698335), (0.9324695142031520278123016, 0.1713244923791703450402961)]

n8 = [(-0.1834346424956498049394761, 0.3626837833783619829651504), (-0.5255324099163289858177390, 0.3137066458778872873379622), (-0.7966664774136267395915539, 0.2223810344533744705443560), (-0.9602898564975362316835609, 0.1012285362903762591525314),
      (0.1834346424956498049394761, 0.3626837833783619829651504), (0.5255324099163289858177390, 0.3137066458778872873379622), (0.7966664774136267395915539, 0.2223810344533744705443560), (0.9602898564975362316835609, 0.1012285362903762591525314)]

n10 = [(-0.1488743389816312108848260, 0.2955242247147528701738930), (-0.4333953941292471907992659, 0.2692667193099963550912269), (-0.6794095682990244062343274, 0.2190863625159820439955349), (-0.8650633666889845107320967, 0.1494513491505805931457763), (-0.9739065285171717200779640, 0.0666713443086881375935688),
       (0.1488743389816312108848260, 0.2955242247147528701738930), (0.4333953941292471907992659, 0.2692667193099963550912269), (0.6794095682990244062343274, 0.2190863625159820439955349), (0.8650633666889845107320967, 0.1494513491505805931457763), (0.9739065285171717200779640, 0.0666713443086881375935688)]

dimensoes = [7, 15, 31, 63]


def tridiagonalLU(n, a, b, c):

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
    L, U = tridiagonalLU(n, a, b, c)

    y[0] = d[0]
    for i in range(1, n):
        y[i] = d[i]-L[i][i - 1]*y[i-1]

    # Ux = y
    x[n-1] = y[n-1]/U[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i]-U[i][i+1]*x[i+1])/U[i][i]

    return x


def dupla(a, b, n, f, c=lambda x: 0, d=lambda x: 1):
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


def innerProduct(anterior, atual, proximo, h, n, case, f, k, q):
    if case == "inferior":
        return (-1) * ((1 / h) ** 2) * dupla(anterior, atual, n, lambda x, y: k(x, y) + (atual - x) * (x - anterior) * q(x, y))

    if case == "superior":
        return (-1) * ((1 / h) ** 2) * dupla(atual, proximo, n, lambda x, y: (k(x, y) + (proximo - x) * (x - atual) * q(x, y)))

    if case == "principal":
        return (1 / h) ** 2 * (dupla(anterior, atual, n, lambda x, y: (k(x, y) + (x - anterior)**2 * q(x, y))) + dupla(atual, proximo, n, lambda x, y: (k(x, y) + (proximo - x)**2 * q(x, y))))

    if case == "resultados":
        return (1 / h) * (dupla(anterior, atual, n, lambda x, y: ((x - anterior) * f(x, y))) + dupla(atual, proximo, n, lambda x, y: ((proximo - x) * f(x, y))))

    return 0


def solveSystem(f, k, q, L, dim, n):
    h = L / (dim + 1)
    xi = [i * h for i in range(dim + 2)]
    a = list()
    b = list()
    c = list()
    d = list()

    for i in range(dim):
        anterior = xi[i]
        atual = xi[i + 1]
        proximo = xi[i + 2]
        a.append(innerProduct(anterior, atual,
                 proximo, h, n, "inferior", f, k, q))
        b.append(innerProduct(anterior, atual,
                 proximo, h, n, "principal", f, k, q))
        c.append(innerProduct(anterior, atual,
                 proximo, h, n, "superior", f, k, q))
        d.append(innerProduct(anterior, atual,
                 proximo, h, n, "resultados", f, k, q))

    return tridiagonalSolution(dim, a, b, c, d)


def phi(x, xi_anterior, xi_atual, xi_proximo, h):
    if (xi_anterior < x <= xi_atual):
        return (x - xi_anterior)/h

    if (xi_atual < x <= xi_proximo):
        return (xi_proximo - x)/h

    return 0


def uBarra(x, xi, solucoes, h, homogeneo=True, a=1, b=1, L=1):
    if(homogeneo):
        uBarra = 0
        for i in range(len(solucoes)):
            uBarra += solucoes[i] * phi(x, xi[i], xi[i + 1], xi[i + 2], h)
        return uBarra
    return uBarra(x, xi, solucoes, h) + (a + (b - a) * x) / L


def biggestError(solucoes, u, dim, L):
    h = L / (dim + 1)
    xi = [i * h for i in range(dim + 2)]
    erroMax = 0
    erroMaxUExato = 0
    erroMaxUBarra = 0
    for x in xi:
        if abs(u(x) - uBarra(x, xi, solucoes, h)) > erroMax:
            erroMax = abs(u(x) - uBarra(x, xi, solucoes, h))
            erroMaxUExato = u(x)
            erroMaxUBarra = uBarra(x, xi, solucoes, h)
    return erroMax, erroMaxUExato, erroMaxUBarra


def main():
    print("")
    print("Bem-vindo ao programa de Modelagem de um Sistema de Resfriamento de Chips escrito por Arthur Maia e Caio Balreira. \n")
    print("Neste programa, existem 3 funcionalidades:\n 1) Validação do Método dos Elementos Finitos \n 2) Equilíbrio com Forçantes de Calor \n 3) Equilíbrio com variação de material \n 0) Encerrar o programa \n")

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

            print(
                "Para a validação com k(x) = 1, q(x) = 0 e f(x) = 12x(1 - x) - 2, com intervalo [0, L]: \n")
            L = int(input("Insira o tamanho do chip (L): "))
            print("Analisando os erros máximos para diferentes valores de n:")

            for n in dimensoes:
                print(f"\n\nPara n = {n}:\n")
                solucoes = solveSystem(
                    lambda x, y: 12 * x * (1 - x) - 2, lambda x, y: 1, lambda x, y: 0, L, n, n10)
                erroMax, erroMaxUExato, erroMaxUBarra = biggestError(
                    solucoes, lambda x: x**2 * (1 - x)**2, n, L)
                print(
                    f" Valor do u barra: {erroMaxUBarra}\n Valor do u exato: {erroMaxUExato} \n Erro encontrado: {erroMax}")

            print(
                "\n\nPara a validação com k(x) = e^x, q(x) = 0 e f(x) = e^x + 1, com intervalo [0, L]: \n")
            print("Analisando os erros máximos para diferentes valores de n:")

            for n in dimensoes:
                print(f"\n\nPara n = {n}:\n")
                solucoes = solveSystem(
                    lambda x, y: e**x + 1, lambda x, y: e**x, lambda x, y: 0, L, n, n10)
                erroMax, erroMaxUExato, erroMaxUBarra = biggestError(
                    solucoes, lambda x: (x - 1)*(e**(-x) - 1), n, L)
                print(
                    f" Valor do u barra: {erroMaxUBarra}\n Valor do u exato: {erroMaxUExato} \n Erro encontrado: {erroMax}")
                print("")

        if (choice == 2):
            print(
                "Para o Equilíbrio com Forçantes de Calor no intervalo [0, L]: \n")

            L = int(input("Insira o tamanho do chip (L): "))
            print("Primeira situação: Q(x) = 1: \n")

            for n in dimensoes:
                print(f"Para n = {n}:\n")

                solucoes = solveSystem(
                    lambda x, y: 1, lambda x, y: 3.6, lambda x, y: 0, 1, n, n10)

                h = L/(n + 1)
                xi = [i * h for i in range(n + 2)]
                barras = list()
                for x in xi:
                    barras.append(uBarra(x, xi, solucoes, h))
                    print(
                        f"x = {x}; u barra = {uBarra(x, xi, solucoes, h)}")

                print("\n\n")
                plt.plot(xi, barras, label="$\overline{u}$")
                plt.title(f"Q(x) = 1 para n = {n}")
                plt.legend()
                plt.grid()
                plt.show()

            print("Segunda situação: Q(x) = -x^2: \n")

            for n in dimensoes:
                print(f"Para n = {n}:\n")

                solucoes = solveSystem(
                    lambda x, y: (-1)*(x**2), lambda x, y: 3.6, lambda x, y: 0, 1, n, n10)

                h = L/(n + 1)
                xi = [i * h for i in range(n + 2)]
                barras = list()
                for x in xi:
                    barras.append(uBarra(x, xi, solucoes, h))
                    print(
                        f"x = {x}; u barra = {uBarra(x, xi, solucoes, h)}")

                print("\n\n")
                plt.plot(xi, barras, label="$\overline{u}$")
                plt.title(f"Q(x) = -x^2 para n = {n}")
                plt.legend()
                plt.grid()
                plt.show()

            print("Terceira situação: Q(x) = sin(10x): \n")

            for n in dimensoes:
                print(f"Para n = {n}:\n")

                solucoes = solveSystem(
                    lambda x, y: np.sin(10*x), lambda x, y: 3.6, lambda x, y: 0, 1, n, n10)

                h = L/(n + 1)
                xi = [i * h for i in range(n + 2)]
                barras = list()
                for x in xi:
                    barras.append(uBarra(x, xi, solucoes, h))
                    print(
                        f"x = {x}; u barra = {uBarra(x, xi, solucoes, h)}")

                print("\n\n")
                plt.plot(xi, barras, label="$\overline{u}$")
                plt.title(f"Q(x) = sin(10x) para n = {n}")
                plt.legend()
                plt.grid()
                plt.show()

        if (choice == 3):
            print(
                "Para o Equilíbrio com Variação de Material no intervalo [0, L]: \n")

            L = int(input("Insira o tamanho do chip (L): "))
            d = np.float64(input("Insira o raio da parte de silício (d): "))
            ka = np.float64(
                input("Insira o parâmetro de condutividade térmica do material (k): "))

            def k(x, y, L, d):
                if (L/2 - d) < x < (L/2 + d):
                    return 3.6
                return ka

            print("Primeira situação: Q(x) = 1: \n")

            for n in dimensoes:
                print(f"Para n = {n}:\n")

                solucoes = solveSystem(
                    lambda x, y: 1, lambda x, y: k(x, y, L, d), lambda x, y: 0, L, n, n10)

                h = L/(n + 1)
                xi = [i * h for i in range(n + 2)]
                barras = list()
                for x in xi:
                    barras.append(uBarra(x, xi, solucoes, h))
                    print(
                        f"x = {x}; u barra = {uBarra(x, xi, solucoes, h)}")

                print("\n\n")
                plt.plot(xi, barras, label="$\overline{u}$")
                plt.title(f"Q(x) = 1 para n = {n}")
                plt.legend()
                plt.grid()
                plt.show()

            print("Segunda situação: Q(x) = -x^2: \n")

            for n in dimensoes:
                print(f"Para n = {n}:\n")

                solucoes = solveSystem(
                    lambda x, y: (-1)*(x**2), lambda x, y: k(x, y, L, d), lambda x, y: 0, L, n, n10)

                h = L/(n + 1)
                xi = [i * h for i in range(n + 2)]
                barras = list()
                for x in xi:
                    barras.append(uBarra(x, xi, solucoes, h))
                    print(
                        f"x = {x}; u barra = {uBarra(x, xi, solucoes, h)}")

                print("\n\n")
                plt.plot(xi, barras, label="$\overline{u}$")
                plt.title(f"Q(x) = -x^2 para n = {n}")
                plt.legend()
                plt.grid()
                plt.show()

            print("Terceira situação: Q(x) = sin(10x): \n")

            for n in dimensoes:
                print(f"Para n = {n}:\n")

                solucoes = solveSystem(
                    lambda x, y: np.sin(10*x), lambda x, y: k(x, y, L, d), lambda x, y: 0, L, n, n10)

                h = L/(n + 1)
                xi = [i * h for i in range(n + 2)]
                barras = list()
                for x in xi:
                    barras.append(uBarra(x, xi, solucoes, h))
                    print(
                        f"x = {x}; u barra = {uBarra(x, xi, solucoes, h)}")

                print("\n\n")
                plt.plot(xi, barras, label="$\overline{u}$")
                plt.title(f"Q(x) = sin(10x) para n = {n}")
                plt.legend()
                plt.grid()
                plt.show()

        if (choice == 0):
            print("Programa encerrado.", "\n")
            break

        print("Seguem as opções novamente: \n 1) Validação do Método dos Elementos Finitos \n 2) Equilíbrio com Forçantes de Calor \n 3) Equilíbrio com variação de material \n 0) Encerrar o programa \n")

    return 0


if __name__ == "__main__":
    main()
