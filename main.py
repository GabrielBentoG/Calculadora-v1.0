from funcoes import dados, mat

dados.titulo("CALCULADORA v1.0")

while True:
    num1 = int(input("Digite um número: "))
    dados.opc('Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Sair')
    esc = int(input("O que deseja fazer com o número? "))
    dados.linha(45)
    if esc == 1:
        # SOMA
        num2 = int(input("Digite outro número: "))
        mat.somar(num1, num2)
    elif esc == 2:
        # SUBTRAÇÃO
        num2 = int(input("Digite outro número: "))
        mat.subtrair(num1, num2)
    elif esc == 3:
        # MULTIPLICAÇÃO
        num2 = int(input("Digite outro número: "))
        mat.multiplicar(num1, num2)
    elif esc == 4:
        # DIVISÃO
        num2 = int(input("Digite outro número: "))
        mat.dividir(num1, num2)
    elif esc == 5:
        # ENCERRA O PROGRAMA
        print("OBRIGADO!".center(45))
        dados.linha(45)
        break
