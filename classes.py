#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @author	   : Manuel Castro Avila <castroavila@ic.unicamp.br>
# @file	   	   : classes.py
# @created	   : 27-Aug-2025
# @company 	   : Institute of Computing - UNICAMP - Campinas - Brazil

""" """

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Transacao(ABC):
    """Docstring for Transacao."""

    @abstractclassmethod
    def registrar(self, conta):
        """TODO: Docstring for registrar.

        Parameters
        ----------
        conta : TODO

        Returns
        -------
        TODO

        """
        pass

    @property
    @abstractproperty
    def valor(self):
        """TODO: Docstring for valor.
        Returns
        -------
        TODO

        """
        pass


class Saque(Transacao):
    """Docstring for Saque."""

    def __init__(self, valor):
        """TODO: to be defined.

        Parameters
        ----------
        valor : TODO


        """

        self.valor = valor

    @property
    def valor(self):
        """TODO: Docstring for valor.
        Returns
        -------
        TODO

        """
        return self.valor

    def registrar(self, conta):
        """TODO: Docstring for registrar.

        Parameters
        ----------
        conta : TODO

        Returns
        -------
        TODO

        """
        executou = conta.sacar(self.valor)
        if executou:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """Docstring for Deposito."""

    def __init__(self, valor):
        """TODO: to be defined.

        Parameters
        ----------
        valor : TODO


        """

        self.valor = valor

    @property
    def valor(self):
        """TODO: Docstring for valor.
        Returns
        -------
        TODO

        """
        return self.valor

    def registrar(self, conta):
        """TODO: Docstring for registrar.

        Parameters
        ----------
        conta : TODO

        Returns
        -------
        TODO

        """
        executou = conta.depositar(self.valor)
        if executou:
            conta.historico.adicionar_transacao(self)


class Cliente:
    """Docstring for Cliente."""

    def __init__(self, endereco):
        """TODO: to be defined.

        Parameters
        ----------
        endereco : TODO


        """

        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """TODO: Docstring for realizar_transacao.

        Parameters
        ----------
        conta : TODO
        transacao : TODO

        Returns
        -------
        TODO

        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """TODO: Docstring for adicionar_con.

        Parameters
        ----------
        arg1 : TODO

        Returns
        -------
        TODO

        """
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """Docstring for PessoaFisica."""

    def __init__(self, cpf, nome, data_nascimento, endereco):
        """TODO: to be defined.

        Parameters
        ----------
        cpf : TODO
        nome : TODO
        data_nascimento : TODO


        """
        super().__init__(endereco)

        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Historico:
    """Docstring for Historico."""

    def __init__(self):
        """TODO: Docstring for __init__.
        Returns
        -------
        TODO

        """
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        """TODO: Docstring for adicionar_transacao.

        Parameters
        ----------
        transacao : TODO

        Returns
        -------
        TODO

        """
        self.transacoes.append(
            {
                "tipo": transacao.__class__._name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Conta:
    """Docstring for Conta."""

    def __init__(self, numero, cliente):
        """TODO: to be defined.

        Parameters
        ----------
        numero : TODO
        cliente : TODO


        """

        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        """TODO: Docstring for saldo.
        Returns
        -------
        TODO

        """
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        """TODO: Docstring for nova_conta.

        Parameters
        ----------
        cliente : TODO
        numero : TODO

        Returns
        -------
        TODO

        """
        return cls(cliente, numero)

    def sacar(self, valor):
        """TODO: Docstring for sacar.

        Parameters
        ----------
        valor : TODO

        Returns
        -------
        TODO

        """
        saldo = self.saldo
        if valor < 0:
            print("Valor a sacar não pode ser negativo")
        excedeu_limite = valor > saldo

        if excedeu_limite:
            print(
                "A transação não é possivel: valor a sacar maior que o saldo disponível."
            )
        else:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        """TODO: Docstring for depositar.

        Parameters
        ----------
        valor : TODO

        Returns
        -------
        TODO

        """
        if valor > 0:
            self.saldo = +valor
            print("Depósito feito")
            return True
        else:
            print("Valor a depositar não pode ser negativo")
            return False


class ContaCorrente(Conta):
    """Docstring for ContaCorrente."""

    def __init__(self, numero, cliente, limite=1000, limite_saques=3):
        """TODO: Docstring for __init__.

        Parameters
        ----------
        numero : TODO
        cliente : TODO
        limite : TODO, optional
        limite_saques : TODO, optional

        Returns
        -------
        TODO

        """
        super().__init__(numero, cliente)

        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        """TODO: Docstring for sacar.

        Parameters
        ----------
        valor : TODO

        Returns
        -------
        TODO

        """
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print("Valor a sacar maior que o limite permitido")
        elif excedeu_saques:
            print("Excedeu número de saques")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        """TODO: Docstring for __str__.
        Returns
        -------
        TODO

        """
        return f"""
        Dados de conta:
        Agencia : {self.agencia}
        # Conta: {self.numero}
        Cliente: {self.cliente.nome}
        """
