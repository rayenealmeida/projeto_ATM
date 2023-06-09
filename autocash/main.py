import os, subprocess, tkinter as tk
from tkinter import ttk, messagebox
from library.module import Transacoes, SolicitaCredito, VerificarBanco
from PIL import ImageTk, Image
from tinydb import TinyDB, Query
import tkinter.messagebox as messagebox
from datetime import datetime, timedelta


class AutocashApp:
    def __init__(self):
        self.diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.db = TinyDB(self.diretorio_atual + '/banco_de_dados.json')

        self.janela = tk.Tk()
        self.janela.geometry("600x600")
        self.janela.title("Caixa Eletrônico")
        self.janela.resizable(False, False)

        imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
        imagem_tk = ImageTk.PhotoImage(imagem)
        label = tk.Label(self.janela, image=imagem_tk).place(x=0, y=0, relwidth=1, relheight=1)

        ######################################
        #         INÍCIO DAS FUNÇÕES         #
        ######################################

        def botoes():
            button_1 = tk.Button(self.janela, text= '1', width=2).place(x=113, y=404)
            button_2 = tk.Button(self.janela, text= '2', width=2).place(x=166, y=404)
            button_3 = tk.Button(self.janela, text= '3', width=2).place(x=219, y=404)
            button_4 = tk.Button(self.janela, text= '4', width=2).place(x=113, y=440)
            button_5 = tk.Button(self.janela, text= '5', width=2).place(x=166, y=440)
            button_6 = tk.Button(self.janela, text= '6', width=2).place(x=219, y=440)
            button_7 = tk.Button(self.janela, text= '7', width=2).place(x=113, y=476)
            button_8 = tk.Button(self.janela, text= '8', width=2).place(x=166, y=476)
            button_9 = tk.Button(self.janela, text= '9', width=2).place(x=219, y=476)
            button_0 = tk.Button(self.janela, text= '0', width=2).place(x=166, y=512)            

        # INÍCIO DA FUNÇÃO REALIZAR CADASTRO: OK #
        def realizar_cadastro():
            subprocess.run(['python', self.diretorio_atual +'/cadastro.py'])

        # INÍCIO DA FUNÇÃO LOGIN: OK #
        def fazer_login():
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)

            def mudar_imagem():
                imagem_original = Image.open(self.diretorio_atual + "/images/atm_bg_insere_cartao.png")
                nova_imagem = imagem_original.resize((600, 600))
                nova_imagem = ImageTk.PhotoImage(nova_imagem)
                label.config(image=nova_imagem)
                label.image = nova_imagem    
            mudar_imagem()

            def logar():
                cpf = entry_cpf_login.get()
                senha = entry_senha.get()
                
                for indice, cliente in enumerate(self.db.all()):
                    if cliente['cpf_ou_cnpj'] == cpf and cliente['senha'] == senha and cliente['solicita_exclusao'] == 0:
                        label_cliente['text'] = 'Login realizado com sucesso!'
                        label_cliente['bg'] = '#5FC0E6'
                        cliente_id = indice+1
                        usuario = self.db.get(doc_id=cliente_id)
                        abrir_menu(cliente_id)                   
                    else:
                        label_cliente['text'] = 'CPF ou senha inválidos!'
                        label_cliente['bg'] = '#5FC0E6'
            
             
            label_cpf_login= tk.Label(self.janela, text= 'CPF:', background="#5FC0E6")
            label_cpf_login.pack()
            label_cpf_login.place(x=100, y=130)
            entry_cpf_login = tk.Entry(self.janela)
            entry_cpf_login.pack()
            entry_cpf_login.place(x=100, y=150)

            label_senha = tk.Label(self.janela, text='Senha:', background="#5FC0E6")
            label_senha.pack()
            label_senha.place(x=100, y=180)
            entry_senha = tk.Entry(self.janela, show='*')
            entry_senha.pack()
            entry_senha.place(x=100, y=200)

            botoes()
            button_enter = tk.Button(self.janela, text= 'Enter', command=logar).place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

            label_cliente = tk.Label(self.janela, text='', background="#5FC0E6")
            label_cliente.place(x=100, y=260)

        # FUNÇÃO SAQUE: OK #
        def abrir_saque(cliente_id):
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            nova_imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
            nova_imagem = ImageTk.PhotoImage(nova_imagem)
            label.config(image=nova_imagem)
            label.image = nova_imagem
            cliente = self.db.get(doc_id=cliente_id)

            def atualiza_tela(valor):
                nonlocal cliente
                cliente = self.db.get(doc_id=cliente_id)
                label_cabecalho = tk.Label(self.janela, text=cliente["nome"] + ", seu saldo é:\nR$ " + str(cliente['saldo']) + '\n\nREALIZAR SAQUE:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=120, y=50)
                imagem = Image.open(self.diretorio_atual + "/images/atm_bg_dinheiro.png")
                nova_imagem = ImageTk.PhotoImage(imagem)
                label.configure(image=nova_imagem)
                label.image = nova_imagem
                
            transacao = Transacoes()

            mensagem_label = tk.Label(self.janela, text="", background="#5FC0E6", font=('normal', 11), justify="left")
            mensagem_label.pack()
            mensagem_label.place(x=30, y=200)

            def sacar(cliente_id):
                nonlocal cliente
                cliente = self.db.get(doc_id=cliente_id)
                valor = entry_valor.get()
                if valor:
                    valor = float(valor)
                    print(valor)
                    if transacao.saque(cliente_id, valor):
                        atualiza_tela(valor)
                        mensagem_label.config(text="Sucesso! Seu saque de R$" + str(valor) + " foi realizado.\nSeu saldo atual é: R$ " + str(cliente['saldo']))
                    else:
                        mensagem_label.config(text="Erro! Saldo insuficiente ou valor inválido.\nSeu saldo atual é: R$ " + str(cliente['saldo']))

            label_cabecalho = tk.Label(self.janela, text=cliente["nome"] + ", seu saldo é:\nR$ " + str(cliente['saldo']) + '\n\nREALIZAR SAQUE:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=120, y=50)
            label_rodape = tk.Label(self.janela, text='Use "*" para voltar ao menu', font=('normal', 11), justify="left", bg="#5FC0E6").place(x=120, y=340)

            label_valor= tk.Label(self.janela, text= 'Valor:', background="#5FC0E6").place(x=100, y=130)
            entry_valor = tk.Entry(self.janela)
            entry_valor.pack()
            entry_valor.place(x=100, y=150)

            botoes()
            button_enter = tk.Button(self.janela, text='Enter', command=lambda: sacar(cliente_id))
            button_enter.place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2, command=lambda: abrir_menu(cliente_id)).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

        # FUNÇÃO EXTRATO #
        def abrir_extrato(cliente_id):
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            nova_imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
            nova_imagem = ImageTk.PhotoImage(nova_imagem)
            label.config(image=nova_imagem)
            label.image = nova_imagem
            cliente = self.db.get(doc_id=cliente_id)

            def atualiza_tela():
                imagem = Image.open(self.diretorio_atual + "/images/atm_bg_extrato.png")
                nova_imagem = ImageTk.PhotoImage(imagem)
                label.configure(image=nova_imagem)
                label.image = nova_imagem
                mensagem_label.config(text="Comprovante impresso!", font=('normal', 14))
                
            transacoes_extrato = Transacoes()

            mensagem_label = tk.Label(self.janela, text="", background="#5FC0E6", font=('normal', 10), justify="left")
            mensagem_label.pack()
            mensagem_label.place(x=120, y=170)

            def extrato(cliente_id):
                nonlocal cliente
                cliente = self.db.get(doc_id=cliente_id)
                transacoes_cliente = transacoes_extrato.extrato(cliente_id)
                if transacoes_cliente:
                    atualiza_tela()
                    janela_extrato = tk.Toplevel(self.janela)
                    janela_extrato.title("Extrato impresso")
                    janela_extrato.geometry("300x400")
                    
                    frame_extrato = tk.Frame(janela_extrato)
                    frame_extrato.pack(fill=tk.BOTH, expand=True)
                    
                    scrollbar = tk.Scrollbar(frame_extrato)
                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                    
                    # Cria um widget Canvas para o frame do extrato
                    canvas = tk.Canvas(frame_extrato, yscrollcommand=scrollbar.set)
                    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                    
                    # Associa a barra de rolagem ao canvas
                    scrollbar.config(command=canvas.yview)
                    
                    # Cria um frame interno para as transações
                    inner_frame = tk.Frame(canvas)
                    canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)
                    
                    for i, transacao in enumerate(transacoes_cliente):
                        label_transacao = tk.Label(inner_frame, text=transacao, font=('normal', 10), justify="left")
                        label_transacao.pack(anchor=tk.W)
                    
                    # Atualiza o tamanho do canvas
                    canvas.update_idletasks()
                    canvas.config(scrollregion=canvas.bbox(tk.ALL))
                    
                else:
                    mensagem_label.config(text="Não há transações para exibir.")

            label_cabecalho = tk.Label(self.janela, text=cliente["nome"].split()[0] + ", tecle enter para gerar o seu extrato.\nSeu saldo atual é: R$ " + str(cliente['saldo']), font=('normal', 12), justify="center", bg="#5FC0E6").place(x=60, y=120)
            label_rodape = tk.Label(self.janela, text='Use "*" para voltar ao menu', font=('normal', 11), justify="left", bg="#5FC0E6").place(x=120, y=340)

            botoes()
            button_enter = tk.Button(self.janela, text='Enter', command=lambda: extrato(cliente_id))
            button_enter.place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2, command=lambda: abrir_menu(cliente_id)).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

        # FUNÇÃO DEPÓSITO> OK #
        def abrir_deposito(cliente_id):
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            nova_imagem = Image.open(self.diretorio_atual + "/images/atm_bg_dinheiro.png")
            nova_imagem = ImageTk.PhotoImage(nova_imagem)
            label.config(image=nova_imagem)
            label.image = nova_imagem
            cliente = self.db.get(doc_id=cliente_id)

            def atualiza_tela(valor):
                nonlocal cliente
                cliente = self.db.get(doc_id=cliente_id)
                label_cabecalho = tk.Label(self.janela, text=cliente["nome"] + ", seu saldo é:\nR$ " + str(cliente['saldo']) + '\n\nREALIZAR DEPÓSITO:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=120, y=50)
                imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
                nova_imagem = ImageTk.PhotoImage(imagem)
                label.configure(image=nova_imagem)
                label.image = nova_imagem
                
            transacao = Transacoes()

            mensagem_label = tk.Label(self.janela, text="", background="#5FC0E6", font=('normal', 11), justify="left")
            mensagem_label.pack()
            mensagem_label.place(x=30, y=200)

            def depositar(cliente_id):
                nonlocal cliente
                cliente = self.db.get(doc_id=cliente_id)
                valor = entry_valor.get()
                if valor:
                    valor = float(valor)
                    print(valor)
                    if transacao.deposito(cliente_id, valor):
                        atualiza_tela(valor)
                        mensagem_label.config(text="Seu depósito de R$" + str(valor) + " foi realizado com sucesso.\nSeu saldo atual é: R$ " + str(cliente['saldo']))
                    else:
                        mensagem_label.config(text="Erro. Este valor é inválido para depósitos.\nSeu saldo atual é: R$ " + str(cliente['saldo']))

            label_cabecalho = tk.Label(self.janela, text=cliente["nome"] + ", seu saldo é:\nR$ " + str(cliente['saldo']) + '\n\nREALIZAR DEPÓSITO:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=120, y=50)
            label_rodape = tk.Label(self.janela, text='Use "*" para voltar ao menu', font=('normal', 11), justify="left", bg="#5FC0E6").place(x=120, y=340)

            label_valor= tk.Label(self.janela, text= 'Valor:', background="#5FC0E6").place(x=100, y=130)
            entry_valor = tk.Entry(self.janela)
            entry_valor.pack()
            entry_valor.place(x=100, y=150)

            botoes()
            button_enter = tk.Button(self.janela, text='Enter', command=lambda: depositar(cliente_id))
            button_enter.place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2, command=lambda: abrir_menu(cliente_id)).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

        # INÍCIO DA FUNÇÃO SOLICITAR CRÉDITO#
        def solicita_credito(cliente_id):
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            nova_imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
            nova_imagem = ImageTk.PhotoImage(nova_imagem)
            label.config(image=nova_imagem)
            label.image = nova_imagem
            cliente = self.db.get(doc_id=cliente_id)
            
            mensagem_label = tk.Label(self.janela, text="", background="#5FC0E6", font=('normal', 11), justify="left")
            mensagem_label.pack()
            mensagem_label.place(x=30, y=200)

            solicitar = SolicitaCredito()

            label_valor = tk.Label(self.janela, text='Valor:', background="#5FC0E6")
            label_valor.pack()
            label_valor.place(x=100, y=130)
            entry_valor = tk.Entry(self.janela)
            entry_valor.pack()
            entry_valor.place(x=100, y=150)

            label_credito_situacao = tk.Label(self.janela, text="", font=("Arial", 10), justify="left", background="#5FC0E6")
            label_credito_situacao.pack()
            label_credito_situacao.place(x=30, y=260)

            label_rodape = tk.Label(self.janela, text='Use "*" para voltar ao menu', font=('normal', 11), justify="left", bg="#5FC0E6").place(x=90, y=340)

            label_cabecalho = tk.Label(self.janela, text="Olá, " + cliente["nome"] + "\nfaça o seu pedido." + '\n\nPEDIDO DE CRÉDITO:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=70, y=50)

            botoes()
            button_asterisco = tk.Button(self.janela, text= '*', width=2, command=lambda: abrir_menu(cliente_id)).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

            def enviar_solicitacao(cliente_id):
                print(cliente_id)
                valor = float(entry_valor.get())
                data_atual = datetime.now().date()
                data_prox_fatura = data_atual + timedelta(days=30)
                data_formatada = data_prox_fatura.strftime("%d/%m/%Y")
                if valor <= 0:
                    label_credito_situacao.configure(text="O valor da solicitação não pode ser menor ou igual a 0.")
                else:
                    if solicitar.solicitacao(cliente_id, valor, data_formatada):
                        label_credito_situacao.configure(text="Parabéns, seu crédito foi aprovado!\nSua próxima fatura será debitada em 30 dias.")
                    else: label_credito_situacao.configure(text="Que pena! Não foi dessa vez.\nSe você já fez um pedido de crédito, outra liberação\n só ocorrerá quando não houver mais débitos a serem feitos.")

            button_enter = tk.Button(self.janela, text='Enter', command=lambda: enviar_solicitacao(cliente_id))
            button_enter.place(x=285, y=513)

        # INÍCIO DA FUNÇÃO PAGAMENTO
        def realizar_pagamento(cliente_id):
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            nova_imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
            nova_imagem = ImageTk.PhotoImage(nova_imagem)
            label.config(image=nova_imagem)
            label.image = nova_imagem
            cliente = self.db.get(doc_id=cliente_id)
            
            label_rodape = tk.Label(self.janela, text='Use "*" para voltar ao menu', font=('normal', 11), justify="left", bg="#5FC0E6").place(x=90, y=340)
            label_cabecalho = tk.Label(self.janela, text=cliente["nome"] + ", seu saldo é:\nR$ " + str(cliente['saldo']) + '\n\nREALIZAR TRANSFERÊNCIA:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=70, y=50)

            def pagamento(cliente_id):
                cpf = conta_destino_entry.get()
                valor = float(valor_entry.get())
                valor_str = valor_entry.get()
                valor_str = valor_str.replace(',','.')
                valor = float(valor_str)
                
                if valor <= 0:
                    mensagem_label = tk.Label(self.janela, text='Valor inválido', background="#5FC0E6")
                    mensagem_label.place(x=100, y=120)
                    return False
                
                for indice, destinatario in enumerate(self.db.all()):
                    if destinatario['cpf_ou_cnpj'] == cpf:
                        destinatario_id = indice+1
                        destinatario = self.db.get(doc_id=destinatario_id)
                        transacao = Transacoes()
                        
                        if transacao.realizar_pagamento(cliente_id, destinatario_id, valor):
                            cliente = self.db.get(doc_id=cliente_id)
                            label_cabecalho = tk.Label(self.janela, text=cliente["nome"] + ", seu saldo é:\nR$ " + str(cliente['saldo']) + '\n\nREALIZAR TRANSFERÊNCIA:', font=('normal', 11), justify="center", bg="#5FC0E6").place(x=70, y=50)
                            mensagem_label = tk.Label(self.janela, text='Pagamento realizado com sucesso', background="#5FC0E6")
                            mensagem_label.place(x=100, y=120)
                            cliente = self.db.get(doc_id=cliente_id)
                            return True
                        else:
                            mensagem_label = tk.Label(self.janela, text='ERRO! Transação não realizada',background="#5FC0E6")
                            mensagem_label.place(x=100, y=120)
                            return False
            
            conta_destino_label = tk.Label(self.janela, text="CPF/CNPJ da conta de destino:", background="#5FC0E6")
            conta_destino_label.place(x=100, y=140)
            conta_destino_entry = tk.Entry(self.janela)
            conta_destino_entry.place(x=100, y=160)

            valor_label = tk.Label(self.janela, text="Valor do pagamento:", background="#5FC0E6")
            valor_label.place(x=100, y=180)
            valor_entry = tk.Entry(self.janela)
            valor_entry.place(x=100, y=200)            
            
            botoes()
            button_enter = tk.Button(self.janela, text='Enter', command= lambda: pagamento(cliente_id))
            button_enter.place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2, command=lambda: abrir_menu(cliente_id)).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)
            
        # INÍCIO DA FUNÇÃO MENU #
        def abrir_menu(cliente_id):
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            cliente = self.db.get(doc_id=cliente_id)

            label_cabecalho = tk.Label(self.janela, text='Olá, ' + cliente["nome"] + ".", font=('normal', 11), justify="left", bg="#5FC0E6").place(x=120, y=50)

            opcoes_texto = "Menu:\n\n1 - Extrato\n2 - Saque\n3 - Depósito\n4 - Realizar pagamento\n5 - Solicitar crédito\n6 - Sair\n\nEntre com a sua opção: _ "

            def sair():
                self.janela.destroy()

            label_opcoes = tk.Label(self.janela, text=opcoes_texto, font=('normal', 13), justify="left", bg="#5FC0E6").place(x=70, y=90)

            button_1 = tk.Button(self.janela, text= '1', width=2, command=lambda: abrir_extrato(cliente_id)).place(x=113, y=404)
            button_2 = tk.Button(self.janela, text='2', width=2, command=lambda: abrir_saque(cliente_id)).place(x=166, y=404)
            button_3 = tk.Button(self.janela, text= '3', width=2, command=lambda: abrir_deposito(cliente_id)).place(x=219, y=404)
            button_4 = tk.Button(self.janela, text= '4', width=2, command=lambda: realizar_pagamento(cliente_id)).place(x=113, y=440)
            button_5 = tk.Button(self.janela, text= '5', width=2, command=lambda: solicita_credito(cliente_id)).place(x=166, y=440)
            button_6 = tk.Button(self.janela, text= '6', width=2, command=sair).place(x=219, y=440)
            button_7 = tk.Button(self.janela, text= '7', width=2).place(x=113, y=476)
            button_8 = tk.Button(self.janela, text= '8', width=2).place(x=166, y=476)
            button_9 = tk.Button(self.janela, text= '9', width=2).place(x=219, y=476)
            button_0 = tk.Button(self.janela, text= '0', width=2).place(x=166, y=512)
            button_enter = tk.Button(self.janela, text= 'Enter').place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

            self.janela.mainloop()
            
                
        def realizar_cadastro():
            mensagem = "Vá até o banco para que o gerente faça seu cadastro."
            # Exibe a mensagem em uma caixa de diálogo
            tk.messagebox.showinfo("Autocash", mensagem)
    
            
        while True:
            opcoes_texto = 'Bem-vindo ao autocash.\nEscolha uma das opções abaixo:\n\n  1 - Fazer login\n  2 - Realizar cadastro'
            verificar_debitos = Transacoes()
            verificar_debitos.verificar_debitos()
            verificar_banco = VerificarBanco()
            verificar_banco.verificar_banco()
            label_opcoes = tk.Label(self.janela, text=opcoes_texto, font=("normal", 14), justify="left", bg="#5FC0E6", wraplength=300).place(x=80, y=90)

            button_1 = tk.Button(self.janela, text= '1', width=2, command=fazer_login).place(x=113, y=404)
            button_2 = tk.Button(self.janela, text= '2', width=2, command= realizar_cadastro).place(x=166, y=404)
            button_3 = tk.Button(self.janela, text= '3', width=2).place(x=219, y=404)
            button_4 = tk.Button(self.janela, text= '4', width=2).place(x=113, y=440)
            button_5 = tk.Button(self.janela, text= '5', width=2).place(x=166, y=440)
            button_6 = tk.Button(self.janela, text= '6', width=2).place(x=219, y=440)
            button_7 = tk.Button(self.janela, text= '7', width=2).place(x=113, y=476)
            button_8 = tk.Button(self.janela, text= '8', width=2).place(x=166, y=476)
            button_9 = tk.Button(self.janela, text= '9', width=2).place(x=219, y=476)
            button_0 = tk.Button(self.janela, text= '0', width=2).place(x=166, y=512)
            button_enter = tk.Button(self.janela, text= 'Enter').place(x=285, y=513)
            button_asterisco = tk.Button(self.janela, text= '*', width=2).place(x=113, y=512)
            button_hashtag = tk.Button(self.janela, text= '#').place(x=219, y=513)

            self.janela.mainloop()

if __name__ == "__main__":
    app = AutocashApp()
    app.iniciar()