print('\n <<------Calculadora Simples----->>')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Presione a tecla "s" para encerra o programa!')


# (\n) faz uma quebra de linha
while True:
    op = input('\n Qual operação deseja fazer? ')
    if op == '+' or op =='-' or op =='*' or op =='/':
        x = float(input('Digite o primeiro número:'))
        y = float(input('Digite o segundo número:'))

    if (op == '+'):
        res = x + y
        print('\n Resultado: {} + {} = {}'.format(x, y, res))
        continue
    elif (op == '-'):
        res = x - y
        print('\n Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('\n Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('\n Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif (op == 's'):
        break
    else:
        print('\n Operação invalida!')


print('\n Encerrando o programa...!')