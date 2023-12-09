#Programa que reliza los pedidos de hamburguesas por Anthony Astudillo
print("Bienvenidos al Carbonero!!!!")
print ("Por favor ingrese los datos para la factura:")
nombre = input ("Por favor ingrese su nombre: ")
cedula = int(input("Por favor ingrese su numero de cedula: "))
correo = input("Por favor ingrese su correo electronico: ")
cantidad = int(input("Por favor indique cuantas hamburguesas deseas: "))
print ("Los Tipos de Hamburguesas que tenemos son:")
print("1:Sencillas")
print("2:Dobles")
print("3:Triples")
opciones1 = input("Seleccione la opcion que desea: ")
if opciones1 == "1":
    valorTotal = cantidad *1.50
    print("El valor de su compra es: ", valorTotal,"$")
    print("Selccione el tipo de pago:")
    print("1:Efectivo")
    print("2:Tarjeta")
    opciones2 = input("Seleccione la opcion que desea: ")
    if opciones2 == "1":
        print("Su pago es en efectivo no hay recargo el total a pagar es: ", valorTotal,"$")
        print(nombre," muchas gracias por su compra, vuelva pronto su factura se le enviara al correo ", correo)
    elif opciones2 == "2":
        print("Su pago es en tarjeta hay recargo el total a pagar es: ", (valorTotal * 0.05) + valorTotal,"$")
        print(nombre," muchas gracias por su compra, vuelva pronto su factura se le enviara al correo ", correo)
    else:
        print("Valor no valido")
elif opciones1 == "2":
    valorTotal = cantidad *2.50
    print("El valor de su compra es: ", valorTotal,"$")
    print("Selccione el tipo de pago:")
    print("1:Efectivo")
    print("2:Tarjeta")
    opciones2 = input("Seleccione la opcion que desea: ")
    if opciones2 == "1":
        print("Su pago es en efectivo no hay recargo el total a pagar es: ", valorTotal,"$")
        print(nombre," muchas gracias por su compra, vuelva pronto su factura se le enviara al correo ", correo)
    elif opciones2 == "2":
        print("Su pago es en tarjeta hay recargo el total a pagar es: ", (valorTotal * 0.05) + valorTotal ,"$")
        print(nombre," muchas gracias por su compra, vuelva pronto su factura se le enviara al correo ", correo)
    else:
        print("Valor no valido")
elif opciones1 == "3":
    valorTotal = cantidad *3.25
    print("El valor de su compra es: ", valorTotal,"$")
    print("Selccione el tipo de pago:")
    print("1:Efectivo")
    print("2:Tarjeta")
    opciones2 = input("Seleccione la opcion que desea: ")
    if opciones2 == "1":
        print("Su pago es en efectivo no hay recargo el total a pagar es: ", valorTotal,"$")
        print(nombre," muchas gracias por su compra, vuelva pronto su factura se le enviara al correo ", correo)
    elif opciones2 == "2":
        print("Su pago es en tarjeta hay recargo el total a pagar es: ", (valorTotal * 0.05) + valorTotal ,"$")
        print(nombre," muchas gracias por su compra, vuelva pronto su factura se le enviara al correo ", correo)
    else:
        print("Valor no valido")
else:
    print("Valor no valido")