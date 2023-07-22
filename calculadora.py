#calculadora de operações básicas 
continuar = 'x'
while continuar == 'x':

    print('calculadora.')
    print('1. Adição \n 2. subtração \n 3. Multiplicação \n 4.Divisão')
    opcao = int(input('Digite a opção: '))

    #calculadora de adição
    if opcao == 1:
        num1 = float(input('Digite o primeiro Número: '))
        num2 = float(input('Digite o segundo número: '))

        resultado = num1 + num2

        print(f'resultado: {resultado}')
        continuar = input('Precione x para continuar: ')

        #calculadora de subtração
    elif opcao == 2:
        num1 = float(input('Digite o primeiro Número: '))
        num2 = float(input('Digite o segundo número: '))

        resultado = num1 - num2

        print(f'resultado: {resultado}')
        continuar = input('Precione x para continuar: ')

    #calculadora de multiplicação
    elif opcao == 3:
        num1 = float(input('Digite o primeiro Número: '))
        num2 = float(input('Digite o segundo número: '))

        resultado = num1 * num2

        print(f'resultado: {resultado}')
        continuar = input('Precione x para continuar: ')

    #calculadora de divisão
    elif opcao == 4:
        num1 = float(input('Digite o primeiro Número: '))
        num2 = float(input('Digite o segundo número: '))
        if num2 != 0:
            resultado = num1 / num2
            print(f'resultado: {resultado}')
            continuar = input('Precione x para continuar: ')

        else:
            print('Erro, divisão por zero.')


    else:
        print('ERRO')