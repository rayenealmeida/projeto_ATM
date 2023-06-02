import os
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel
from tinydb import TinyDB

# Obtém o caminho do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco_dados = os.path.join(diretorio_atual, 'banco_de_dados.json')

db = TinyDB(caminho_banco_dados)

def salvar_cadastro():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data_nascimento.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    renda = entry_renda.get()
    senha = entry_senha.get()

    # Salvar os dados no banco de dados
    db.insert({
        'nome': nome,
        'telefone': telefone,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
        'renda': renda,
        'senha': senha,
    })
    
    exibir_janela_confirmacao()
    
def exibir_janela_confirmacao():
    janela_confirmacao = Toplevel(janela)
    janela_confirmacao.title("Cadastro Aprovado! Faça seu Login")
    janela_confirmacao.geometry("300x100")
    
    label_confirmacao = Label(janela_confirmacao, text="Cadastro aprovado")
    label_confirmacao.pack(pady=20)
    
    button_ok = Button(janela_confirmacao, text="OK", command=janela_confirmacao.destroy)
    button_ok.pack()
    
    # Limpar os campos após salvar
    entry_nome.delete(0, 'end')
    entry_telefone.delete(0, 'end')
    entry_data_nascimento.delete(0, 'end')
    entry_cpf.delete(0, 'end')
    entry_endereco.delete(0, 'end')
    entry_renda.delete(0, 'end')
    entry_senha.delete(0, 'end')
    

    
def abrir_janela_login():
    janela.destroy()
    import login

janela = Tk()
janela.title("Solicitar Cadastro")
largura = 400
altura = 300
x = (janela.winfo_screenwidth() - largura) // 2
y = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f'{largura}x{altura}+{x}+{y}')

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

label_senha = Label(janela, text='Crie uma Senha:')
label_senha.pack()
entry_senha = Entry(janela, show='*')
entry_senha.pack()

button_frame = Frame(janela)
button_frame.pack(pady=10)

button_salvar = Button(janela, text='Salvar', command=salvar_cadastro)
button_salvar.pack(side='top', padx=5)

button_login= Button(janela, text='Login', command=abrir_janela_login)
button_login.pack(side='top', padx=5)

janela.mainloop()