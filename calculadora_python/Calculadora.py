while True:
    Resultado, Valor1, Valor2 = int(0), int(0), int(0)

    try:
        print("Digite um valor:")
        Valor1 = int(input())
        print("Digite o segundo valor:")
        Valor2 = int(input())
    except ValueError:
        print("Erro: você precisa digitar um número inteiro. Tente novamente.")
        continue

    print("Escolha uma operação:\n 1: Adição\n 2: Subtração\n 3: Divisão\n 4: Multiplicação\n 5: Potenciação\n 6: Mod\n 0: Sair")

    try:
        Operacao = int(input())
    except ValueError:
        print("Erro: você precisa digitar um número inteiro para a operação. Tente novamente.")
        continue

    if Operacao == 1:
        Resultado = Valor1 + Valor2
        print(f"A soma de {Valor1} + {Valor2} é igual a: {Resultado}")
    
    elif Operacao == 2:
        Resultado = Valor1 - Valor2
        print(f"A subtração de {Valor1} - {Valor2} é igual a: {Resultado}")

    elif Operacao == 3:
        try:
            Resultado = Valor1 / Valor2
            print(f"A divisão de {Valor1} / {Valor2} é igual a: {Resultado}")
        except ZeroDivisionError:
            print("Erro: divisão por zero não é permitida.")
    
    elif Operacao == 4:
        Resultado = Valor1 * Valor2
        print(f"A multiplicação de {Valor1} por {Valor2} é igual a: {Resultado}")
        
    elif Operacao == 5:
        Resultado = pow(Valor1, Valor2)
        print(f"A potência de {Valor1} por {Valor2} é igual a: {Resultado}")
        
    elif Operacao == 6:
        try:
            Resultado = Valor1 % Valor2
            print(f"O mod de {Valor1} / {Valor2} é igual a: {Resultado}")
        except ZeroDivisionError:
            print("Erro: não é possível calcular o mod por zero.")
        
    elif Operacao == 0:
        print("Encerrando a calculadora. Até mais!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")