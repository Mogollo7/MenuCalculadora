# Importar las clases necesarias de tkinter
from tkinter import Tk, Label, Button, Entry

def crear_ventana():
    # Configurar colores
    bg_color = "#fdcae1"  # Color de fondo de la ventana y los labels
    fg_color = "#333"     # Color del texto en los labels
    font = ("Arial", 12)  # Fuente y tamaño del texto en los widgets

    # Crear la ventana principal
    vent = Tk()
    vent.title("Calculadora Simple")       # Título de la ventana
    vent.geometry("1000x300")              # Dimensiones de la ventana
    vent.configure(bg=bg_color)            # Configurar el color de fondo
    
    # Función para volver el resultado entero si el residuo es 0
    def formato_resultado(r):
        return int(r) if r % 1 == 0 else r
    
    # Función para sumar los valores de las entradas
    def suma():
        n1 = txt1.get()  # Obtener el texto del primer Entry
        n2 = txt2.get()  # Obtener el texto del segundo Entry
        try:
            r = float(n1) + float(n2)      # Convertir a float y sumar
            r = formato_resultado(r)
            txt3.delete(0, 'end')          # Limpiar el Entry de resultado
            txt3.insert(0, r)              # Insertar el resultado
        except ValueError:                 # Manejo de errores si la conversión falla
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")        # Mostrar "Error" en caso de fallo

    # Función para restar los valores de las entradas
    def resta():
        n1 = txt1.get()  # Obtener el texto del primer Entry
        n2 = txt2.get()  # Obtener el texto del segundo Entry
        try:
            r = float(n1) - float(n2)      # Convertir a float y restar
            r = formato_resultado(r)
            txt3.delete(0, 'end')          # Limpiar el Entry de resultado
            txt3.insert(0, r)              # Insertar el resultado
        except ValueError:                 # Manejo de errores si la conversión falla
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")        # Mostrar "Error" en caso de fallo
            
    def multiplicación():
        n1 = txt1.get()  # Obtener el texto del primer Entry
        n2 = txt2.get()  # Obtener el texto del segundo Entry
        try:
            r = float(n1) * float(n2)      # Convertir a float y multiplica
            r = formato_resultado(r)
            txt3.delete(0, 'end')          # Limpiar el Entry de resultado
            txt3.insert(0, r)              # Insertar el resultado
        except ValueError:                 # Manejo de errores si la conversión falla
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")        # Mostrar "Error" en caso de fallo


    

    

    def salir():
        vent.destroy()

    lbl1 = Label(vent, text="Número 1:", bg=bg_color, fg=fg_color, font=font)
    lbl1.place(relx=0.2, rely=0.1, anchor='center', relwidth=0.3, relheight=0.1)
    txt1 = Entry(vent, bg="#fff")
    txt1.place(relx=0.6, rely=0.1, anchor="center", relwidth=0.3, relheight=0.1)
    
    lbl2 = Label(vent, text="Número 2:", bg=bg_color, fg=fg_color, font=font)
    lbl2.place(relx=0.2, rely=0.3, anchor='center', relwidth=0.3, relheight=0.1)
    txt2 = Entry(vent, bg="#fff")
    txt2.place(relx=0.6, rely=0.3, anchor="center", relwidth=0.3, relheight=0.1)

    lbl3 = Label(vent, text="Resultado:", bg=bg_color, fg=fg_color, font=font)
    lbl3.place(relx=0.2, rely=0.5, anchor='center', relwidth=0.3, relheight=0.1)
    txt3 = Entry(vent, bg="#FFF")
    txt3.place(relx=0.6, rely=0.5, anchor="center", relwidth=0.3, relheight=0.1)

    # Botones para operaciones
    btn_suma = Button(vent, text="Sumar", command=suma, bg="#7fff7f")
    btn_suma.place(relx=0.2, rely=0.7, anchor="center", relwidth=0.3, relheight=0.1)
    
    btn_resta = Button(vent, text="Restar", command=resta, bg="#ff7f7f")
    btn_resta.place(relx=0.6, rely=0.7, anchor="center", relwidth=0.3, relheight=0.1)
    
    btn_multiplicación = Button(vent, text="multiplicación", command=multiplicación, bg="#ff7f7f")
    btn_multiplicación.place(relx=0.2, rely=0.9, anchor="center", relwidth=0.3, relheight=0.1)
    

    # Botón para salir
    btn_salir = Button(vent, text="Salir", command=salir, bg="#d3d3d3")
    btn_salir.place(relx=0.6, rely=0.9, anchor="center", relwidth=0.3, relheight=0.1)

    return vent

vent = crear_ventana()
vent.mainloop()
