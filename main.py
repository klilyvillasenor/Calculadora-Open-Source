from sumar import sumar
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Bienvenido a la Calculadora")
    print("Seleccione una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar varios números")
    print("6. Salir")

def obtener_numero():
    return float(input("Introduce un número: "))

while True:
    mostrar_menu()
    opcion = input("Opción: ")
    
    if opcion == "1":
        num1 = obtener_numero()
        num2 = obtener_numero()
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == "2":
        num1 = obtener_numero()
        num2 = obtener_numero()
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == "3":
        num1 = obtener_numero()
        num2 = obtener_numero()
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == "4":
        num1 = obtener_numero()
        num2 = obtener_numero()
        if num2 != 0:
            print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == "5":
        cantidad = int(input("¿Cuántos números quieres sumar? "))
        numeros = [obtener_numero() for _ in range(cantidad)]
        print(f"Resultado: {suma_avanzada(*numeros)}")
    elif opcion == "6":
        print("Gracias por usar la calculadora.")
        break
    else:
        print("Opción no válida.")
