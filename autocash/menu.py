import os
import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

janela = tk.Tk()
janela.geometry("600x600")
janela.title("Menu")
janela.resizable(False, False)

imagem = Image.open(diretorio_atual + "/images/atm_bg.png")
imagem = imagem.resize((600, 600), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)

label = Label(janela, image=imagem_tk)
label.place(x=0, y=0, relwidth=1, relheight=1)

janela.mainloop()