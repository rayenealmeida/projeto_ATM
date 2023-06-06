import os
import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
import subprocess

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

janela_menu = tk.Tk()
janela_menu.geometry("600x600")
janela_menu.title("Menu")
janela_menu.resizable(False, False)

imagem = Image.open(diretorio_atual + "/images/atm_bg.png")
imagem = imagem.resize((600, 600), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)

label = Label(janela_menu, image=imagem_tk)
label.place(x=0, y=0, relwidth=1, relheight=1)

opcoes_texto = "Menu:\n\n1 - Extrato\n2 - Saque\n3 - Depósito\n4 - Realizar pagamento\n5 - Solicitar crédito\n6 - Sair\n\nEntre com a sua opção: _ "

label_opcoes = Label(janela_menu, text=opcoes_texto, font=("Consolas", 14), justify="left", bg="#50c7e2")
label_opcoes.pack()
label_opcoes.place(x=70, y=90)

def abrir_saque():
    janela_menu.destroy()
    subprocess.run(['python', diretorio_atual + '/saque.py'])

    
button_menu = tk.Button(janela_menu, text= '1', width=2)
button_menu.pack()
button_menu.place(x=113, y=404)

button_menu = tk.Button(janela_menu, text= '2', width=2, command=abrir_saque)
button_menu.pack()
button_menu.place(x=166, y=404)

button_menu = tk.Button(janela_menu, text= '3', width=2)
button_menu.pack()
button_menu.place(x=219, y=404)

button_menu = tk.Button(janela_menu, text= '4', width=2)
button_menu.pack()
button_menu.place(x=113, y=440)

button_menu = tk.Button(janela_menu, text= '5', width=2)
button_menu.pack()
button_menu.place(x=166, y=440)

button_menu = tk.Button(janela_menu, text= '6', width=2)
button_menu.pack()
button_menu.place(x=219, y=440)

button_menu = tk.Button(janela_menu, text= '7', width=2)
button_menu.pack()
button_menu.place(x=113, y=476)

button_menu = tk.Button(janela_menu, text= '8', width=2)
button_menu.pack()
button_menu.place(x=166, y=476)

button_menu = tk.Button(janela_menu, text= '9', width=2)
button_menu.pack()
button_menu.place(x=219, y=476)

button_menu = tk.Button(janela_menu, text= '0', width=2)
button_menu.pack()
button_menu.place(x=166, y=512)

janela_menu.mainloop()