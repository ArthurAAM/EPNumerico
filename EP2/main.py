from math import e, pi

# nx = [(raiz, peso)]
n6 = [(-0.2386191860831969086305017, 0.4679139345726910473898703), (-0.6612093864662645136613996, 0.3607615730481386075698335), (-0.9324695142031520278123016, 0.1713244923791703450402961),
      (0.2386191860831969086305017, 0.4679139345726910473898703), (0.6612093864662645136613996, 0.3607615730481386075698335), (0.9324695142031520278123016, 0.1713244923791703450402961)]

n8 = [(-0.1834346424956498049394761, 0.3626837833783619829651504), (-0.5255324099163289858177390, 0.3137066458778872873379622), (-0.7966664774136267395915539, 0.2223810344533744705443560), (-0.9602898564975362316835609, 0.1012285362903762591525314),
      (0.1834346424956498049394761, 0.3626837833783619829651504), (0.5255324099163289858177390, 0.3137066458778872873379622), (0.7966664774136267395915539, 0.2223810344533744705443560), (0.9602898564975362316835609, 0.1012285362903762591525314)]

n10 = [(-0.1488743389816312108848260, 0.2955242247147528701738930), (-0.4333953941292471907992659, 0.2692667193099963550912269), (-0.6794095682990244062343274, 0.2190863625159820439955349), (-0.8650633666889845107320967, 0.1494513491505805931457763), (-0.9739065285171717200779640, 0.0666713443086881375935688),
       (0.1488743389816312108848260, 0.2955242247147528701738930), (0.4333953941292471907992659, 0.2692667193099963550912269), (0.6794095682990244062343274, 0.2190863625159820439955349), (0.8650633666889845107320967, 0.1494513491505805931457763), (0.9739065285171717200779640, 0.0666713443086881375935688)]


def zExpArea(x, y):
    return ((e**(y/x) / x)**2 + (y*e**(y/x) / x**2)**2 + 1)**0.5


