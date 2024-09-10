from tkinter import *
from tkinter import ttk

# Función para procesar la entrada del botón
def agregar_caracter(caracter):
    actual = entrada2.get()
    entrada2.set(actual + str(caracter))

# Función para evaluar la expresión y mostrar el resultado
def evaluar():
    try:
        # Reemplaza símbolos y evalúa respetando la prioridad de operaciones
        expresion = entrada2.get()
        # Remplazar x por * y ÷ por /
        expresion = expresion.replace('x', '*').replace('÷', '/')
        resultado = eval(expresion)
        entrada1.set(entrada2.get())  # Muestra la expresión en el label pequeño
        entrada2.set(str(resultado))  # Muestra el resultado en el label grande
    except Exception as e:
        entrada2.set("Error")

# Función para borrar el último carácter y restaurar la operación anterior en Label2
def borrar():
    if entrada2.get() == "":  # Si no hay nada en Label2, se restaura lo que había en Label1
        entrada2.set(entrada1.get())
    else:
        entrada2.set(entrada2.get()[:-1])

# Función para borrar toda la entrada
def borrar_todo():
    entrada1.set("")  # Borra la operación anterior
    entrada2.set("")  # Borra el resultado actual

# Funciones para agregar caracteres específicos
def agregar_parentesis_izquierdo():
    agregar_caracter('(')

def agregar_parentesis_derecho():
    agregar_caracter(')')

def agregar_suma():
    agregar_caracter('+')

def agregar_resta():
    agregar_caracter('-')

def agregar_multiplicacion():
    agregar_caracter('x')

def agregar_division():
    agregar_caracter('÷')

def agregar_punto():
    agregar_caracter('.')

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")

# Estilos
estilos = ttk.Style()
estilos.configure('frame.TFrame', background="#DBDBDB")

frame = ttk.Frame(ventana, style="frame.TFrame")
frame.grid(column=0, row=0)

estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

# Variable para los labels
entrada1 = StringVar()  # Label pequeño (expresión anterior)
label_entrada1 = ttk.Label(frame, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()  # Label grande (resultado actual)
label_entrada2 = ttk.Label(frame, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

# Estilos de los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")

estilo_boton_borrar = ttk.Style()
estilo_boton_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")

otros_botones = ttk.Style()
otros_botones.configure('Botones_otros.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")

# Creación de botones
botones_numeros = [ttk.Button(frame, text=str(i), style="Botones_numeros.TButton", command=lambda i=i: agregar_caracter(i)) for i in range(10)]

botton_borrar = ttk.Button(frame, text=chr(9003), style="Botones_borrar.TButton", command=borrar)
botton_borrar_todo = ttk.Button(frame, text="C", style="Botones_borrar.TButton", command=borrar_todo)
botton_parentesis1 = ttk.Button(frame, text="(", style="Botones_otros.TButton", command=agregar_parentesis_izquierdo)
botton_parentesis2 = ttk.Button(frame, text=")", style="Botones_otros.TButton", command=agregar_parentesis_derecho)

botton_suma = ttk.Button(frame, text="+", style="Botones_otros.TButton", command=agregar_suma)
botton_resta = ttk.Button(frame, text="-", style="Botones_otros.TButton", command=agregar_resta)
botton_multiplicacion = ttk.Button(frame, text="x", style="Botones_otros.TButton", command=agregar_multiplicacion)
botton_division = ttk.Button(frame, text=chr(247), style="Botones_otros.TButton", command=agregar_division)

botton_igual = ttk.Button(frame, text="=", style="Botones_otros.TButton", command=evaluar)
botton_punto = ttk.Button(frame, text=".", style="Botones_otros.TButton", command=agregar_punto)

# Posicionamiento de botones
botton_parentesis1.grid(column=0, row=2)
botton_parentesis2.grid(column=1, row=2)
botton_borrar_todo.grid(column=2, row=2)
botton_borrar.grid(column=3, row=2)

botones_numeros[7].grid(column=0, row=3)
botones_numeros[8].grid(column=1, row=3)
botones_numeros[9].grid(column=2, row=3)
botton_division.grid(column=3, row=3)

botones_numeros[4].grid(column=0, row=4)
botones_numeros[5].grid(column=1, row=4)
botones_numeros[6].grid(column=2, row=4)
botton_multiplicacion.grid(column=3, row=4)

botones_numeros[1].grid(column=0, row=5)
botones_numeros[2].grid(column=1, row=5)
botones_numeros[3].grid(column=2, row=5)
botton_resta.grid(column=3, row=5)

botones_numeros[0].grid(column=0, row=6, columnspan=2, sticky=(W, E))
botton_punto.grid(column=2, row=6)
botton_suma.grid(column=3, row=6)

botton_igual.grid(column=0, row=7, columnspan=4, sticky=(W, E))

ventana.mainloop()
