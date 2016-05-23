import time
import math
from tkinter import *
import tkinter.messagebox
#Funciones de ventanas
def mostrar(win):
    win.deiconify()
    ventana.withdraw()
#------------------------
#Funcion para volver al menu
def ocultar():
    answer2= tkinter.messagebox.askquestion("ColorSwitchPinball", "Seguro que desea regresar al menu?")
    if answer2=="yes":
        win.withdraw()
        ventana.deiconify()
#-------------------------
#funcion para pasar sdel registro de nombre a la ventana del juego     
def mostrarp ():
    mostrar(win)
    saludo.withdraw()
    label2.config(text=" "+entry.get())
#--------------------------
#Funcion que me permite salir del juego, luego de responder el messagebox
def salir():
    answer= tkinter.messagebox.askquestion ("ColorSwitchPinball","Seguro que desea salir?")
    if answer == "yes":
        ventana.destroy()
#-------------------------
#Funcion para pasar del menu al registro del nombre
def name():
    saludo.deiconify()
    ventana.withdraw()
#-------------------------
#Funcion para guardar el archivo de la partida en un archivo.txt
def guardarPartida():
    global label2
    name=input("Ingrese el nombre de la partida a guardar : ")
    archi = open("./" + name+".txt","w")
    nombre= entry.get()
    puntos="1000"
    vidas="2"
    archi.write(nombre+'\n')
    archi.write(puntos+'\n')
    archi.write(vidas+'\n')
    archi.close()
def Usuario():
    Musuario.deiconify()
    ventana.withdraw()
def Usuario2():
    ventana.deiconify()
    Musuario.withdraw()
#--------------------
#Declaracion de ventanas
ventana=Tk()
saludo=Tk()
win=Tk()
Musuario= Toplevel()
#--------------------
#Creacion ventana principal
a=canvas2= Canvas(win,width=550,height=530,bg="grey")
canvas2.place(x=10,y=35)
#---------------------
#definicion de mapa y movimiento de palancas
triangulo1=canvas2.create_polygon(0,30,100,30,0,100,fill="black")
triangulo2=canvas2.create_polygon(700,30,600,30, 700,100,fill="black")
rectangulo1=canvas2.create_polygon(0,0,700,0, 700,40,0,40,fill="black")
poligono1=canvas2.create_polygon(250,610,260,630,300,630,310,620,fill="black")
poligono2=canvas2.create_polygon(450,610,440,630,400,630,390,620,fill="black")
poligono3=canvas2.create_polygon(468,750,488,610,488,250,518,250,518,630,408,630,fill="black")
poligono7=canvas2.create_polygon((62,122),(111,64),(133,70),(75,129),fill="brown")
obstaculo1=canvas2.create_polygon((112,63),(107,71),(136,92),(147,75),fill="orange")                               
obstaculo2=canvas2.create_polygon((41,363),(53,417),(106,431), fill="white")
obstaculo3=canvas2.create_polygon((235,53),(278,45),(320,74),fill="blue")
#Borde izquierdo
poligono9=canvas2.create_polygon((4,98),(44,173),(2,274),fill="black")
poligonon10=canvas2.create_polygon((4,270),(39,339),(2,391),fill="black")
#Palancas y su movimiento.
def pl1():
    global canvas2,palanca1
    palanca1= canvas2.create_polygon((230,455),(120,435),(140,450),fill="red")
def pl11():
    global canvas2,palanca1
    palanca1=canvas2.create_polygon((120,435),(150,345),(140,425),fill="purple")
def pl1actualizado():
    global canvas2,palanca1
    canvas2.delete(palanca1)
    pl1()
def pl2():
    global canvas2,palanca2
    palanca2=canvas2.create_polygon((265,455),(375,435),(355,450),fill="blue")
def pl22():
    global canvas2, palanca2
    palanca2= canvas2.create_polygon((375,435),(345,335),(355,425),fill="yellow")
def pl2actualizado():
    global canvas2, palanca2
    canvas2.delete(palanca2)
    pl2()
    

#Definicion de la bola
circulo=canvas2.create_oval(310,310,280, 280,  fill="red")

canvas2.move(circulo, 240,210)    
#Movimiento de la bola y aplicacion de gravedad
seEjecuto2 = False
contador2 = 0
def aplicaGravedad():
    global circulo

    canvas2.move(circulo, 0, 3)
    canvas2.after(1, aplicaGravedad)
    

dx = -1
dy = 0
xSpeed = 3
ySpeed = 3
puntos=0
def mirarColisiones():
    global dx, dy, puntos
    x1, y1, x2, y2 = canvas2.coords(circulo)
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    


    if (x < 30):
        dx = 1
    if (x > 535):
        dx = -1

    if (y < 60):
        dy = 1
    if (y > 515):
        dy = -1

    
        
    xSpeed = 3
    ySpeed = 6

    if x >= 61 and x <= 134 and y >= 61 and y <= 136:
        dy *= -1
        dx *= -1
        xSpeed = 4
        puntos+=100
    #Colision rectangulo negro derecha
    if x >= 488 and x<= 554 and y >= 253 and y <= 534:
        dy*=1
        dx*=-1
    #Colision obstaculo 2(blanco izquierdo)
    if x >= 31 and x<= 122 and y >= 366 and y <= 436:
        dy*=-1
        dx=1
   
    #Colision complemento derecho de palanca
    if x >=371 and x<= 487 and y >= 431 and y <= 457:
        dy*=-1
        dx=-1
   #Colision obstaculo3 (azul)
    if x >= 230 and x<= 325 and y >= 40 and y <= 88:
        dy*=1
        dx=-1
    if (dy == 1):
        ySpeed = 3
        
    canvas2.move(circulo, dx * xSpeed, dy * ySpeed)
    canvas2.after(1, mirarColisiones)

