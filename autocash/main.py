import os, subprocess, tkinter as tk
from library.module import Gerente, Conta, Transacoes, Cliente, SolicitaCredito
from PIL import ImageTk, Image
from tinydb import TinyDB, where

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
db = TinyDB(diretorio_atual + '/banco_de_dados.json')

janela = tk.Tk()
janela.geometry("600x600")
janela.title("Menu")
janela.resizable(False, False)

imagem = Image.open(diretorio_atual + "/images/atm_bg.png")
imagem = imagem.resize((600, 600), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)
label = tk.Label(janela, image=imagem_tk).place(x=0, y=0, relwidth=1, relheight=1)

######################################
#         INÍCIO DAS FUNÇÕES         #
######################################

# INÍCIO DA FUNÇÃO REALIZAR CADASTRO #
def realizar_cadastro():
    subprocess.run(['python', diretorio_atual +'/cadastro.py'])

# INÍCIO DA FUNÇÃO LOGIN #
def fazer_login():
    imagem_tk = ImageTk.PhotoImage(imagem)
    label = tk.Label(janela, image=imagem_tk)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    def mudar_imagem():
        imagem_original = Image.open(diretorio_atual + "/images/atm_bg_insere_cartao.png")
        nova_imagem = imagem_original.resize((600, 600))
        nova_imagem = ImageTk.PhotoImage(nova_imagem)
        label.config(image=nova_imagem)
        label.image = nova_imagem    
    mudar_imagem()

    def logar():
        cpf = entry_cpf_login.get()
        senha = entry_senha.get()
        cliente = db.search((where('cpf') == cpf) & (where('senha') == senha))
        print(cliente)
        if cliente:
            label_cliente['text'] = 'Login realizado com sucesso!'        
            label_cliente['bg'] = '#50c7e2'
            abrir_menu()  
        else:
            label_cliente['text'] = 'CPF ou senha inválidos!'
            label_cliente['bg'] = '#50c7e2'
                 
    label_cpf_login= tk.Label(janela, text= 'CPF:', background="#50c7e2")
    label_cpf_login.pack()
    label_cpf_login.place(x=100, y=130)
    entry_cpf_login = tk.Entry(janela)
    entry_cpf_login.pack()
    entry_cpf_login.place(x=100, y=150)

    label_senha = tk.Label(janela, text='Senha:', background="#50c7e2")
    label_senha.pack()
    label_senha.place(x=100, y=180)
    entry_senha = tk.Entry(janela, show='*')
    entry_senha.pack()
    entry_senha.place(x=100, y=200)

    button_1 = tk.Button(janela, text= '1', width=2).place(x=113, y=404)
    button_2 = tk.Button(janela, text= '2', width=2).place(x=166, y=404)
    button_3 = tk.Button(janela, text= '3', width=2).place(x=219, y=404)
    button_4 = tk.Button(janela, text= '4', width=2).place(x=113, y=440)
    button_5 = tk.Button(janela, text= '5', width=2).place(x=166, y=440)
    button_6 = tk.Button(janela, text= '6', width=2).place(x=219, y=440)
    button_7 = tk.Button(janela, text= '7', width=2).place(x=113, y=476)
    button_8 = tk.Button(janela, text= '8', width=2).place(x=166, y=476)
    button_9 = tk.Button(janela, text= '9', width=2).place(x=219, y=476)
    button_0 = tk.Button(janela, text= '0', width=2).place(x=166, y=512)
    button_enter = tk.Button(janela, text= 'Enter', command=logar).place(x=285, y=513)

    label_cliente = tk.Label(janela, text='', background="#50c7e2")
    label_cliente.place(x=100, y=260)

