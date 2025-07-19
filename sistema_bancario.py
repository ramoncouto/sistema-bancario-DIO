menu = """
==== Seu Banco ====

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

===================
=> """

deposito = 0
saque = 0
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    while opcao not in "0123":
        print('Opção inválida. Por favor, escolha uma opção válida.')
        opcao = input(menu)
        
    
    if opcao == '1':
        deposito = int(input('Informe o valor do depósito: '))
        if deposito <= 0:
            print('Operação falhou! O valor informado é inválido.')
        else:
            confirma_deposito = input(f'Deseja depositar o valor de R$ {deposito:.2f}? [s/n] ')
            if confirma_deposito.lower() == 's':
                saldo += deposito
                extrato += f'Depósito: {deposito}\n'
    
    elif opcao == '2':
        saque = int(input('Informe o valor do saque: '))
        if saque <= 0:
            print('Operação falhou! O valor informado é inválido.')
        elif saque > saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif saque > limite:
            print('Operação falhou! O valor do saque excede o limite.')
        elif numero_saques == LIMITE_SAQUES:
            print('Operação falhou! Número máximo de saques excede o limite')
        else:
            confirma_saque = input(f'Deseja sacar o valor de R$ {saque:.2f}? [s/n] ')
            if confirma_saque.lower() == 's':
                saldo -= saque
                numero_saques += 1
                print(f'Você possui {LIMITE_SAQUES - numero_saques} saques disponíveis.')
                extrato += f'Saque: {saque}\n'

    elif opcao == '3':
        if not extrato:
            print('================ EXTRATO ================')
            print('Não foram realizadas movimentações.')
            print()
            print(f'Saldo: R$ {saldo:.2f}')
            print('=========================================')
        else:
            print('================ EXTRATO ================')
            print(extrato)
            print()
            print(f'Saldo: R$ {saldo:.2f}')
            print('=========================================')
            
    elif opcao == '0':
        print('O Seu Banco agradece sua preferência! Volte sempre!')
        break