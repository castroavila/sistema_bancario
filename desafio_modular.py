#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[i] Aumentar limite saques
[nu] Cadastrar novo usuário
[nc] Cadastrar conta
[lc] Listar contas cadastradas
[q] Sair

=> """


def depositar(saldo, valor, depositos, movimentos, /):
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        movimentos = True

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, depositos, movimentos


def sacar(*, saldo, valor, numero_saques, saques, limite, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

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
    return saldo, numero_saques


def extrato(
    saldo, /, *, depositos, saques, numero_saques, movimentos, limite_saques
):
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
    print(f"Numero máximo de saques: {limite_saques}")
    print("==========================================")


def atualizar_limite_saques(novo_limite):
    LIMITE_SAQUES = novo_limite
    print(f'Número maximo de saques atualizado para: {LIMITE_SAQUES}')
    return LIMITE_SAQUES


def cadastrar_usuario(usuarios):
    cpf = input("Informe CPF (somente números):")
    if cpf in usuarios:
        print("CPF já cadastrado")
        return
    nome = input("Informe nome completo:")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaaa):")
    endereco = input(
        "Informe endereco completo (logradouro, # -- bairro - cidade/sigla de estado):"
    )
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "agencia": None,
        "contas": [],
    }
    print("*****Usuario cadastrado com sucesso***********")
    print("**********************************************")


def criar_conta(agencia, cpf, usuarios):

    if cpf not in usuarios:
        print(f'Usuario com cpf: {cpf} nao está cadastrado!!')
        return
    numero_conta = len(usuarios[cpf]["contas"]) + 1
    usuarios[cpf]["agencia"] = agencia
    usuarios[cpf]["contas"].append(numero_conta)
    print("****Conta associada com sucesso******************")
    print("*************************************************")


def listar_contas(usuarios):
    if not usuarios:
        print("Sem usuarios cadastrados")
        return

    for cpf in usuarios:
        contas = usuarios[cpf]["contas"]
        print("****************************************")
        print(f'Titular:\t {usuarios[cpf]["nome"]}')
        print(f'CPF:\t {usuarios[cpf]["cpf"]}')
        print(
            f'C/C:\t {", ".join([str(i) for i in contas]) if len(contas)>0 else "Nenhuma" }'
        )


def main():
    saldo = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = {}
    AGENCIA = "0001"

    depositos = []
    saques = []
    movimentos = False
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, depositos, movimentos = depositar(
                saldo, valor, depositos, movimentos
            )

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                numero_saques=numero_saques,
                saques=saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "i":
            atualizar_numero_saques = int(
                input('Novo numero máximo de saques: ')
            )
            LIMITE_SAQUES = atualizar_limite_saques(atualizar_numero_saques)
        elif opcao == "e":
            extrato(
                saldo,
                depositos=depositos,
                saques=saques,
                numero_saques=numero_saques,
                movimentos=movimentos,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            cpf = input("Informe CPF do usuario para associar conta:")
            criar_conta(AGENCIA, cpf, usuarios)
        elif opcao == "lc":
            listar_contas(usuarios)

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
