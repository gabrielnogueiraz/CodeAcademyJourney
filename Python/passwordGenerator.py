from tkinter import *
from tkinter import ttk


co0 = "#444466"  
co1 = "#feffff"  
co2 = "#f05a43"  

janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.configure(bg=co1)

janela.mainloop()
frame_cima = Frame(janela, width=280, height=50,bg=co1, pady=0, padx=0, relief="flat",)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=280, height=310,bg=co1, pady=0, padx=0, relief="flat",)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

style = ttk.Style(janela)
style.theme_use("clam")

from PIL import ImageTk, Image

img_0 = Image.open('password.png')
img_0 = img_0.resize((30, 30), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

app_imagem = Label(frame_cima,  height=60, image=img_0, compound=LEFT,padx=10, relief="flat", anchor="nw", font=('Ivy 16 bold'), bg=co1)
app_imagem.place(x=2, y=0)
app_name = Label(frame_cima, text="GERADOR DE SENHAS", width=20, height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 16 bold'), bg=co1, fg=co0)
app_name.place(x=35, y=2)

app_linha = Label(frame_cima, text="", width=290, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

app_senha = Label(frame_baixo , text="- - -", width=26, height=2, padx=0, relief="solid", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
app_senha.grid(row=0, column=0, columnspan=1,  sticky=NSEW, pady=10, padx=3)

var =IntVar()
var.set(8)
app_info = Label(frame_baixo, text="Número total de caracteres na senha", height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=1, column=0, columnspan=2,  sticky=NSEW, pady=1, padx=5)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, sticky=NW, pady=5, padx=8)

import random
import string

alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = '123456789'
simbolos = "[]{}()*;/,_-"

frame_caracters = Frame(frame_baixo, width=280, height=210,bg=co1, pady=0, padx=0, relief="flat",)
frame_caracters.grid(row=3, column=0, sticky=NSEW)

estado_1 = StringVar()
estado_1.set(False)  # set check state
chek_1 = Checkbutton(frame_caracters,width=1, var=estado_1,onvalue=alfabeto_mais, offvalue='off', bg=co1)
chek_1.grid(row=0, column=0,  sticky=NW, pady=5, padx=2)

app_info = Label(frame_caracters, text="ABC Letras maiúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=0, column=1,  sticky=NW, pady=5, padx=2)
    
# ------------ Letras minúsculas ------------------
estado_2 = StringVar()
estado_2.set(False)  # set check state
chek_2 = Checkbutton(frame_caracters,width=1, var=estado_2,onvalue=alfabeto_menos, offvalue='off',bg=co1)
chek_2.grid(row=1, column=0,  sticky=NW, pady=5, padx=2)


app_info = Label(frame_caracters, text="abc Letras minúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=1, column=1,  sticky=NW, pady=5, padx=2)
    
estado_3 = StringVar()
estado_3.set(False)  # set check state
chek_3 = Checkbutton(frame_caracters,width=1, var=estado_3,onvalue=numeros, offvalue='off',bg=co1)
chek_3.grid(row=2, column=0,  sticky=NW, pady=5, padx=2)


app_info = Label(frame_caracters, text="123 Números",height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=2, column=1,  sticky=NW, pady=5, padx=2)

estado_4 = StringVar()
estado_4.set(False)  # set check state
chek_4 = Checkbutton(frame_caracters,width=1, var=estado_4, onvalue=simbolos, offvalue='off',bg=co1)
chek_4.grid(row=3, column=0,  sticky=NW, pady=1, padx=2)

app_info = Label(frame_caracters, text="!@# Símbolos", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=3, column=1,  sticky=NW, pady=1, padx=2)

# ------------ Botao gerar senha ------------------
b_gerar_senha = Button(frame_box, command=criar_senha, text="Gerar senha",width=32, height=1, overrelief=SOLID,  bg=co3, fg="white", font=('Ivy 10 bold'), anchor="center", relief=FLAT )
b_gerar_senha.grid(row=5, column=0,  sticky=NSEW, pady=20, padx=0, columnspan=5)

b_copiar = Button(frame_baixo, text="Copiar",width=7, height=2, overrelief=SOLID,  bg=co1, fg=co0, font=('Ivy 10 bold'), anchor="center", relief=RAISED )
b_copiar.grid(row=0, column=1, columnspan=1,  sticky=NW, pady=10, padx=5)

def criar_senha():
    alfabeto_menos = string.ascii_lowercase
    alfabeto_mais = string.ascii_uppercase
    numeros = '123456789'
    simbolos = "[]{}()*;/,_-"
    
    global combinar
    
    if estado_1.get() == alfabeto_mais:
        combinar = alfabeto_mais
    else:
        pass
    
    if estado_2.get() == alfabeto_menos:
        combinar = combinar + alfabeto_menos
    else:
        pass
    
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass
    
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass
    
    comprimento = int(spin.get())
    
    senha = "".join(random.sample(combinar, comprimento))
    
    app_senha['text'] = senha
    
    def copiar_senha():
        info = senha
        frame_box.clipboard_clear()
        frame_box.clipboard_append(info)
        messagebox.showinfo("Sucesso","A senha foi copiada com sucesso") 
        
    b_copiar = Button(frame_box, command=copiar_senha, text="Copiar",width=7, height=1, overrelief=SOLID,  bg=co1, fg=co0, font=('Ivy 10 bold'), anchor="center", relief=RAISED )
    b_copiar.grid(row=0, column=2, columnspan=2,  sticky=NSEW, pady=10, padx=1)