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

button_login = tk.Button(janela, text= '1')
button_login.pack()
button_login.place(x=117, y=404)

button_login = tk.Button(janela, text= '2')
button_login.pack()
button_login.place(x=170, y=404)

button_login = tk.Button(janela, text= '3')
button_login.pack()
button_login.place(x=223, y=404)

button_login = tk.Button(janela, text= '4')
button_login.pack()
button_login.place(x=117, y=440)

button_login = tk.Button(janela, text= '5')
button_login.pack()
button_login.place(x=170, y=440)

button_login = tk.Button(janela, text= '6')
button_login.pack()
button_login.place(x=223, y=440)

button_login = tk.Button(janela, text= '7')
button_login.pack()
button_login.place(x=117, y=476)

button_login = tk.Button(janela, text= '8')
button_login.pack()
button_login.place(x=170, y=476)

button_login = tk.Button(janela, text= '9')
button_login.pack()
button_login.place(x=223, y=476)

button_login = tk.Button(janela, text= '0')
button_login.pack()
button_login.place(x=170, y=512)

janela.mainloop()