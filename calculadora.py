while True:
    numero_valido1 = None
    numero_valido2 = None
    num_1_float = 0
    num_2_float = 0
    print(f'{'-'*10}Calculadora Simples by hasaryo{'-'*10}')
    numero_1 = input('Digite um número: ')
    try:
        num_1_float = float(numero_1)
        numeros_valido1 = True
    except:
        if numero_valido1 is None:
            print('O número digitado é inválido.')
            continue
    numero_2 = input('Digite outro número: ')
    try:
        num_2_float = float(numero_2)
        numeros_valido2 = True
    except:
        if numero_valido2 is None:
            print('O segundo número digitado é inválido.')
            continue

    operador = input('Digite o operador (+-/x): ')
    if operador == 'x':
        operador = '*'


    operadores_perm = '+-/*'
    if operador not in operadores_perm:
        print('O operador é inválido. ')
    if len(operador) > 1:
        print('Digite somente um operador. ')
    
    if operador == '+':
        print(f'O resultado de {numero_1} + {numero_2} é {num_1_float + num_2_float}')

    elif operador == '-':
        print(f'O resultado de {numero_1} - {numero_2} é {num_1_float - num_2_float}')
    
    elif operador == '*':
        print(f'O resultado de {numero_1} x {numero_2} é {num_1_float * num_2_float}')
    
    elif operador == '/':
        if num_2_float == 0:
            print('Indefinido.')
        else:
            print(f'O resultado de {numero_1} / {numero_2} é {num_1_float / num_2_float}')
        ###########


    sair = input('Quer sair? [s]im: ').lower().startswith('s')
   
    if sair is True:
        break
