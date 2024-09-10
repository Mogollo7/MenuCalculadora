def Menú_Nombre():
    print("\nHola usuario, por favor ingrese su nombre")
    nombre_usuario = input("Nombre: ")
    return nombre_usuario

def mostrar_menu(nombre_usuario):
    print(f"Hola {nombre_usuario}")
    print("\nOpciones del Menú")
    print("1. Suma")
    print("2. Resta")
    print("3. División")
    print("4. Calcular precio con Impuesto")
    print("5. Conversor de Temperatura (Celsius a Fahrenheit)")
    print("6. Terminar")

def agregar_valores(valores):
    return sum(valores)

def restar_valores(valores):
    resultado_final = valores[0]
    for valor in valores[1:]:
        resultado_final -= valor
    return resultado_final

def dividir_valores(valores):
    resultado_final = valores[0]
    for valor in valores[1:]:
        if valor == 0:
            return "Error: División por cero no permitida."
        resultado_final /= valor
    return resultado_final

def calcular_precio_impuesto(costo, tasa_impuesto=0.19):
    costo_total = costo + (costo * tasa_impuesto)
    return costo_total

def mostrar_resultado(resultado):
    return int(resultado) if resultado % 1 == 0 else resultado

def conversor_temperatura():
    grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    grados_fahrenheit = (grados_celsius * 9/5) + 32
    grados_fahrenheit = mostrar_resultado(grados_fahrenheit)  # Aplicar formateo del resultado
    print(f"{grados_celsius}°C son {grados_fahrenheit}°F\n")

def iniciar_calculadora():
    nombre_usuario = Menú_Nombre()  # Se obtiene el nombre del usuario al inicio
    while True:
        mostrar_menu(nombre_usuario)
        try:
            eleccion = int(input("Selecciona una opción del menú: "))
            if eleccion == 6:
                print(f"Terminando la calculadora, gracias {nombre_usuario}")
                break
            if 1 <= eleccion <= 3:
                cantidad_valores = int(input("¿Cuántos valores deseas usar? "))
                if cantidad_valores <= 0:
                    print("Error: La cantidad de valores debe ser positiva.")
                    continue
                lista_valores = []
                for i in range(cantidad_valores):
                    try:
                        valor = float(input(f"Ingrese el valor {i+1}: "))
                        lista_valores.append(valor)  # Se agregan los valores a la lista
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico válido.")
                        break
                else:
                    if eleccion == 1:
                        resultado_final = agregar_valores(lista_valores)
                    elif eleccion == 2:
                        resultado_final = restar_valores(lista_valores)
                    elif eleccion == 3:
                        resultado_final = dividir_valores(lista_valores)

                    print(f"Resultado: {mostrar_resultado(resultado_final)}")
            elif eleccion == 4:
                try:
                    precio_inicial = float(input("Introduce el precio: "))
                    precio_con_impuesto = calcular_precio_impuesto(precio_inicial)
                    print(f"El precio final con impuesto es: {mostrar_resultado(precio_con_impuesto)}")
                except ValueError:
                    print("Error: Debe ingresar un valor numérico válido para el precio.")
            elif eleccion == 5:
                conversor_temperatura()
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

iniciar_calculadora()

