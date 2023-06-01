from tkinter import Tk, Label, Entry, Button
from tinydb import TinyDB, where

db = TinyDB('banco_de_dados.json')

def verificar_login():
    cpf = entry_cpf_login.get()
    senha = entry_senha.get()
    
    resultado = db.search((where('cpf') == cpf) & (where('senha') == senha))
    
    if resultado:
        print('Login realizado com sucesso!')
    else:
        print('CPF ou senha inválidos!')

janela_login = Tk()
janela_login.title("Login")

label_cpf_login= Label(janela_login, text= 'CPF:')
label_cpf_login.pack()
entry_cpf_login = Entry(janela_login)
entry_cpf_login.pack()

label_senha = Label(janela_login, text='Senha:')
label_senha.pack()
entry_senha = Entry(janela_login, show='*')
entry_senha.pack()

button_login = Button(janela_login, text= 'Entrar', command= verificar_login)
button_login.pack()

janela_login.mainloop()