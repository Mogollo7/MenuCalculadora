from tkinter import *
from tkinter import ttk
import math
import subprocess
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
    menu_inicio.add_command(label="Ejecutar Calculadora", command=ejecutar_otro_programa)
    menu_inicio.add_command(label="Salir", command=vent.quit)

    menu_tema = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Tema", menu=menu_tema)
    menu_tema.add_command(label="Tema Claro", command=temaClaro)
    menu_tema.add_command(label="Tema Oscuro", command=temaOscuro)
def formato_resultado(r):
    return int(r) if r % 1 == 0 else r

def factorial():
    n1 = txt1.get()
    try:
        r = math.factorial(int(n1))
        txt3.delete(0, 'end')
        txt3.insert(0, r)
    except ValueError:
        txt3.delete(0, 'end')
        txt3.insert(0, "Error")

def mcm():
    def calcular_mcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    n1 = txt1.get()
    n2 = txt2.get()
    try:
        r = calcular_mcm(int(n1), int(n2))
        txt3.delete(0, 'end')
        txt3.insert(0, r)
    except ValueError:
        txt3.delete(0, 'end')
        txt3.insert(0, "Error")

def mcd():
    n1 = txt1.get()
    n2 = txt2.get()
    try:
        r = math.gcd(int(n1), int(n2))
        txt3.delete(0, 'end')
        txt3.insert(0, r)
    except ValueError:
        txt3.delete(0, 'end')
        txt3.insert(0, "Error")

def salir():
    vent.destroy()


  

   
    vent = Tk()
    vent.title("Calculadora Simple")
    vent.geometry("+500+80")
    vent.configure(bg=bg_color)
    
    global txt1, txt2, txt3
    
    lbl1 = Label(vent, text="Número 1:", bg=bg_color, fg=fg_color, font=font)
    lbl1.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    txt1 = Entry(vent, bg="#fff")
    txt1.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    
    lbl2 = Label(vent, text="Número 2:", bg=bg_color, fg=fg_color, font=font)
    lbl2.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    txt2 = Entry(vent, bg="#fff")
    txt2.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    lbl3 = Label(vent, text="Resultado:", bg=bg_color, fg=fg_color, font=font)
    lbl3.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    txt3 = Entry(vent, bg="#FFF")
    txt3.grid(row=5, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    btn_factorial = Button(vent, text="Factorial", command=factorial, bg="#7f7fff")
    btn_factorial.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    btn_mcm = Button(vent, text="MCM", command=mcm, bg="#7f7fff")
    btn_mcm.grid(row=6, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

    btn_mcd = Button(vent, text="MCD", command=mcd, bg="#7f7fff")
    btn_mcd.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    btn_salir = Button(vent, text="Salir", command=salir, bg="#d3d3d3")
    btn_salir.grid(row=7, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

   

def ejecutar_otro_programa():
    programa = "Calculadora.py"  
    try:
        subprocess.run(["python", programa], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el programa: {e}")




   
    
    ventana.mainloop()


