from datetime import datetime
from tinydb import TinyDB, Query

class Conta:
    def __init__(self):
        self.db = TinyDB('banco.db')

    def criar_conta(self, cliente):
        self.db.insert({'cpf': cliente.cpf, 'nome': cliente.nome, 'conta': cliente.numero_conta})

    def apagar_conta(self, cliente):
        self.db.remove((Query().cpf == cliente.cpf) & (Query().conta == cliente.numero_conta))

class Gerente:
    def aprovar_credito(self, cliente):
        if cliente.renda * 5 <= cliente.valor_solicitado:
            return True
        else:
            return False

    def excluir_conta(self, conta):
        conta.apagar_conta()

class Transacoes:
    def __init__(self):
        self.db = TinyDB('banco.db')

    def verificar_debitos(self, cliente):
        data_atual = datetime.now().date()
        debitos = self.db.search((Query().conta_origem == cliente.numero_conta) & (Query().tipo == 'credito'))
        for debito in debitos:
            data_transacao = datetime.strptime(debito['data'], "%d/%m/%Y %H:%M:%S").date()
            if data_transacao <= data_atual:
                valor_parcela = debito['valor'] / cliente.qtd_parcelas
                self.registrar_transacao('retirada', valor_parcela, conta_origem=cliente.numero_conta)

    def registrar_transacao(self, tipo, valor, conta_origem=None, conta_destino=None):
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.db.insert({'data': data_atual, 'tipo': tipo, 'valor': valor, 'conta_origem': conta_origem, 'conta_destino': conta_destino})

    def extrato(self, conta):
        return self.db.search((Query().conta_origem == conta) | (Query().conta_destino == conta))

    def saque(self, conta, valor):
        # Verifica o saldo antes de fazer o saque
        saldo = self.calcular_saldo(conta)
        if saldo >= valor:
            self.registrar_transacao('saque', valor, conta_origem=conta)
            return True
        else:
            return False

    def deposito(self, conta, valor):
        self.registrar_transacao('deposito', valor, conta_destino=conta)

    def calcular_saldo(self, conta):
        saldo = 0
        for transacao in self.db:
            if transacao['conta_origem'] == conta:
                saldo -= transacao['valor']
            if transacao['conta_destino'] == conta:
                saldo += transacao['valor']
        return saldo

    def realizar_pagamento(self, conta_origem, conta_destino, valor, agendar=False):
        if agendar:
            self.registrar_transacao('agendamento', valor, conta_origem=conta_origem, conta_destino=conta_destino)
        else:
            saldo = self.calcular_saldo(conta_origem)
            if saldo >= valor:
                self.registrar_transacao('pagamento', valor, conta_origem=conta_origem, conta_destino=conta_destino)
                return True
            else:
                return False
            
class Cliente:
    def __init__(self, cpf, nome, telefone, endereco, data_nascimento, renda):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.renda = renda
    
    def solicita_aprovacao(self, gerente):
        resultado = gerente.aprovar_conta(self)
        return resultado
    
class SolicitaCredito:
    def __init__(self, valor_solicitado, renda, qtd_parcelas):
        self.valor_solicitado = valor_solicitado
        self.renda = renda
        self.qtd_parcelas = qtd_parcelas
        self.resultado = None

    def requisitar_emprestimo(self, gerente):
        self.resultado = gerente.aprovar_credito(self)

