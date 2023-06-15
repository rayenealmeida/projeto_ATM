import os
from datetime import datetime
from library.module import CadastroCliente
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
from tinydb import TinyDB
import os, subprocess, tkinter as tk
from PIL import ImageTk, Image
from tinydb import TinyDB, Query

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco_dados = os.path.join(diretorio_atual, 'banco_de_dados.json')

db = TinyDB(caminho_banco_dados)

cadastro_cliente = CadastroCliente()

def abrir_janela_login():
    janela.destroy()

janela = Tk()
janela.title("Portal do gerente")
janela.geometry('960x540')
janela.resizable(False, False)

imagem = Image.open(diretorio_atual + "/images/portal_gerente.png")
imagem_tk = ImageTk.PhotoImage(imagem)
label = tk.Label(janela, image=imagem_tk).place(x=0, y=-235, relwidth=1, relheight=1)

def abrir_tela_cadastro(user_id, button_cadastrar, button_solicitar_credito, label_msg_head):
    button_cadastrar.destroy()
    button_solicitar_credito.destroy()
    label_msg_head.destroy()

    label_nome = Label(janela, text='Nome:')
    label_nome.place(x=100, y=130)
    entry_nome = Entry(janela)
    entry_nome.place(x=100, y=150)

    label_cpf_ou_cnpj = Label(janela, text='CPF/CNPJ:')
    label_cpf_ou_cnpj.place(x=250, y=130)
    entry_cpf_ou_cnpj = Entry(janela)
    entry_cpf_ou_cnpj.place(x=250, y=150)

    label_data_nascimento = Label(janela, text='Data de Nascimento (ex: 01/01/2001):')
    label_data_nascimento.place(x=400, y=130)
    entry_data_nascimento = Entry(janela)
    entry_data_nascimento.place(x=400, y=150)

    label_telefone = Label(janela, text='Telefone:')
    label_telefone.place(x=100, y=170)
    entry_telefone = Entry(janela)
    entry_telefone.place(x=100, y=190)

    label_endereco = Label(janela, text='Endereço:')
    label_endereco.place(x=250, y=170)
    entry_endereco = Entry(janela)
    entry_endereco.place(x=250, y=190)

    label_renda = Label(janela, text='Renda:')
    label_renda.place(x=400, y=170)
    entry_renda = Entry(janela)
    entry_renda.place(x=400, y=190)

    label_senha = Label(janela, text='Crie a sua senha:')
    label_senha.place(x=100, y=210)
    entry_senha = Entry(janela, show='*')
    entry_senha.place(x=100, y=230)

    button_frame = Frame(janela)
    button_frame.pack(pady=10)

    def exibir_janela_confirmacao():
        janela_confirmacao = tk.Toplevel(janela)
        janela_confirmacao.title("Cadastro Aprovado!")
        janela_confirmacao.geometry("300x100")

        label_confirmacao = tk.Label(janela_confirmacao, text="Cadastro aprovado")
        label_confirmacao.pack(pady=20)

        button_ok = tk.Button(janela_confirmacao, text="OK", command=janela_confirmacao.destroy)
        button_ok.pack()

    def exibir_janela_reprovacao():
        janela_confirmacao = Toplevel(janela)
        janela_confirmacao.title("Cadastro Aprovado!")
        janela_confirmacao.geometry("300x100")

        label_confirmacao = Label(janela_confirmacao, text="Cadastro aprovado")
        label_confirmacao.pack(pady=20)

        button_ok = Button(janela_confirmacao, text="OK", command=janela_confirmacao.destroy)
        button_ok.pack()

    def verificar_campos():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        data_nascimento = entry_data_nascimento.get()
        cpf_ou_cnpj = entry_cpf_ou_cnpj.get()
        endereco = entry_endereco.get()
        renda = entry_renda.get()
        senha = entry_senha.get()
        cpf_ou_cnpj = entry_cpf_ou_cnpj.get()
        cpf_ou_cnpj_num = ''.join(filter(str.isdigit, cpf_ou_cnpj))

        if nome and telefone and data_nascimento and cpf_ou_cnpj_num and endereco and renda and senha:
            try:
                renda = float(renda)
                if cadastro_cliente.salvar_cadastro(nome, telefone, data_nascimento, cpf_ou_cnpj_num, endereco, renda, senha):
                    entry_nome.delete(0, 'end')
                    entry_telefone.delete(0, 'end')
                    entry_data_nascimento.delete(0, 'end')
                    entry_cpf_ou_cnpj.delete(0, 'end')
                    entry_endereco.delete(0, 'end')
                    entry_renda.delete(0, 'end')
                    entry_senha.delete(0, 'end')
                    exibir_janela_confirmacao()
                else:
                    exibir_janela_reprovacao()
            except ValueError:
                import tkinter.messagebox as messagebox
                messagebox.showerror("Erro", "Verifique se completou todos os campos corretamente.")
        else:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    button_salvar = Button(janela, text='Cadastrar', command=verificar_campos)
    button_salvar.pack(side='top', padx=5)
    button_salvar.place(x=100, y=260)


    def voltar_para_painel(user_id):
        entry_nome.destroy()
        entry_telefone.destroy()
        entry_data_nascimento.destroy()
        entry_cpf_ou_cnpj.destroy()
        entry_endereco.destroy()
        entry_renda.destroy()
        entry_senha.destroy()
        label_nome.destroy()
        label_telefone.destroy()
        label_data_nascimento.destroy()
        label_cpf_ou_cnpj.destroy()
        label_endereco.destroy()
        label_renda.destroy()
        label_senha.destroy()
        button_voltar.destroy()
        button_salvar.destroy()

        abrir_painel_gerente(user_id)

    button_voltar = Button(janela, text='Voltar a tela principal', command=lambda: voltar_para_painel(user_id))
    button_voltar.pack(side='top', padx=5)
    button_voltar.place(x=100, y=360)
    