#print (puntos)
        


    
def moverIzquierda():
    global circulo, contador2, seEjecuto2
    if (contador2 >= 45):
        if (not seEjecuto2):
            aplicaGravedad()
            mirarColisiones()
            seEjecuto2 = True
        return
    
    canvas2.move(circulo, -2, 0.5)
    contador2 += 1
    canvas2.after(15, moverIzquierda)
    
contador = 0
seEjecuto = False
inicio = False

def moverBola():
    global circulo, contador, seEjecuto
    
    if (contador >= 90):
         
        if (not seEjecuto):
            moverIzquierda()
            seEjecuto = True
        return
    
    canvas2.move(circulo, 0, -5)
    contador += 1
    canvas2.after(50, moverBola)
#Eventos de teclado para movimiento de palancas y la bola    
def teclas(event):
    global canvas2,palanca1,palanca2, inicio
    key=repr(event.char)
    if key=="'z'":
        canvas2.delete(palanca1)
        canvas2.after(0,pl11)
        canvas2.after(300,pl1actualizado)
    if key =="'m'":
        canvas2.delete(palanca2)
        canvas2.after(0,pl22)
        canvas2.after(300,pl2actualizado)
    if key == "'l'" and not inicio:
        moverBola()
        inicio = True
        
def mouse(event):
    print ("clicked at", event.x, event.y)

#Complemento de palancas y desarrolo del mapa   
complmentopalanca1=canvas2.create_polygon((2,434),(4,455),(138,450),(120,436),fill="orange")
complementopalanca2=canvas2.create_polygon((488,433),(375,436),(355,452),(488,456),fill="red")
canvas2.bind_all("<Key>",teclas)
canvas2.bind("<Button-1>", mouse)
canvas2.focus_set()
pl1()
pl2()
#Definicion de propiedades de ventan principal
win.geometry("800x600+0+0")
win.config(bg="grey")
win.title("Color Switch Pinball")
#Labels de nombres del jugador, botones en la ventana principal y demas
label1= Label(win,text="Jugador:",bg="grey",fg="red",font=('Ravie',20))
label1.place(x=570,y=250)
label3= Label ( win, text=" Vidas:", bg= "grey", fg= "red", font=( 'Ravie', 20))
label3.place(x=570, y=320)
label4= Label(win, text= "3", bg= "grey", fg ="black", font=('Ravie', 20))
label4.place(x=570, y=350)
label2=Label(win,text=" ",bg="grey",font=('Ravie',20))
label2.place(x=570,y=285)
imgButton2= PhotoImage(master = win, file="imgBoton.gif")
volver= Button(win,text="Volver al  menu",bg="grey", command= ocultar)
volver.place(x=570,y=480)
guardarPartida= Button(win, text="Guardar Partida", bg="grey", command= guardarPartida)
guardarPartida.place(x=570,y=520)
win.withdraw()
#Nombre
saludo.config(bg="black")
saludo.title("Pinball")
frame=Frame(saludo)
frame.pack()
label1= Label(frame,text="Digita tu nombre:",fg="red")
label1.pack()
entry= Entry(frame)
entry.pack()
con=Button(frame,text="Continuar..",command=mostrarp)
con.pack()
saludo.withdraw()
#Manual de usuario
Musuario.config(bg="black")
Musuario.title("ColorSwitch--Manual de Usuario")
Musuario.geometry("400x400+0+0")
canvas3= Canvas(Musuario, width=350, height=200, bg="black")
canvas3.pack()
label= Label(canvas3,fg="white", text="Bienvenido a este juego creado para tu diversion. \n"
             "Como bien sabes las relgas son las clasicas del   \n"
             "pinball, tienes 3 bolas o 3 vidas para lograr la    \n"
             "mayoria de puntos. Debes oprimir la letra <L> para \n"
             "lanzar la bola y la tecla <Z > para activar la palanca\n"
             "izquierda y la tecla < M > para  activar la  palanca    \n"
             "derecha, si la bola cae en el vacio entre las palancas \n "
             "perderas una vida, cuando pierdas las 3  vidas \n"
             "habras perdido el juego. Cuando la bola colisione\n"
             "ganaras puntos y cada mil puntos obtendras una \n"
             "nueva vida",bg="black")
label.place(x=5,y=5)
img= PhotoImage(file="good.gif")
suerte=Label(Musuario, image=img).place(x=142,y=235)
texto=Label(Musuario, text="Buena suerte!!",fg="white",bg="black", font=('Ravie', 20))
texto.place(x=120, y=320)
BackMenu=Button(Musuario, text="Volver al menu", bg="black", fg="white", command=Usuario2)
BackMenu.place(x=135,y=360)
Musuario.withdraw()
#Creacion ventana bienvenida
ventana.geometry("945x532")
ventana.title("Pinball")
imagen2= PhotoImage(file="INICIO.gif")
lblImagen2=Label(ventana,image=imagen2).place(x=0,y=0)
imgButton=PhotoImage(file="imgBoton.gif")
boton1=Button(ventana,image=imgButton,command=name,bg="grey")
boton1.place(x=250,y=450)
imgButton2=PhotoImage(file="salirBoton.gif")
boton2=Button(ventana,image=imgButton2,command=salir,bg="grey")
boton2.place(x=650,y=450)
imgButton3= PhotoImage(file="iconomanual.gif")
botonusu= Button(ventana, image=imgButton3, command= Usuario, bg="grey")
botonusu.place(x=450, y=450)
ventana.mainloop()
win.mainloop()
Musuario.mainloop()

