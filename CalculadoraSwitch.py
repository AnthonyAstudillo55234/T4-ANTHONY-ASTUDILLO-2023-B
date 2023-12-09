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
match opciones:
    case "1":
        resultado = num1 + num2
        print("El resultado de la operacion es:", resultado)
    case "2":
        resultado = num1 - num2
        print("El resultado de la operacion es:", resultado)
    case "3":
        resultado = num1 * num2
        print("El resultado de la operacion es:", resultado)
    case "4":
        match num2:
            case 0:
                print("No se puede dividir para 0")
            case _:
                resultado = num1 / num2
                print("El resultado de la operacion es:", resultado)
    case "5":
        resultado = num1 ** num2
        print("El resultado de la operacion es:", resultado)
    case "6":
        match num2:
            case 0:
                print("No se puede usar el 0")
            case _:
                resultado = num1 % num2
                print("El resultado de la operacion es:", resultado)
    case _:
        print("Valor no valido")