def abrir_painel_gerente(user_id):
    global button_cadastrar
    global button_solicitar_credito
    global label_msg_head
    global button_excluir_cliente
    user = db.get(doc_id=user_id)
    label_msg_head = tk.Label(janela, text= user["nome"].split()[0] + ', escolha uma das opções disponíveis abaixo:', font=('normal', 14))
    label_msg_head.place(x=100, y=130)
    
    button_excluir_cliente = tk.Button(janela, text='Excluir cliente', command=excluir_cliente)
    button_excluir_cliente.place(x=470, y=170)

    button_cadastrar = tk.Button(janela, text= 'Cadastrar cliente', command=lambda: abrir_tela_cadastro(user_id, button_cadastrar, button_solicitar_credito, label_msg_head))
    button_cadastrar.place(x=100, y=170)
    button_solicitar_credito = tk.Button(janela, text= 'Solicitações de crédito', command=abrir_lista_solicitacoes)
    button_solicitar_credito.place(x=260, y=170)
    
def excluir_cliente():
    def confirmar_exclusão():
        cpf_cnpj = entry_cpf_cnpj.get()
        cliente = db.get(Query().cpf == cpf_cnpj)
        if cliente:
            db.remove(doc_ids=[cliente.doc_id])
            label_result_exclusao.configure(text='Cliente excluído com sucesso!')
        else:
            label_result_exclusao.configure(text='Cliente não encontrado.')

    janela_exclusao = tk.Toplevel(janela)
    janela_exclusao.title("Excluir Cliente")
    janela_exclusao.geometry("400x200")

    label_cpf_cnpj = tk.Label(janela_exclusao, text='Informe o CPF/CNPJ do cliente:')
    label_cpf_cnpj.pack(pady=10)

    entry_cpf_cnpj = tk.Entry(janela_exclusao)
    entry_cpf_cnpj.pack()

    button_confirmar = tk.Button(janela_exclusao, text='Confirmar exclusão', command=confirmar_exclusão)
    button_confirmar.pack(pady=10)
    

    label_result_exclusao = tk.Label(janela_exclusao, text='')
    label_result_exclusao.pack(pady=10)
        
