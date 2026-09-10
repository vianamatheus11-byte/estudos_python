


n1 = int(input("Digite um número: "))
print ('escolha uma das opções abaixo: ')
operacao = int(input('1 - Somar \n2 - Subtrair \n3 - Multiplicar \n4 - Dividir  '))

n2 = int(input("Digite outro número: "))

if operacao == 1:
    resultado = n1 + n2
    print("O resultado da soma é: ", resultado)

if operacao == 2:
    resultado = n1 - n2
    print("O resultado da subtração é: ", resultado)

if operacao == 3:
    resultado = n1 * n2
    print("O resultado da multiplicação é: ", resultado)        

if operacao == 4:
    resultado = n1 / n2
    print("O resultado da divisão é: ", resultado)

    
                     
                     