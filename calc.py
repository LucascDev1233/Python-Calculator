operador = input('Qual operador você vai usar (+, -, *, /): ')
num = int(input('Digite um número:'))
num2 = int(input('Digite o segundo número:'))

if operador == '*':
    
    if num2 != 0:
        print(f"\nO resultado da MULTIPLICAÇÃO é =", num * num2)
    else:
        print("\nErro: não é possível multiplicar por zero!")



elif operador == '+':
    
    if num2 != 0:
        print(f"\nO resultado da ADIÇÃO é =", num + num2)
    else:
        print("\nErro: não é possível somar por zero!")



elif operador == '-':
    
    if num2 != 0:
        print(f"\nO resultado da Subtração é =", num - num2)
    else:
        print("\nErro: não é possível subtrair por zero!")



elif operador == '/':
    
    
    if num2 != 0:
        print(f"\nO resultado da DIVISÃO é =", num / num2)
    else:
        print("\nErro: não é possível dividir por zero!")
     
else:
    print('Operador inválido!')



    