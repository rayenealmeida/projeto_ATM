import os
import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
from tinydb import TinyDB, where


# Obtém o caminho do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco_dados = os.path.join(diretorio_atual, 'banco_de_dados.json')

db = TinyDB(caminho_banco_dados)




def verificar_login():
    cpf = entry_cpf_login.get()
    senha = entry_senha.get()
    
    resultado = db.search((where('cpf') == cpf) & (where('senha') == senha))
    
    if resultado:
        label_resultado['text'] = 'Login realizado com sucesso!'        
    else:
        label_resultado['text'] = 'CPF ou senha inválidos!'

janela_login = tk.Tk()
janela_login.geometry("600x600")
janela_login.title("Login")
janela_login.resizable(False, False)

imagem = Image.open(diretorio_atual + "/images/atm_bg.png")
imagem = imagem.resize((600, 600), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)

label = Label(janela_login, image=imagem_tk)
label.place(x=0, y=0, relwidth=1, relheight=1)

label_cpf_login= Label(janela_login, text= 'CPF:')
label_cpf_login.pack()
label_cpf_login.place(x=100, y=130)
entry_cpf_login = tk.Entry(janela_login)
entry_cpf_login.pack()
entry_cpf_login.place(x=100, y=150)

label_senha = Label(janela_login, text='Senha:')
label_senha.pack()
label_senha.place(x=100, y=180)
entry_senha = tk.Entry(janela_login, show='*')
entry_senha.pack()
entry_senha.place(x=100, y=200)

button_login = tk.Button(janela_login, text= 'Entrar', command= verificar_login)
button_login.pack()
button_login.place(x=100, y=230)

label_resultado = Label(janela_login, text='')
label_resultado.pack()
label_resultado.place(x=100, y=260)

janela_login.mainloop()