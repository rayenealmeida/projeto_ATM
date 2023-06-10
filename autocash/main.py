import os, subprocess, tkinter as tk
from library.module import Gerente, Conta, Transacoes, Cliente, SolicitaCredito
from PIL import ImageTk, Image
from tinydb import TinyDB, where
import tkinter.messagebox as messagebox
import json

class AutocashApp:
    def __init__(self):
        self.diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.db = TinyDB(self.diretorio_atual + '/banco_de_dados.json')

        self.janela = tk.Tk()
        self.janela.geometry("600x600")
        self.janela.title("Menu")
        self.janela.resizable(False, False)

        imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
        imagem = imagem.resize((600, 600), Image.ANTIALIAS)
        imagem_tk = ImageTk.PhotoImage(imagem)
        label = tk.Label(self.janela, image=imagem_tk).place(x=0, y=0, relwidth=1, relheight=1)

        ######################################
        #         INÍCIO DAS FUNÇÕES         #
        ######################################

        # INÍCIO DA FUNÇÃO REALIZAR CADASTRO #
        def realizar_cadastro():
            subprocess.run(['python', self.diretorio_atual +'/cadastro.py'])

        # INÍCIO DA FUNÇÃO LOGIN #
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
                cliente = self.db.search((where('cpf') == cpf) & (where('senha') == senha))
                print(cliente)
                if cliente:
                    label_cliente['text'] = 'Login realizado com sucesso!'        
                    label_cliente['bg'] = '#50c7e2'
                    abrir_menu()  
                else:
                    label_cliente['text'] = 'CPF ou senha inválidos!'
                    label_cliente['bg'] = '#50c7e2'
                        
            label_cpf_login= tk.Label(self.janela, text= 'CPF:', background="#50c7e2")
            label_cpf_login.pack()
            label_cpf_login.place(x=100, y=130)
            entry_cpf_login = tk.Entry(self.janela)
            entry_cpf_login.pack()
            entry_cpf_login.place(x=100, y=150)

            label_senha = tk.Label(self.janela, text='Senha:', background="#50c7e2")
            label_senha.pack()
            label_senha.place(x=100, y=180)
            entry_senha = tk.Entry(self.janela, show='*')
            entry_senha.pack()
            entry_senha.place(x=100, y=200)

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
            button_enter = tk.Button(self.janela, text= 'Enter', command=logar).place(x=285, y=513)

            label_cliente = tk.Label(self.janela, text='', background="#50c7e2")
            label_cliente.place(x=100, y=260)

        # INÍCIO DA FUNÇÃO SAQUE #
        def abrir_saque():
            def mudar_imagem():
                imagem_original = Image.open(self.diretorio_atual + "/images/atm_bg_dinheiro.png")
                nova_imagem = imagem_original.resize((600, 600))
                nova_imagem = ImageTk.PhotoImage(nova_imagem)
                label.config(image=nova_imagem)
                label.image = nova_imagem 
            mudar_imagem()

            imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
            imagem = imagem.resize((600, 600))
            imagem_tk = ImageTk.PhotoImage(imagem)

            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)

            valor_label = tk.Label(self.janela, text="Digite o valor do saque:", background='#50c7e2')
            valor_label.pack()
            valor_label.place(x=100, y=70)

            valor_entry = tk.Entry(self.janela)
            valor_entry.pack()
            valor_entry.place(x=100, y=90)

            senha_label = tk.Label(self.janela, text="Digite sua senha:", background='#50c7e2')
            senha_label.pack()
            senha_label.place(x=100, y=120)

            senha_entry = tk.Entry(self.janela, show="*")
            senha_entry.pack()
            senha_entry.place(x=100, y=140)

            verificar_button = tk.Button(self.janela, text="Verificar senha")
            verificar_button.pack()
            verificar_button.place(x=100, y=160)


            sacar_button = tk.Button(self.janela, text="Sacar", command=mudar_imagem,  background="#d2d5d4")
            sacar_button.pack()
            sacar_button.place(x=285, y=513)

            mensagem_label = tk.Label(self.janela, text="", background="#50c7e2")
            mensagem_label.pack()
            mensagem_label.place(x=100, y=200)

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
            button_enter = tk.Button(self.janela, text= 'Enter').place(x=285, y=513)

        # INÍCIO DA FUNÇÃO PAGAMENTO #
        def exibir_mensagem(mensagem):
                messagebox.showinfo("Mensagem", mensagem) 
        def realizar_pagamento():
            def mudar_imagem():
                imagem_original = Image.open(self.diretorio_atual + "/images/atm_bg_pagamento.png")
                nova_imagem = imagem_original.resize((600, 600))
                nova_imagem = ImageTk.PhotoImage(nova_imagem)
                label.config(image=nova_imagem)
                label.image = nova_imagem
            
            imagem = Image.open(self.diretorio_atual + "/images/atm_bg.png")
            imagem = imagem.resize((600, 600))
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0)
            label.pack(fill="both", expand=True)

            conta_origem_label = tk.Label(self.janela, text="Seu nome:", background="#50c7e2")
            conta_origem_label.place(x=100, y=90)

            conta_origem_entry = tk.Entry(self.janela)
            conta_origem_entry.place(x=100, y=110)

            conta_destino_label = tk.Label(self.janela, text="Nome do destinatário:", background="#50c7e2")
            conta_destino_label.place(x=100, y=140)

            conta_destino_entry = tk.Entry(self.janela)
            conta_destino_entry.place(x=100, y=160)

            valor_label = tk.Label(self.janela, text="Valor do pagamento:", background="#50c7e2")
            valor_label.place(x=100, y=190)

            valor_entry = tk.Entry(self.janela)
            valor_entry.place(x=100, y=210)

            agendar_var = tk.IntVar()
            agendar_checkbox = tk.Checkbutton(self.janela, text="Agendar pagamento", variable=agendar_var, background="#50c7e2")
            agendar_checkbox.place(x=100, y=240)
            
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
            button_enter = tk.Button(self.janela, text= 'Enter').place(x=285, y=513)
            mudar_imagem()
     
        
        # INÍCIO DA FUNÇÃO MENU #
        def abrir_menu():
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = tk.Label(self.janela, image=imagem_tk)
            label.place(x=0, y=0, relwidth=1, relheight=1)

            opcoes_texto = "Menu:\n\n1 - Extrato\n2 - Saque\n3 - Depósito\n4 - Realizar pagamento\n5 - Solicitar crédito\n6 - Sair\n\nEntre com a sua opção: _ "

            label_opcoes = tk.Label(self.janela, text=opcoes_texto, font=("Montserrat", 14), justify="left", bg="#50c7e2").place(x=70, y=90)

            button_1 = tk.Button(self.janela, text= '1', width=2).place(x=113, y=404)
            button_2 = tk.Button(self.janela, text= '2', width=2, command=abrir_saque).place(x=166, y=404)
            button_3 = tk.Button(self.janela, text= '3', width=2).place(x=219, y=404)
            button_4 = tk.Button(self.janela, text= '4', width=2, command=realizar_pagamento).place(x=113, y=440)
            button_5 = tk.Button(self.janela, text= '5', width=2).place(x=166, y=440)
            button_6 = tk.Button(self.janela, text= '6', width=2).place(x=219, y=440)
            button_7 = tk.Button(self.janela, text= '7', width=2).place(x=113, y=476)
            button_8 = tk.Button(self.janela, text= '8', width=2).place(x=166, y=476)
            button_9 = tk.Button(self.janela, text= '9', width=2).place(x=219, y=476)
            button_0 = tk.Button(self.janela, text= '0', width=2).place(x=166, y=512)
            button_enter = tk.Button(self.janela, text= 'Enter').place(x=285, y=513)

            self.janela.mainloop()
            
        while True:
            opcoes_texto = 'Bem-vindo ao autocash.\nEscolha uma das opções abaixo:\n\n1 - Fazer login\n2 - Realizar cadastro'

            label_opcoes = tk.Label(self.janela, text=opcoes_texto, font=("Montserrat", 14), justify="left", bg="#50c7e2", wraplength=300).place(x=80, y=90)

            button_1 = tk.Button(self.janela, text= '1', width=2, command=fazer_login).place(x=113, y=404)
            button_2 = tk.Button(self.janela, text= '2', width=2, command=realizar_cadastro).place(x=166, y=404)
            button_3 = tk.Button(self.janela, text= '3', width=2, command=abrir_menu).place(x=219, y=404)
            button_4 = tk.Button(self.janela, text= '4', width=2).place(x=113, y=440)
            button_5 = tk.Button(self.janela, text= '5', width=2).place(x=166, y=440)
            button_6 = tk.Button(self.janela, text= '6', width=2).place(x=219, y=440)
            button_7 = tk.Button(self.janela, text= '7', width=2).place(x=113, y=476)
            button_8 = tk.Button(self.janela, text= '8', width=2).place(x=166, y=476)
            button_9 = tk.Button(self.janela, text= '9', width=2).place(x=219, y=476)
            button_0 = tk.Button(self.janela, text= '0', width=2).place(x=166, y=512)            
            button_enter = tk.Button(self.janela, text= 'Enter').place(x=285, y=513)

            self.janela.mainloop()

if __name__ == "__main__":
    app = AutocashApp()
    app.iniciar()
