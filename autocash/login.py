import os
import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
from tinydb import TinyDB, where
import subprocess

# Obtém o caminho do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco_dados = os.path.join(diretorio_atual, 'banco_de_dados.json')

db = TinyDB(caminho_banco_dados)

def abrir_menu():
   subprocess.run(['python', diretorio_atual +'/menu.py'])


def verificar_login():
    cpf = entry_cpf_login.get()
    senha = entry_senha.get()
    
    resultado = db.search((where('cpf') == cpf) & (where('senha') == senha))
    
    if resultado:
        label_resultado['text'] = 'Login realizado com sucesso!'        
        label_resultado['bg'] = '#50c7e2'
        janela_login.destroy() 
        abrir_menu()  

    else:
        label_resultado['text'] = 'CPF ou senha inválidos!'
        label_resultado['bg'] = '#50c7e2'
                 
janela_login = tk.Tk()
janela_login.geometry("600x600")
janela_login.title("Login")
janela_login.resizable(False, False)

imagem = Image.open(diretorio_atual + "/images/atm_bg_insere_cartao.png")
imagem = imagem.resize((600, 600), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)

label = Label(janela_login, image=imagem_tk)
label.place(x=0, y=0, relwidth=1, relheight=1)

label_cpf_login= Label(janela_login, text= 'CPF:', background="#50c7e2")
label_cpf_login.pack()
label_cpf_login.place(x=100, y=130)
entry_cpf_login = tk.Entry(janela_login)
entry_cpf_login.pack()
entry_cpf_login.place(x=100, y=150)

label_senha = Label(janela_login, text='Senha:', background="#50c7e2")
label_senha.pack()
label_senha.place(x=100, y=180)
entry_senha = tk.Entry(janela_login, show='*')
entry_senha.pack()
entry_senha.place(x=100, y=200)

button_login = tk.Button(janela_login, text= 'Entrar', command=verificar_login)
button_login.pack()
button_login.place(x=285, y=513)

label_resultado = Label(janela_login, text='', background="#50c7e2")
label_resultado.pack()
label_resultado.place(x=100, y=260)

button_login = tk.Button(janela_login, text= '1')
button_login.pack()
button_login.place(x=117, y=404)

button_login = tk.Button(janela_login, text= '2')
button_login.pack()
button_login.place(x=170, y=404)

button_login = tk.Button(janela_login, text= '3')
button_login.pack()
button_login.place(x=223, y=404)

button_login = tk.Button(janela_login, text= '4')
button_login.pack()
button_login.place(x=117, y=440)

button_login = tk.Button(janela_login, text= '5')
button_login.pack()
button_login.place(x=170, y=440)

button_login = tk.Button(janela_login, text= '6')
button_login.pack()
button_login.place(x=223, y=440)

button_login = tk.Button(janela_login, text= '7')
button_login.pack()
button_login.place(x=117, y=476)

button_login = tk.Button(janela_login, text= '8')
button_login.pack()
button_login.place(x=170, y=476)

button_login = tk.Button(janela_login, text= '9')
button_login.pack()
button_login.place(x=223, y=476)

button_login = tk.Button(janela_login, text= '0')
button_login.pack()
button_login.place(x=170, y=512)

janela_login.mainloop()