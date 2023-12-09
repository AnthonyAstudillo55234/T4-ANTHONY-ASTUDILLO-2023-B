#Programa de una calculadora por Anthony Astudillo
print("Calculadora de Anthony Astudillo")
num1 = float(input("Por favor ingrese el primer valor: "))
num2 = float(input("Por favor ingrese el segundo valor: "))
print("Las operaciones que se puede realizar son:")
print("1:Suma")
print("2:Resta")
print("3:Multiplicacion")
print("4:Division")
print("5:Potencia")
print("6:Modulo")
opciones = input("Seleccione la opcion que desea: ")
if opciones == "1":
    resultado = num1 + num2
    print("El resultado de la operacion es:", resultado)
elif opciones == "2":
    resultado = num1 - num2
    print("El resultado de la operacion es:", resultado)
elif opciones == "3":
    resultado = num1 * num2
    print("El resultado de la operacion es:", resultado)
elif opciones == "4":
    if num2 == 0:
        print("No se puede dividir para 0")
    else:
        resultado = num1 / num2
        print("El resultado de la operacion es:", resultado)
elif opciones == "5":
    resultado = num1 ** num2
    print("El resultado de la operacion es:", resultado)
elif opciones == "6":
    resultado = num1 % num2
    if num2 == 0:
        print("No se puede utilizar el 0")
    else:
        resultado = num1 % num2
        print("El resultado de la operacion es:", resultado)
else:
    print("Valor no valido")