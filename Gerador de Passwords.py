from tkinter import *
from tkinter import ttk, messagebox

#from PIL import ImageTk,Image
import random
import string
import tkinter as tk


cor0='#17BEBB'  # letras
cor1='#D4F4DD'  # fundo
cor2='#70A288' # detalhe

janela=Tk()
janela.geometry('295x360')
janela.title('Password Generator')
janela.configure(bg=cor1)



#dividir a tela em dois frames
frame_cima= Frame(janela, width=295, height=50, bg=cor1,pady=0,padx=0,relief='flat')
frame_cima.grid(row=0,column=0,sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=310, bg=cor1,pady=0,padx=0,relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NSEW)

estilo_janela=ttk.Style(janela)
estilo_janela.theme_use('clam')

#trabalhar no frame cima

app_logo=Label(frame_cima, height=60, compound="left", pady=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2,y=0)

app_nome=Label(frame_cima, text='Password Generator', width=20,height=1, padx=0, relief='flat', anchor='nw', bg=cor1,font=('Ivy 16 bold'))
app_nome.place(x=35,y=4)

app_linha=Label(frame_cima, text='', width=295,height=1, padx=0, relief='flat', anchor='nw', bg=cor2,font=('Ivy 1'))
app_linha.place(x=0,y=35)

#funcao gerar senha

def password_generator():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = ('123456789')
    simbolos = '[]{}()*;/,_-'

    global combinar

    #condicao para maiuscula
    if estado_1.get() == alfabeto_maior:
        combinar= alfabeto_maior
    else:
        pass
    if estado_2.get() == alfabeto_menor:
        combinar= combinar+ alfabeto_menor
    else:
        pass
    if estado_3.get() == numeros:
        combinar= combinar+numeros
    else:
        pass
    if estado_4.get() == simbolos:
        combinar= combinar+simbolos
    else:
        pass




    comprimento=int(spin.get())


    password=''.join(random.sample(combinar,comprimento))
    app_senha['text']= password

def copiar_password():
    senha=app_senha
    frame_baixo.clipboard_clear()
    frame_baixo.clipboard_append(senha)
    messagebox.showinfo('Sucesso','Copia da password com sucesso')

    botao_copiar_senha = Button(frame_baixo,command=copiar_password, text='Copiar', width=6, height=2, overrelief='solid', relief='raised',
                                    anchor='center', bg=cor1, font=('Ivy 10 bold '), fg=cor0)
    botao_copiar_senha.grid(row=0, column=1, sticky=NW, pady=10, padx=5, columnspan=1)

#frame baixo

app_senha=Label(frame_baixo, text='- - -', width=21,height=2, padx=0, relief='solid', anchor='center', bg=cor1,font=('Ivy 12 bold'))
app_senha.grid(row=0,column=0, columnspan=1, sticky=NSEW, pady=10, padx=3)

app_info=Label(frame_baixo, text='Nº Total de Caracteres de Password',height=1, padx=0, relief='flat', anchor='nw', bg=cor1,font=('Ivy 10'))
app_info.grid(row=1,column=0, columnspan=2, sticky=NSEW, pady=1, padx=5)

var=IntVar()
var.set(8)
spin= Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, pady=8, padx=5)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = ('123456789')
simbolos = '[]{}()*;/,_-'

frame_caracteres= Frame(frame_baixo, width=295, height=210, bg=cor1,pady=0,padx=0,relief='flat')
frame_caracteres.grid(row=3,column=0,sticky=NSEW,columnspan=3)

estado_1= StringVar()
estado_1.set(False) # nao esta marcado
check_1=Checkbutton(frame_caracteres, width=1, var= estado_1, onvalue= alfabeto_maior, offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=0,column=0, padx=2, pady=5,sticky=NW)
app_info=Label(frame_caracteres, text='ABC letras maiusculas',height=1, padx=0, relief='flat', anchor='nw', bg=cor1,font=('Ivy 10 '))
app_info.grid(row=0,column=1, sticky=NW, pady=5, padx=2)

estado_2= StringVar()
estado_2.set(False) # nao esta marcado
check_2=Checkbutton(frame_caracteres, width=1, var= estado_2, onvalue= alfabeto_menor, offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=1,column=0, padx=2, pady=5,sticky=NW)
app_info=Label(frame_caracteres, text='abc letras minusculas',height=1, padx=0, relief='flat', anchor='nw', bg=cor1,font=('Ivy 10 '))
app_info.grid(row=1,column=1, sticky=NW, pady=5, padx=2)

estado_3= StringVar()
estado_3.set(False) # nao esta marcado
check_3=Checkbutton(frame_caracteres, width=1, var= estado_3, onvalue= numeros, offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=2,column=0, padx=2, pady=5,sticky=NW)
app_info=Label(frame_caracteres, text='123 numeros',height=1, padx=0, relief='flat', anchor='nw', bg=cor1,font=('Ivy 10 '))
app_info.grid(row=2,column=1, sticky=NW, pady=5, padx=2)

estado_4= StringVar()
estado_4.set(False) # nao esta marcado
check_4=Checkbutton(frame_caracteres, width=1, var= estado_4, onvalue= simbolos, offvalue='off', relief='flat', bg=cor1)
check_4.grid(row=3,column=0, padx=2, pady=5,sticky=NW)
app_info=Label(frame_caracteres, text='Simbolos',height=1, padx=0, relief='flat', anchor='nw', bg=cor1,font=('Ivy 10 '))
app_info.grid(row=3,column=1, sticky=NW, pady=5, padx=2)

#botao



botao_gerar_senha=Button(frame_caracteres,command=password_generator, text='Gerar Password', width=34, height=1,overrelief='solid', relief='flat', anchor='center', bg=cor2,font=('Ivy 10 bold '),fg=cor1)
botao_gerar_senha.grid(row=5,column=0, sticky=NSEW, pady=11, padx=5, columnspan=5)

botao_copiar_senha = Button(frame_baixo,command=copiar_password, text='Copiar', width=6, height=2, overrelief='solid', relief='raised',
                                    anchor='center', bg=cor1, font=('Ivy 10 bold '), fg=cor0)
botao_copiar_senha.grid(row=0, column=1, sticky=NW, pady=10, padx=5, columnspan=1)








janela.mainloop()
