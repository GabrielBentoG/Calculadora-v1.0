def linha(a):
    """
    Cria uma linha no terminal


    :param a: Tamanho da linha
    :return: Linha vezes o tamanho
    """
    print("-"*a)


def titulo(msg):
    """
    Cria um título com uma mensagem
    :param msg: Mensagem do título
    :return: Título
    """
    linha(45)
    print(f"{msg}".center(45))
    linha(45)

def opc(*opc):
    """
    Essa função exibe na tela as opções da calculadora.
    :param opc: funções da calculadora
    :return: função escolhida
    """

    linha(45)
    for c in range(0, len(opc)):
        print(f"{c + 1} - {opc[c]}")