def dupla(a, b, n, c, d, f):
    h1 = (b-a)/2
    h2 = (b+a)/2
    J = 0

    for i in range(len(n)):
        JX = 0
        r1 = n[i][0]
        w1 = n[i][1]
        x = h1*r1 + h2
        c1 = c(x)  # definir c(x) para cada exemplo
        d1 = d(x)  # definir d(x) para cada exemplo
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
    print("Neste programa, existem 5 funcionalidades:\n 1) Calcular o volume do cubo cujas arestas tem comprimento 1 e o do tetraedro com vértices em (0,0,0), (1,0,0), (0,1,0), (0,0,1) \n 2) Calcular a área da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2 \n 3) Calcular a área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 \n 4) Calcular o volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1 \n 0) Encerrar o programa \n")

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
            volume_cubo = [dupla(0, 1, n6, lambda x: 0, lambda x: 1, lambda x, y: 1), dupla(
                0, 1, n8, lambda x: 0, lambda x: 1, lambda x, y: 1), dupla(0, 1, n10, lambda x: 0, lambda x: 1, lambda x, y: 1)]

            volume_tetraedro = [dupla(0, 1, n6, lambda x: 0, lambda x: (-1) * x + 1, lambda x, y: 1 - x - y), dupla(0, 1, n8, lambda x: 0,
                                                                                                                    lambda x: (-1) * x + 1, lambda x, y: 1 - x - y), dupla(0, 1, n10, lambda x: 0, lambda x: (-1) * x + 1, lambda x, y: 1 - x - y)]

            print(
                f"O volume do cubo é: \n\tPara n6: {volume_cubo[0]} u.v. \n\tPara n8: {volume_cubo[1]} u.v. \n\tPara n10: {volume_cubo[2]} u.v. \n\tValor esperado: 1 u.v. \n")

            print(
                f"O volume do tetraedro é: \n\tPara n6: {volume_tetraedro[0]} u.v. \n\tPara n8: {volume_tetraedro[1]} u.v. \n\tPara n10: {volume_tetraedro[2]} u.v. \n\tValor esperado: 0.16666666... u.v. \n")

        if (choice == 2):
            limite_x = [dupla(0, 1, n6, lambda x: 0, lambda x: 1 - x**2, lambda x, y: 1), dupla(0, 1, n8, lambda x: 0,
                                                                                                lambda x: 1 - x**2, lambda x, y: 1), dupla(0, 1, n10, lambda x: 0, lambda x: 1 - x**2, lambda x, y: 1)]

            limite_y = [dupla(0, 1, n6, lambda x: 0, lambda y: (1 - y)**0.5, lambda x, y: 1), dupla(0, 1, n8, lambda x: 0,
                                                                                                    lambda y: (1 - y)**0.5, lambda x, y: 1), dupla(0, 1, n10, lambda x: 0, lambda y: (1 - y)**0.5, lambda x, y: 1)]

            print(
                f"A área em baixo da parábola, para o limite de 1 - x^2, no intervalo pedido é: \n\tPara n6: {limite_x[0]} u.v. \n\tPara n8: {limite_x[1]} u.v. \n\tPara n10: {limite_x[2]} u.v. \n\tValor esperado: 0.6666666... u.v. \n")

            print(
                f"A área em baixo da parábola, para o limite de √(1 - y), no intervalo pedido é: \n\tPara n6: {limite_y[0]} u.v. \n\tPara n8: {limite_y[1]} u.v. \n\tPara n10: {limite_y[2]} u.v. \n\tValor esperado: 0.6666666... u.v. \n")

        if (choice == 3):
            volume = [dupla(0.1, 0.5, n6, lambda x: x**3, lambda x: x**2, lambda x, y: e**(y/x)), dupla(0.1, 0.5, n8, lambda x: x **
                                                                                                        3, lambda x: x**2, lambda x, y: e**(y/x)), dupla(0.1, 0.5, n10, lambda x: x**3, lambda x: x**2, lambda x, y: e**(y/x))]

            area = [dupla(0.1, 0.5, n6, lambda x: x**3, lambda x: x**2, zExpArea), dupla(0.1, 0.5, n8, lambda x: x **
                                                                                         3, lambda x: x**2, zExpArea), dupla(0.1, 0.5, n10, lambda x: x**3, lambda x: x**2, zExpArea)]

            print(
                f"O volume em baixo da superfície no intervalo pedido é: \n\tPara n6: {volume[0]} u.v. \n\tPara n8: {volume[1]} u.v. \n\tPara n10: {volume[2]} u.v. \n\tValor esperado: 0.0333055661162 u.v. \n")

            print(
                f"A área dá superfície no intervalo pedido é: \n\tPara n6: {area[0]} u.a. \n\tPara n8: {area[1]} u.a. \n\tPara n10: {area[2]} u.a. \n\tValor esperado: 0.105497882401 u.a. \n")

        if (choice == 4):
            calota = [2*pi*dupla(0.75, 1, n6, lambda x: 0, lambda x: (1 - x**2)**0.5, lambda x, y: y), 2*pi*dupla(0.75, 1, n8, lambda x: 0,
                                                                                                                  lambda x: (1 - x**2)**0.5, lambda x, y: y), 2*pi*dupla(0.75, 1, n10, lambda x: 0, lambda x: (1 - x**2)**0.5, lambda x, y: y)]

            curva = [2*pi*dupla(-1, 1, n6, lambda x: 0, lambda x: e**(-1*x**2), lambda x, y: y), 2*pi*dupla(-1, 1, n8, lambda x: 0,
                                                                                                            lambda x: e**(-1*x**2), lambda x, y: y), 2*pi*dupla(-1, 1, n10, lambda x: 0, lambda x: e**(-1*x**2), lambda x, y: y)]

            print(
                f"O volume da calota esférica é: \n\tPara n6: {calota[0]} u.v. \n\tPara n8: {calota[1]} u.v. \n\tPara n10: {calota[2]} u.v. \n\tValor esperado: 0.179987079112 u.v. \n")

            print(
                f"O volume da calota esférica é: \n\tPara n6: {curva[0]} u.v. \n\tPara n8: {curva[1]} u.v. \n\tPara n10: {curva[2]} u.v. \n\tValor esperado: 3.75824963423 u.v. \n")

        if (choice == 0):
            print("Programa encerrado.", "\n")
            break

        print("Seguem as opções novamente: \n 1) Calcular o volume do cubo cujas arestas tem comprimento 1 e o do tetraedro com vértices em (0,0,0), (1,0,0), (0,1,0), (0,0,1) \n 2) Calcular a área da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2 \n 3) Calcular a área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 \n 4) Calcular o volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1 \n 0) Encerrar o programa \n")


if __name__ == "__main__":
    main()
