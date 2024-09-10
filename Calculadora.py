from tkinter import *
from tkinter import ttk
import math

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")

estilos = ttk.Style()
estilos.configure('frame.TFrame', background = "#DBDBDBDB")

frame = ttk.Frame(ventana, style="frame.TFrame")
frame.grid(column=0, row=0)

estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label1.TLabel', font="arial 40", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(frame, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
label_entrada2 = ttk.Label(frame, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

estilos_bottones_numeros=ttk.Style()
estilos_bottones_numeros.configure('Botones_numeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")

estilo_boton_borrar=ttk.Style()
estilo_boton_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")

otros_botones=ttk.Style()
otros_botones.configure('Botones_otros.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")

botton0 = ttk.Button(frame, text="0", style="Botones_numeros.TButton")
botton1 = ttk.Button(frame, text="1", style="Botones_numeros.TButton")
botton2 = ttk.Button(frame, text="2", style="Botones_numeros.TButton")
botton3 = ttk.Button(frame, text="3", style="Botones_numeros.TButton")
botton4 = ttk.Button(frame, text="4", style="Botones_numeros.TButton")
botton5 = ttk.Button(frame, text="5", style="Botones_numeros.TButton")
botton6 = ttk.Button(frame, text="6", style="Botones_numeros.TButton")
botton7 = ttk.Button(frame, text="7", style="Botones_numeros.TButton")
botton8 = ttk.Button(frame, text="8", style="Botones_numeros.TButton")
botton9 = ttk.Button(frame, text="9", style="Botones_numeros.TButton")

botton_borrar = ttk.Button(frame, text=chr(9003), style="Botones_borrar.TButton")
botton_borrar_todo = ttk.Button(frame, text="C", style="Botones_borrar.TButton")
botton_parentesis1 = ttk.Button(frame, text="(", style="Botones_otros.TButton")
botton_parentesis2 = ttk.Button(frame, text=")", style="Botones_otros.TButton")

botton_suma = ttk.Button(frame, text="+", style="Botones_otros.TButton")
botton_resta = ttk.Button(frame, text="-", style="Botones_otros.TButton")
botton_multiplicacion = ttk.Button(frame, text="x", style="Botones_otros.TButton")
botton_division = ttk.Button(frame, text=chr(247), style="Botones_otros.TButton")

botton_igual = ttk.Button(frame, text="=", style="Botones_otros.TButton")         
botton_raiz_cuadrada = ttk.Button(frame, text="√", style="Botones_otros.TButton")

botton_punto = ttk.Button(frame, text=".", style="Botones_otros.TButton")

botton_parentesis1.grid(column=0, row=2)
botton_parentesis2.grid(column=1, row=2)
botton_borrar_todo.grid(column=2, row=2)
botton_borrar.grid(column=3, row=2)

botton7.grid(column=0, row=3)
botton8.grid(column=1, row=3)
botton9.grid(column=2, row=3)
botton_division.grid(column=3, row=3)

botton4.grid(column=0, row=4)
botton5.grid(column=1, row=4)
botton6.grid(column=2, row=4)
botton_multiplicacion.grid(column=3, row=4)

botton1.grid(column=0, row=5)
botton2.grid(column=1, row=5)
botton3.grid(column=2, row=5)
botton_resta.grid(column=3, row=5)

botton0.grid(column=0, row=6, columnspan=2, sticky=(W, E))
botton_punto.grid(column=2, row=6)
botton_suma.grid(column=3, row=6)

botton_raiz_cuadrada.grid(column=3, row=7)

botton_igual.grid(column=0, row=7, columnspan=3, sticky=(W, E))



ventana.mainloop()