def abrir_lista_solicitacoes(db):
    button_cadastrar.destroy()
    button_solicitar_credito.destroy()
    button_excluir_cliente.destroy()
    label_msg_head.destroy()

    solicitacoes = db.search(Query().solicitacao_credito.exists())
   
    if solicitacoes:
        janela_solicitacoes = Toplevel(janela)
        janela_solicitacoes.title("Solicitações de Crédito")
        janela_solicitacoes.geometry("600x400")

        scrollbar = tk.Scrollbar(janela_solicitacoes)
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(janela_solicitacoes, yscrollcommand=scrollbar.set)
        listbox.pack(fill="both", expand=True)

        for solicitacao in solicitacoes:
            nome_cliente = solicitacao['nome']
            cpf_cnpj = solicitacao['cpf']
            renda = solicitacao['renda']
            listbox.insert("end", f"Nome: {nome_cliente} | CPF/CNPJ: {cpf_cnpj} | Renda: {renda}")

        scrollbar.config(command=listbox.yview)

        def aprovar():
            selecionado = listbox.curselection()
            if selecionado:
                solicitacao = solicitacoes[selecionado[0]]
                cpf = solicitacao['cpf']
                valor = solicitacao['valor']
                cliente = db.get(Query().cpf == cpf)
                cliente['credito'] += valor
                db.update(cliente, Query().cpf == cpf)
                db.remove(doc_ids=[solicitacao.doc_id])
                messagebox.showinfo("Aprovação de Crédito", f"Crédito aprovado para o cliente {cliente['nome']}!")
                janela_solicitacoes.destroy()
                
        def rejeitar():
            selecionado = listbox.curselection()
            if selecionado:
                solicitacao = solicitacoes[selecionado[0]]
                cpf = solicitacao['cpf']
                db.remove(doc_ids=[solicitacao.doc_id])
                messagebox.showinfo("Rejeição de Crédito", f"Crédito rejeitado para o cliente com CPF/CNPJ: {cpf}")
                janela_solicitacoes.destroy()
                
        button_aprovar = tk.Button(janela_solicitacoes, text="Aprovar", command=aprovar)
        button_aprovar.pack(side="left", padx=10, pady=10)

        button_rejeitar = tk.Button(janela_solicitacoes, text="Rejeitar", command=rejeitar)
        button_rejeitar.pack(side="left", padx=10, pady=10)         
        
        
    else:
        janela_alerta = Toplevel(janela)
        janela_alerta.title("Sem Solicitações")
        janela_alerta.geometry("300x100")

        label_alerta = Label(janela_alerta, text="Não há solicitações de crédito no momento.")
        label_alerta.pack(pady=20)

        button_ok = Button(janela_alerta, text="OK", command=janela_alerta.destroy)
        button_ok.pack(pady=10)

        janela_alerta.mainloop()

def abrir_login():
    def logar():
        cpf = entry_cpf_login.get()
        senha = entry_senha.get()
        cliente_encontrado = False
        user_id = None

        for cliente in db.all():
            if cliente['cpf'] == cpf and cliente['senha'] == senha and cliente['cadastro_nivel'] == 2:
                cliente_encontrado = True
                user_id = cliente.doc_id
                break

        if cliente_encontrado:
            usuario = db.get(doc_id=user_id)
            if usuario['cadastro_nivel'] == 2:
                destruir_widgets_login()
                abrir_painel_gerente(user_id)
        else:
            label_result_login.configure(text='Suas credenciais estão erradas! Tente novamente.')
        
    def destruir_widgets_login():
        label_msg_head.destroy()
        label_cpf_login.destroy()
        entry_cpf_login.destroy()
        label_senha.destroy()
        entry_senha.destroy()
        button_enter.destroy()
        label_result_login.destroy()

    label_msg_head= tk.Label(janela, text= 'Olá grente, para acessar o sistema, faça o seu login:', font=('normal', 14))
    label_msg_head.place(x=100, y=130)

    label_cpf_login= tk.Label(janela, text='CPF:')
    label_cpf_login.place(x=100, y=160)
    entry_cpf_login = tk.Entry(janela)
    entry_cpf_login.place(x=100, y=180)

    label_senha = tk.Label(janela, text='Senha:')
    label_senha.place(x=100, y=200)
    entry_senha = tk.Entry(janela, show='*')
    entry_senha.place(x=100, y=220)

    button_enter = tk.Button(janela, text= 'Entrar', command=logar)
    button_enter.place(x=100, y=250)

    label_result_login = tk.Label(janela, text='')
    label_result_login.place(x=100, y=280)
    
    
abrir_login()
janela.mainloop()