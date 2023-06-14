import os
from datetime import datetime
from library.module import Gerente, Conta, Transacoes, Cliente, SolicitaCredito
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel
from tinydb import TinyDB

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco_dados = os.path.join(diretorio_atual, 'banco_de_dados.json')

db = TinyDB(caminho_banco_dados)

class CadastroCliente:
    def __init__(self):
        self.gerente = Gerente()

    def salvar_cadastro(self):
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        data_nascimento = entry_data_nascimento.get()
        cpf_ou_cnpj = entry_cpf_ou_cnpj.get()
        endereco = entry_endereco.get()
        renda = float(entry_renda.get())
        senha = entry_senha.get()

        data_atual = datetime.now().date()
        data_nascimento_check = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        idade = data_atual.year - data_nascimento_check.year

        if (data_atual.month, data_atual.day) < (data_nascimento_check.month, data_nascimento_check.day):
            idade -= 1
        if idade < 18:
            self.exibir_janela_reprovacao()
        else:
            # Verificar se todos os campos estão preenchidos
            if nome and telefone and data_nascimento and cpf_ou_cnpj and endereco and renda and senha:
                cliente = Cliente(cpf_ou_cnpj, nome, telefone, endereco, data_nascimento, renda)

                # Salvar os dados no banco de dados
                db.insert({
                    'cadastro_nivel': 1,
                    'nome': nome,
                    'telefone': telefone,
                    'data_nascimento': data_nascimento,
                    'cpf': cpf_ou_cnpj,
                    'endereco': endereco,
                    'renda': renda,
                    'senha': senha,
                    'transacoes': '',
                    'saldo': 0,
                    'solicita_credito': 0,
                    'valor_solicitado': 0,
                    'dia_para_cobranca': '',
                    'solicita_exclusao': 0,
                })

                aprovado = self.gerente.aprovar_conta(cliente)
                if aprovado:
                    self.exibir_janela_confirmacao()
                else:
                    self.exibir_janela_reprovacao()

                self.limpar_campos()
            else:
                import tkinter.messagebox as messagebox
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def exibir_janela_confirmacao(self):
        janela_confirmacao = Toplevel(janela)
        janela_confirmacao.title("Cadastro Aprovado! Faça seu Login")
        janela_confirmacao.geometry("300x100")

        label_confirmacao = Label(janela_confirmacao, text="Cadastro aprovado")
        label_confirmacao.pack(pady=20)

        button_ok = Button(janela_confirmacao, text="OK", command=janela_confirmacao.destroy)
        button_ok.pack()

    def exibir_janela_reprovacao(self):
        janela_reprovacao = Toplevel(janela)
        janela_reprovacao.title("Cadastro Reprovado")
        janela_reprovacao.geometry("300x100")

        label_reprovacao = Label(janela_reprovacao, text="Cadastro reprovado")
        label_reprovacao.pack(pady=20)

        button_ok = Button(janela_reprovacao, text="OK", command=janela_reprovacao.destroy)
        button_ok.pack()

    def limpar_campos(self):
        entry_nome.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_data_nascimento.delete(0, 'end')
        entry_cpf_ou_cnpj.delete(0, 'end')
        entry_endereco.delete(0, 'end')
        entry_renda.delete(0, 'end')
        entry_senha.delete(0, 'end')


cadastro_cliente = CadastroCliente()

def abrir_janela_login():
    janela.destroy()

janela = Tk()
janela.title("Portal do gerente")
janela.geometry('960x540')
janela.resizable(False, False)

def abrir_tela_cadastro():
    label_nome = Label(janela, text='Nome:')
    label_nome.pack()
    entry_nome = Entry(janela)
    entry_nome.pack()

    label_cpf_ou_cnpj = Label(janela, text='CPF/CNPJ (somente números):')
    label_cpf_ou_cnpj.pack()
    entry_cpf_ou_cnpj = Entry(janela)
    entry_cpf_ou_cnpj.pack()

    label_data_nascimento = Label(janela, text='Data de Nascimento (ex: 01/01/2001):')
    label_data_nascimento.pack()
    entry_data_nascimento = Entry(janela)
    entry_data_nascimento.pack()

    label_telefone = Label(janela, text='Telefone:')
    label_telefone.pack()
    entry_telefone = Entry(janela)
    entry_telefone.pack()

    label_endereco = Label(janela, text='Endereço:')
    label_endereco.pack()
    entry_endereco = Entry(janela)
    entry_endereco.pack()

    label_renda = Label(janela, text='Renda:')
    label_renda.pack()
    entry_renda = Entry(janela)
    entry_renda.pack()

    label_senha = Label(janela, text='Crie a sua senha:')
    label_senha.pack()
    entry_senha = Entry(janela, show='*')
    entry_senha.pack()

    button_frame = Frame(janela)
    button_frame.pack(pady=10)

    button_salvar = Button(janela, text='Cadastrar', command=cadastro_cliente.salvar_cadastro)
    button_salvar.pack(side='top', padx=5)
    button_salvar.place(x=140, y=300)

janela.mainloop()