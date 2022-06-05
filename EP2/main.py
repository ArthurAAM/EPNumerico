from math import e, pi

# nx = [(raiz, peso)]
n6 = [(-0.2386191860831969086305017, 0.4679139345726910473898703), (-0.6612093864662645136613996, 0.3607615730481386075698335), (-0.9324695142031520278123016, 0.1713244923791703450402961),
      (0.2386191860831969086305017, 0.4679139345726910473898703), (0.6612093864662645136613996, 0.3607615730481386075698335), (0.9324695142031520278123016, 0.1713244923791703450402961)]

n8 = [(-0.1834346424956498049394761, 0.3626837833783619829651504), (-0.5255324099163289858177390, 0.3137066458778872873379622), (-0.7966664774136267395915539, 0.2223810344533744705443560), (-0.9602898564975362316835609, 0.1012285362903762591525314),
      (0.1834346424956498049394761, 0.3626837833783619829651504), (0.5255324099163289858177390, 0.3137066458778872873379622), (0.7966664774136267395915539, 0.2223810344533744705443560), (0.9602898564975362316835609, 0.1012285362903762591525314)]

n10 = [(-0.1488743389816312108848260, 0.2955242247147528701738930), (-0.4333953941292471907992659, 0.2692667193099963550912269), (-0.6794095682990244062343274, 0.2190863625159820439955349), (-0.8650633666889845107320967, 0.1494513491505805931457763), (-0.9739065285171717200779640, 0.0666713443086881375935688),
       (0.1488743389816312108848260, 0.2955242247147528701738930), (0.4333953941292471907992659, 0.2692667193099963550912269), (0.6794095682990244062343274, 0.2190863625159820439955349), (0.8650633666889845107320967, 0.1494513491505805931457763), (0.9739065285171717200779640, 0.0666713443086881375935688)]


def parabolax(x):
    return 1 - x**2


def parabolay(y):
    return (1 - y)**0.5


def const0(x, y=None):
    return 0


def const1(x, y=None):
    return 1


def yTetraedro(x):
    return -1*x + 1


def zTetraedro(x, y):
    return 1 - x - y


def y0Exp(x):
    return x**3


def y1Exp(x):
    return x**2


def zExp(x, y):
    return e**(y/x)


def zExpArea(x, y):
    return ((e**(y/x) / x)**2 + (y*e**(y/x) / x**2)**2 + 1)**0.5


def Exp(x, y=None):
    return e**(-1*x**2)


def Circunferencia(x, y=None):
    return (1 - x**2)**0.5


def dupla(a, b, n, c, d, f):
    h1 = (b-a)/2
    h2 = (b+a)/2
    J = 0

    for i in range(len(n)):
        JX = 0
        r1 = n[i][0]
        w1 = n[i][1]
        x = h1*r1 + h2
        d1 = d(x)  # definir d(x) para cada exemplo
        c1 = c(x)  # definir c(x) para cada exemplo
        k1 = (d1 - c1)/2
        k2 = (d1 + c1)/2

        for j in range(len(n)):
            r2 = n[j][0]
            w2 = n[j][1]
            y = k1*r2 + k2
            Q = f(x, y)
            JX = JX + w2*Q

        J = J + w1*k1*JX

    J = h1*J
    return(J)


def main():
    print("")
    print("Bem-vindo ao programa de integração numérica de Gauss escrito por Arthur Maia e Caio Balreira. \n")
    print("Neste programa, existem 5 funcionalidades:\n 1) Calcular o volume do cubo cujas arestas tem comprimento 1 e o do tetraedro com vértices em (0,0,0), (1,0,0), (0,1,0), (0,0,1) \n 2) Calcular a área A da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2 \n 3) Calcular a área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 \n 4) Volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1 \n 0) Encerrar o programa \n")

    while True:
        while True:
            try:
                choice = int(
                    input("Escolha a funcionalidade que deseja executar: "))
                print("")
                if (choice < 0 or choice > 4):
                    raise ValueError()
                break
            except ValueError:
                print("Esta funcionalidade não é válida. Por favor, tente outra \n")

        if (choice == 1):
            print(dupla(0, 1, n10, const0, const1, const1))
            print(dupla(0, 1, n10, const0, yTetraedro, zTetraedro))

        if (choice == 2):
            print(dupla(0, 1, n10, const0, parabolax, const1))
            print(dupla(0, 1, n10, const0, parabolay, const1))

        if (choice == 3):
            print(dupla(0.1, 0.5, n10, y0Exp, y1Exp, zExp))
            print(dupla(0.1, 0.5, n10, y0Exp, y1Exp, zExpArea))

        if (choice == 4):
            print(2*pi*dupla(-1, 1, n10, const0, Exp, Exp))
            print(2*pi*dupla(0.75, 1, n10, const0, Circunferencia, Circunferencia))

        if (choice == 0):
            print("Programa encerrado.", "\n")
            break

        print("Seguem as opções novamente: \n 1) Calcular o volume do cubo cujas arestas tem comprimento 1 e o do tetraedro com vértices em (0,0,0), (1,0,0), (0,1,0), (0,0,1) \n 2) Calcular a área A da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2 \n 3) Calcular a área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 \n 4) Volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1 \n 0) Encerrar o programa \n")


if __name__ == "__main__":
    main()
