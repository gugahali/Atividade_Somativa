from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

#Criando janela
janela = Tk()
janela.title('Sistema de Registro Alunos')
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width= FALSE, height= FALSE)

style = Style(janela)
style.theme_use('clam')

#Criando Frames
frame_logo = Frame(janela, width=850, height=53, bg=co6 )
frame_logo.grid(row=0,column=0,padx=0,pady=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1,relief=RAISED )
frame_botoes.grid(row=1,column=0,padx=0,pady=1, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1,column=1,padx=10,pady=1, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3,column=0,padx=10,pady=0, sticky=NSEW,columnspan=5)

#trabalhando na logo
global image, image_string, l_image

app_lg = Image.open('App_logo.jpg')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text='Sistema de registro de Alunos', width=850 , compound=LEFT, anchor= NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place (x=5, y=0)

#Criando Local dos Dados

l_nome = Label(frame_detalhes,  text= 'Nome *', anchor= NW, font=('Ivy 10'), bg=co1, fg=co6)
l_nome.place(x=4,y=10)
e_nome = Entry(frame_detalhes, width=30, justify= 'left', relief=SOLID)
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes,  text= 'Email *', anchor= NW, font=('Ivy 10'), bg=co1, fg=co6)
l_email.place(x=4,y=70)
e_email = Entry(frame_detalhes, width=30, justify= 'left', relief=SOLID)
e_email.place(x=7, y=100)

l_matricula = Label(frame_detalhes,  text= 'Matricula *', anchor= NW, font=('Ivy 10'), bg=co1, fg=co6)
l_matricula.place(x=4,y=130)
e_matricula = Entry(frame_detalhes, width=15, justify= 'left', relief=SOLID)
e_matricula.place(x=7, y=160)

l_turma = Label(frame_detalhes,  text= 'Turma *', anchor= NW, font=('Ivy 10'), bg=co1, fg=co6)
l_turma.place(x=30,y=190)







janela.mainloop()