# INÍCIO DA FUNÇÃO SAQUE #
def abrir_saque():
    def mudar_imagem():
        imagem_original = Image.open(diretorio_atual + "/images/atm_bg_dinheiro.png")
        nova_imagem = imagem_original.resize((600, 600))
        nova_imagem = ImageTk.PhotoImage(nova_imagem)
        label.config(image=nova_imagem)
        label.image = nova_imagem 

    imagem = Image.open(diretorio_atual + "/images/atm_bg.png")
    imagem = imagem.resize((600, 600))
    imagem_tk = ImageTk.PhotoImage(imagem)

    label = tk.Label(janela, image=imagem_tk)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    valor_label = tk.Label(janela, text="Digite o valor do saque:", background='#50c7e2')
    valor_label.pack()
    valor_label.place(x=100, y=70)

    valor_entry = tk.Entry(janela)
    valor_entry.pack()
    valor_entry.place(x=100, y=90)

    senha_label = tk.Label(janela, text="Digite sua senha:", background='#50c7e2')
    senha_label.pack()
    senha_label.place(x=100, y=120)

    senha_entry = tk.Entry(janela, show="*")
    senha_entry.pack()
    senha_entry.place(x=100, y=140)

    verificar_button = tk.Button(janela, text="Verificar senha")
    verificar_button.pack()
    verificar_button.place(x=100, y=160)


    sacar_button = tk.Button(janela, text="Sacar", command=mudar_imagem,  background="#d2d5d4")
    sacar_button.pack()
    sacar_button.place(x=285, y=513)

    mensagem_label = tk.Label(janela, text="", background="#50c7e2")
    mensagem_label.pack()
    mensagem_label.place(x=100, y=200)

    button_1 = tk.Button(janela, text= '1', width=2).place(x=113, y=404)
    button_2 = tk.Button(janela, text= '2', width=2).place(x=166, y=404)
    button_3 = tk.Button(janela, text= '3', width=2).place(x=219, y=404)
    button_4 = tk.Button(janela, text= '4', width=2).place(x=113, y=440)
    button_5 = tk.Button(janela, text= '5', width=2).place(x=166, y=440)
    button_6 = tk.Button(janela, text= '6', width=2).place(x=219, y=440)
    button_7 = tk.Button(janela, text= '7', width=2).place(x=113, y=476)
    button_8 = tk.Button(janela, text= '8', width=2).place(x=166, y=476)
    button_9 = tk.Button(janela, text= '9', width=2).place(x=219, y=476)
    button_0 = tk.Button(janela, text= '0', width=2).place(x=166, y=512)
    button_enter = tk.Button(janela, text= 'Enter').place(x=285, y=513)

    janela.mainloop()

# INÍCIO DA FUNÇÃO MENU #
def abrir_menu():
    imagem_tk = ImageTk.PhotoImage(imagem)
    label = tk.Label(janela, image=imagem_tk)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    opcoes_texto = "Menu:\n\n1 - Extrato\n2 - Saque\n3 - Depósito\n4 - Realizar pagamento\n5 - Solicitar crédito\n6 - Sair\n\nEntre com a sua opção: _ "

    label_opcoes = tk.Label(janela, text=opcoes_texto, font=("Consolas", 14), justify="left", bg="#50c7e2").place(x=70, y=90)

    button_1 = tk.Button(janela, text= '1', width=2).place(x=113, y=404)
    button_2 = tk.Button(janela, text= '2', width=2, command=abrir_saque).place(x=166, y=404)
    button_3 = tk.Button(janela, text= '3', width=2).place(x=219, y=404)
    button_4 = tk.Button(janela, text= '4', width=2).place(x=113, y=440)
    button_5 = tk.Button(janela, text= '5', width=2).place(x=166, y=440)
    button_6 = tk.Button(janela, text= '6', width=2).place(x=219, y=440)
    button_7 = tk.Button(janela, text= '7', width=2).place(x=113, y=476)
    button_8 = tk.Button(janela, text= '8', width=2).place(x=166, y=476)
    button_9 = tk.Button(janela, text= '9', width=2).place(x=219, y=476)
    button_0 = tk.Button(janela, text= '0', width=2).place(x=166, y=512)
    button_enter = tk.Button(janela, text= 'Enter').place(x=285, y=513)

    janela.mainloop()


while True:
    opcoes_texto = 'Bem-vindo ao autocash.\nEscolha uma das opções abaixo:\n\n  1 - Fazer login\n  2 - Realizar cadastro'

    label_opcoes = tk.Label(janela, text=opcoes_texto, font=("Montserrat", 14), justify="left", bg="#50c7e2", wraplength=300).place(x=80, y=90)

    button_1 = tk.Button(janela, text= '1', width=2, command=fazer_login).place(x=113, y=404)
    button_2 = tk.Button(janela, text= '2', width=2, command=realizar_cadastro).place(x=166, y=404)
    button_3 = tk.Button(janela, text= '3', width=2, command=abrir_menu).place(x=219, y=404)
    button_4 = tk.Button(janela, text= '4', width=2).place(x=113, y=440)
    button_5 = tk.Button(janela, text= '5', width=2).place(x=166, y=440)
    button_6 = tk.Button(janela, text= '6', width=2).place(x=219, y=440)
    button_7 = tk.Button(janela, text= '7', width=2).place(x=113, y=476)
    button_8 = tk.Button(janela, text= '8', width=2).place(x=166, y=476)
    button_9 = tk.Button(janela, text= '9', width=2).place(x=219, y=476)
    button_0 = tk.Button(janela, text= '0', width=2).place(x=166, y=512)
    button_enter = tk.Button(janela, text= 'Enter').place(x=285, y=513)

    janela.mainloop()
