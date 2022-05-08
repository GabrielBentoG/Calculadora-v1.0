from funcoes import dados


def somar(a, b):
    """
    Realiza a soma das variaveis a e b

    :param a: Primeiro número
    :param b: Segundo número
    :return: a + b
    """
    dados.linha(45)
    print(f"Resultado: {a+b}")
    dados.linha(45)


def subtrair(a, b):
    """
    Subtrai b da variavel a

    :param a: Primeiro número
    :param b: Segundo número
    :return: a - b
    """
    dados.linha(45)
    print(f"Resultado: {a - b}")
    dados.linha(45)


def multiplicar(a, b):
    """
    Multiplica a por b

    :param a: Primeiro número
    :param b: Segundo número
    :return: a * b
    """
    dados.linha(45)
    print(f"Resultado: {a * b}")
    dados.linha(45)


def dividir(a, b):
    """
    Divide a por b

    :param a: Primeiro número
    :param b: Segundo número
    :return: a / b
    """
    dados.linha(45)
    print(f"Resultado: {a / b}")
    dados.linha(45)