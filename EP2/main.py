def main():
    print("")
    print("Bem-vindo ao programa de integração numérica de Gauss escrito por Arthur Maia e Caio Balreira. \n")
    print("Neste programa, existem 5 funcionalidades:\n 1) Calcular os volumes do cubo cujas arestas tem comprimento 1 e do tetraedro com vértices em (0,0,0), (1,0,0), (0,1,0), (0,0,1) \n 2) Calcular a área A da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2 \n 3) Calcular a área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 \n 4) Volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1 \n 0) Encerrar o programa \n")

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
            pass

        if (choice == 2):
            pass

        if (choice == 3):
            pass

        if (choice == 4):
            pass

        if (choice == 0):
            print("Programa encerrado.", "\n")
            break

        print("Seguem as opções novamente: \n 1) Calcular os volumes do cubo cujas arestas tem comprimento 1 e do tetraedro com vértices em (0,0,0), (1,0,0), (0,1,0), (0,0,1) \n 2) Calcular a área A da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2 \n 3) Calcular a área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 \n 4) Volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1 \n 0) Encerrar o programa \n")


if __name__ == "__main__":
    main()
