from datetime import datetime
import os
import json
from tinydb import TinyDB, Query

class Conta:
    def __init__(self):
        self.diretorio_pai = os.path.dirname(os.path.abspath(__file__))
        caminho_banco_dados = os.path.join(os.path.dirname(self.diretorio_pai), 'banco_de_dados.json')
        self.db = TinyDB(caminho_banco_dados)

    # def criar_conta(self, cliente):
    #     self.db.insert({'cpf': cliente.cpf, 'nome': cliente.nome, 'conta': cliente.numero_conta})

    # def apagar_conta(self, cliente):
    #     self.db.remove((Query().cpf == cliente.cpf) & (Query().conta == cliente.numero_conta))

class Gerente:
    def aprovar_conta(self, cliente):
        if cliente.renda >= 450:
            return True
        else:
            return False

    def aprovar_credito(self, cliente):
        if cliente.renda * 5 <= cliente.valor_solicitado:
            return True
        else:
            return False

    def excluir_conta(self, conta):
        conta.apagar_conta()

class Transacoes:
    def __init__(self):
        self.diretorio_pai = os.path.dirname(os.path.abspath(__file__))
        caminho_banco_dados = os.path.join(os.path.dirname(self.diretorio_pai), 'banco_de_dados.json')
        self.db = TinyDB(caminho_banco_dados)
    
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

        # Recupera as transações existentes do banco de dados e cria uma nova transação
        transacoes = self.db.get(doc_id=conta_origem)['transacoes'] 
        nova_transacao = {
            'data': data_atual,
            'tipo': tipo,
            'valor': valor,
            'conta_origem': conta_origem,
            'conta_destino': conta_destino
        }
        
        # Verifica se transacoes é uma lista e add a nova transação à lista
        if isinstance(transacoes, list):
            transacoes.append(nova_transacao)
        else:
            # Converte a string em uma lista vazia e add a nova transação
            transacoes = json.loads(transacoes) if transacoes else []
            transacoes.append(nova_transacao)
        # Converte em string
        transacoes_str = json.dumps(transacoes)
        # Atualiza o valor no banco de dados
        self.db.update({'transacoes': transacoes}, doc_ids=[conta_origem])


    def extrato(self, conta):
        return self.db.search((Query().conta_origem == conta) | (Query().conta_destino == conta))

    # SAQUE OK #
    def saque(self, conta, valor):
        cliente = self.db.get(doc_id=conta)
        saldo = cliente['saldo']

        if saldo >= valor and valor != 0:
            novo_saldo = saldo - valor
            novo_saldo = round(novo_saldo, 2)
            # print(novo_saldo, saldo, valor)
            self.registrar_transacao('saque', valor, conta_origem=conta)
            self.db.update({'saldo': novo_saldo}, doc_ids=[conta])
            return True
        else:
            return False

    # DEPOSITO OK #
    def deposito(self, conta, valor):
        cliente = self.db.get(doc_id=conta)
        saldo = cliente['saldo']

        if valor > 0:
            novo_saldo = saldo + valor
            novo_saldo = round(novo_saldo, 2)
            # print(novo_saldo, saldo, valor)
            self.registrar_transacao('deposito', valor, conta_origem=conta)
            self.db.update({'saldo': novo_saldo}, doc_ids=[conta])
            return True
        else:
            return False


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

