from tkinter import *
from tkinter import ttk
import math

def temaOscuro():
    estilos.configure('mainframe.TFrame', background="#010924")
    estilos_label1.configure('label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('label2.TLabel', background="#010924", foreground="white")
    
    estilos_numero.configure('Botones_numero.TButton', background="#00044A", foreground="white")
    estilos_numero.map('Botones_numero.TButton', background=[('active', '#020A90')] )
    
    estilos_otros.configure('Botones_OTROS.TButton', background="#010924", foreground="white")
    estilos_otros.map('Botones_OTROS.TButton', background=[('active', '#000AB1')] )

    estilos_borrar.configure('Botones_BORRAR.TButton', background="#010924", foreground="white")
    estilos_borrar.map('Botones_BORRAR.TButton', background=[('active', '#000AB1')] )

def temaClaro():
    estilos.configure('mainframe.TFrame', background="#DBDBDB")
    estilos_label1.configure('label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('label2.TLabel', background="#DBDBDB", foreground="black")
    
    estilos_numero.configure('Botones_numero.TButton', background="#FFFFFF", foreground="black")
    estilos_numero.map('Botones_numero.TButton', background=[("active", "#B9B9B9")])
    
    estilos_otros.configure('Botones_OTROS.TButton', background="#CECECE", foreground="black")
    estilos_otros.map('Botones_OTROS.TButton', background=[("active", "#B9B9B9")])
    
    estilos_borrar.configure('Botones_BORRAR.TButton', background="#CECECE", foreground="black")
    estilos_borrar.map('Botones_BORRAR.TButton', foreground=[("active", "#FF0000")], background=[("active", "#858585")])


def crear_menu(vent):
    barra_menu = Menu(vent)
    vent.config(menu=barra_menu)
    
    menu_inicio = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Salir", command=vent.destroy)

    menu_tema = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Tema", menu=menu_tema)
    menu_tema.add_command(label="Tema Claro", command=temaClaro)
    menu_tema.add_command(label="Tema Oscuro", command=temaOscuro)

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(ventana, style="mainframe.TFrame")
mainframe.grid(row=0, column=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

# Estilos label
estilos_label1 = ttk.Style()
estilos_label1.configure('label1.TLabel', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('label2.TLabel', font="arial 40", anchor="e")

# Entrada
entry1 = StringVar()
label_entry1 = ttk.Label(mainframe, textvariable=entry1, style="label1.TLabel")
label_entry1.grid(row=0, column=0, columnspan=4, sticky=(W, N, E, S))

entry2 = StringVar()
label_entry2 = ttk.Label(mainframe, textvariable=entry2, style="label2.TLabel")
label_entry2.grid(row=1, column=0, columnspan=4, sticky=(W, N, E, S))

# Estilos botones
estilos_numero = ttk.Style()
estilos_numero.configure('Botones_numero.TButton', font="arial22", width=5, background="#FFFFFF", relief="flat")


estilos_borrar = ttk.Style()
estilos_borrar.configure('Botones_BORRAR.TButton', font="arial22", width=5, background="#CECECE", relief="flat")

estilos_otros = ttk.Style()
estilos_otros.configure('Botones_OTROS.TButton', font="arial22", width=5, background="#CECECE", relief="flat")

# Crear botones
button0 = ttk.Button(mainframe, text="0", style="Botones_numero.TButton")
button1 = ttk.Button(mainframe, text="1", style="Botones_numero.TButton")
button2 = ttk.Button(mainframe, text="2", style="Botones_numero.TButton")
button3 = ttk.Button(mainframe, text="3", style="Botones_numero.TButton")
button4 = ttk.Button(mainframe, text="4", style="Botones_numero.TButton")
button5 = ttk.Button(mainframe, text="5", style="Botones_numero.TButton")
button6 = ttk.Button(mainframe, text="6", style="Botones_numero.TButton")
button7 = ttk.Button(mainframe, text="7", style="Botones_numero.TButton")
button8 = ttk.Button(mainframe, text="8", style="Botones_numero.TButton")
button9 = ttk.Button(mainframe, text="9", style="Botones_numero.TButton")

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_BORRAR.TButton")  # Botón para borrar un carácter
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_BORRAR.TButton")  # Botón para borrar todo

button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_OTROS.TButton")  # Paréntesis de apertura
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_OTROS.TButton")  # Paréntesis de cierre
button_punto = ttk.Button(mainframe, text=".", style="Botones_OTROS.TButton")  # Punto decimal

button_division = ttk.Button(mainframe, text=chr(247), style="Botones_OTROS.TButton")  # Botón para división
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones_OTROS.TButton")  # Botón para multiplicación
button_suma = ttk.Button(mainframe, text="+", style="Botones_OTROS.TButton")  # Botón para suma
button_resta = ttk.Button(mainframe, text="-", style="Botones_OTROS.TButton")  # Botón para resta

button_radicacion = ttk.Button(mainframe, text="√", style="Botones_OTROS.TButton")  # Botón para radicación
button_igual = ttk.Button(mainframe, text="=", style="Botones_OTROS.TButton")  # Botón para igual

# Colocar botones en pantalla
button_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))  # Posición del botón de resta

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))  # Posición del botón igual
button_radicacion.grid(column=3, row=7, sticky=(W, N, E, S))  # Posición del botón de radicación

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

# Crear el menú en cascada
crear_menu(ventana)

ventana.mainloop()
