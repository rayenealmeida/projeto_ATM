import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
#Cor azul #50c7e2
# Cor cinza claro #d2d5d4
# Cor cinza escuro #9b9b9b
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
janela.geometry("600x600")
janela.title("Caixa Eletrônico")



imagem = Image.open("autocash/images/atm_bg.png")
imagem = imagem.resize((600, 600), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)

label = Label(janela, image=imagem_tk)
label.place(x=0, y=0, relwidth=1, relheight=1)


senha_label = tk.Label(janela, text="Digite sua senha:", background='#9b9b9b')
senha_label.pack()

senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

verificar_button = tk.Button(janela, text="Verificar senha", command=verificar_senha)
verificar_button.pack()

# teclado_label = tk.Label(janela, image=teclado_image)
# teclado_label.pack()

valor_label = tk.Label(janela, text="Digite o valor do saque:", background='#50c7e2')
valor_label.place(x=100, y=500)
valor_label.pack()

valor_entry = tk.Entry(janela)
valor_entry.pack()

sacar_button = tk.Button(janela, text="Sacar", command=sacar)
sacar_button.pack()

# local_saque_label = tk.Label(janela, image=local_saque_image)
# local_saque_label.pack()

mensagem_label = tk.Label(janela, text="")
mensagem_label.pack()

# Iniciar o loop da aplicação
janela.mainloop()
