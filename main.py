menu_inicial = """

    ====== MENU ======
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
    ==================

"""
saldo  = 0
limite = 500 #Valor limite por saque em R$ 
extrato = ""
n_saque = 0 #Numero de saque realizado
l_saque = 3 #Limite de saque diario

while True:
    opcao = input(menu_inicial)

    if opcao == "1": # Depositar
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor do depósito deve ser positivo.")


    elif opcao == "2": # Sacar
        valor_saque = float(input("Informe o valor do saque: "))

        if valor_saque > saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif valor_saque > limite:
            print("Operação falhou! O valor excede o limite de R$ 500,00 por saque.")

        elif n_saque >= l_saque:
            print("Operação falhou! Limite diário de 3 saques atingido.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            n_saque += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3": # Extrato
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")


    elif opcao == "0": # Sair
        print("Saindo...")
        break

    else:
        print("Opção Inválida, tente novamente...")

