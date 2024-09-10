def mostrar_menu():
    print("Menú de Operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Dividición")
    print("5. Salir")

def sumar(numeros):
    return sum(numeros)

def restar(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
        #resultado=resultado*num
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        if num == 0:
            return "Error: División por cero no permitida."
        resultado /= num
    return resultado

def formato_resultado(resultado):
    return int(resultado) if resultado % 1 == 0 else resultado

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción del menú: "))
            if opcion == 5:
                print("Saliendo de la calculadora")
                break
            if 1 <= opcion <= 4:
                cantidad = int(input("¿Cuántos números desea operar? "))
                if cantidad <= 0:
                    print("Error: La cantidad de números debe ser positiva.")
                    continue
                numeros = []
                for i in range(cantidad):
                    try:
                        numero = float(input(f"Ingrese el número {i+1}: "))
                        numeros.append(numero)
                    except ValueError:
                        print("Error: Debe ingresar un número válido.")
                        break
                else:
                    if opcion == 1:
                        resultado = sumar(numeros)
                    elif opcion == 2:
                        resultado = restar(numeros)
                    elif opcion == 3:
                        resultado = multiplicar(numeros)
                    elif opcion == 4:
                        resultado = dividir(numeros)

                    print(f"Resultado:{formato_resultado(resultado)}")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

ejecutar_calculadora()

