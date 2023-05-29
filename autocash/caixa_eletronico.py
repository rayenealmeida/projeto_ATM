import tkinter as tk
from PIL import ImageTk, Image

def verificar_senha():
    senha = senha_entry.get()
    
    # Lógica para verificar a senha
    
    if senha == "1234":
        mensagem_label.config(text="Senha correta")
    else:
        mensagem_label.config(text="Senha incorreta")

def sacar():
    # Lógica para realizar o saque
    valor = valor_entry.get()
    
    # Exibir uma mensagem de sucesso ou erro
    
    mensagem_label.config(text="Saque realizado com sucesso")

# Criar a janela principal
janela = tk.Tk()
janela.title("Caixa Eletrônico")

# Carregar imagens
tela_image = ImageTk.PhotoImage(Image.open("/home/rayene/Documentos/unb/2023.1/OO/projeto4/projeto_ATM/autocash/tela.png"))
teclado_image = ImageTk.PhotoImage(Image.open("teclado.png"))
local_saque_image = ImageTk.PhotoImage(Image.open("local_saque.png"))

# Criar os elementos da interface
tela_label = tk.Label(janela, image=tela_image)
tela_label.pack()

senha_label = tk.Label(janela, text="Digite sua senha:")
senha_label.pack()

senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

verificar_button = tk.Button(janela, text="Verificar senha", command=verificar_senha)
verificar_button.pack()

teclado_label = tk.Label(janela, image=teclado_image)
teclado_label.pack()

valor_label = tk.Label(janela, text="Digite o valor do saque:")
valor_label.pack()

valor_entry = tk.Entry(janela)
valor_entry.pack()

sacar_button = tk.Button(janela, text="Sacar", command=sacar)
sacar_button.pack()

local_saque_label = tk.Label(janela, image=local_saque_image)
local_saque_label.pack()

mensagem_label = tk.Label(janela, text="")
mensagem_label.pack()

# Iniciar o loop da aplicação
janela.mainloop()
