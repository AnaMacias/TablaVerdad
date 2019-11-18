from Tkinter import *

root = Tk()

root.geometry("560x80")
root.title("Tabla de Verdad")
root.configure(background="goldenrod")

Valor1 = False
Valor2 = False
Valor3 = False
Resultado = StringVar()

def Calcular():
    if Spinbox1.get() == "Verdadero":
        Valor1 = True
    else:
        Valor1 = False

    if Spinbox2.get() == "Verdadero":
        Valor2 = True
    else:
        Valor2 = False

    if Spinbox3.get() == "^":
        Valor3 = Valor1 and Valor2

    if Spinbox3.get() == "v":
        Valor3 = Valor1 or Valor2

    if Spinbox3.get() == "->":
        if Valor1 == True and Valor2 == True:
            Valor3 = True
        elif Valor1 == True and Valor2 == False:
            Valor3 = False
        elif Valor1 == False and Valor2 == True:
            Valor3 = True
        elif Valor1 == False and Valor2 == False:
            Valor3 = True
    
    if Spinbox3.get() == "<->":
        if Valor1 == True and Valor2 == True:
            Valor3 = True
        elif Valor1 == True and Valor2 == False:
            Valor3 = False
        elif Valor1 == False and Valor2 == True:
            Valor3 = False
        elif Valor1 == False and Valor2 == False:
            Valor3 = True

    if Valor3 == True:
        Resultado.set("Verdadero")
    else:
        Resultado.set("Falso")

MyFrame = Frame(root, width = 1300, height = 600)
MyFrame.pack()

MyFrame.configure(background="goldenrod")

Label1 = Label(MyFrame, text = "P", bg="goldenrod", width = 13)
Label1.grid(row = 0, column = 0)

Label2 = Label(MyFrame, text = "Q", bg="goldenrod", width = 13)
Label2.grid(row = 0, column = 1)

Label3 = Label(MyFrame, text = "Simbolo", bg="goldenrod", width = 13)
Label3.grid(row = 0, column = 2)

Label4 = Label(MyFrame, text = "Resultado", bg="goldenrod", width = 13)
Label4.grid(row = 0, column = 4)

Spinbox1 = Spinbox(MyFrame, values=("Verdadero", "Falso"), width = 10)
Spinbox1.grid(row = 1, column = 0)

Spinbox2 = Spinbox(MyFrame, values=("Verdadero", "Falso"), width = 10)
Spinbox2.grid(row = 1, column = 1)

Spinbox3 = Spinbox(MyFrame, values=("^","v","->","<->"), width = 10)
Spinbox3.grid(row = 1, column = 2)

Button1 = Button(MyFrame, text ="Calcular", command=Calcular)
Button1.grid(row = 1, column = 3)

Label5 = Label(MyFrame, textvariable = Resultado, borderwidth=1, relief=SOLID, width = 10)
Label5.grid(row = 1, column = 4)

root.mainloop()