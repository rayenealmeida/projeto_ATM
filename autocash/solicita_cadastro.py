import customtkinter

janela = customtkinter.CTk()
janela.geometry("400x300")
janela.grid_columnconfigure(0, weight=1)

def clique():
    print("Solicitar Cadastro")

texto = customtkinter.CTkLabel(janela, text="Solicitar Cadastro")
texto.pack(padx=10, pady=10)

cpf = customtkinter.CTkEntry(janela, placeholder_text= "Seu CPF")
cpf.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, placeholder_text= "Seu nome completo")
nome.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text= "Seu e-mail")
email.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Solicitar", command=clique)
botao.pack(padx=18, pady=18)


janela.mainloop()