#  Aqui pedimos o nome do usuário e para inserir um número
nome = input (f'Qual seria seu nome? ')
numero = input("Digite um número: ")

try: #Aqui convertemos a variavel para número inteiro
    numero = int(numero)
    # Aqui verificamos se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é par !")
    else:
         print("O número é ímpar !")
except ValueError: #Aqui colocamos um exceção para caso o usuário colocar algo fora de code
 print(f'Digite um número válido ')
