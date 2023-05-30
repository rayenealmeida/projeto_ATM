import customtkinter, Label, Entry, Button
from tinydb import TinyDB

db = TinyDB('banco_de_dados.json')

def salvar_cadastro():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data_nascimento.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    renda = entry_renda.get()
    senha = entry_senha.get()
    
def login():
    cpf = entry_cpf

    # Salvar os dados no banco de dados
    db.insert({
        'nome': nome,
        'telefone': telefone,
        'data_nascimento': data_nascimento,
        'cpf/cnpj': cpf,
        'endereco': endereco,
        'renda': renda
    })

    # Limpar os campos após salvar
    entry_nome.delete(0, 'end')
    entry_telefone.delete(0, 'end')
    entry_data_nascimento.delete(0, 'end')
    entry_cpf.delete(0, 'end')
    entry_endereco.delete(0, 'end')
    entry_renda.delete(0, 'end')
    entry_senha.delete(0, 'end')


janela = customtkinter.CTk()
janela.geometry("400x300")
janela.grid_columnconfigure(0, weight=1)

def clique():
    print("Solicitar Cadastro")
    

texto = customtkinter.CTkLabel(janela, text="Solicitar Cadastro")
texto.pack(padx=10, pady=10)


label_nome = Label(janela, text='Nome:')
label_nome.pack()
entry_nome = Entry(janela)
entry_nome.pack()

label_telefone = Label(janela, text='Telefone:')
label_telefone.pack()
entry_telefone = Entry(janela)
entry_telefone.pack()

label_data_nascimento = Label(janela, text='Data de Nascimento:')
label_data_nascimento.pack()
entry_data_nascimento = Entry(janela)
entry_data_nascimento.pack()

label_cpf = Label(janela, text='CPF:')
label_cpf.pack()
entry_cpf = Entry(janela)
entry_cpf.pack()

label_endereco = Label(janela, text='Endereço:')
label_endereco.pack()
entry_endereco = Entry(janela)
entry_endereco.pack()

label_renda = Label(janela, text='Renda:')
label_renda.pack()
entry_renda = Entry(janela)
entry_renda.pack()

label_senha = Label(janela, text='Senha:')
label_senha.pack()
entry_senha = Entry(janela)
entry_senha.pack()

button_salvar = Button(janela, text='Salvar', command=salvar_cadastro)
button_salvar.pack()

#button_login = Button(janela, text='Fazer Login', command=)
#button_login.pack()

janela.mainloop()
