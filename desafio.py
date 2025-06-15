#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[i] Aumentar limite saques
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

depositos = []
saques = []
movimentos = False
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            depositos.append(valor)
            movimentos = True

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            saques.append(valor)
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "i":
        atualizar_numero_saques = int(input('Novo numero máximo de saques: '))
        LIMITE_SAQUES = atualizar_numero_saques
        print(f'Número maximo de saques atualizado para: {LIMITE_SAQUES}')
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if movimentos:
            if len(depositos) > 0:
                print('........Depositos...........')
                for i, deposito in enumerate(depositos):
                    print(f'Deposito {i+1}: R$: {deposito:0.2f}')
            if len(saques) > 0:
                print('........Saques...........')
                for i, saque in enumerate(saques):
                    print(f'Saque {i+1}: R$: {saque:0.2f}')
        else:
            print("Não foram realizadas movimentações.")

        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Número de saques até agora: {numero_saques}")
        print(f"Numero máximo de saques: {LIMITE_SAQUES}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print(
            "Operação inválida, por favor selecione novamente a operação desejada."
        )
