import os, time


def registro ():
    
    nombre = input("Ingrese su nombre: ")
    while nombre == "" or nombre == " ":
        nombre = input("Ingrese su nombre correctamente: ")
    
        
        
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 15:
                print("Usted no puede acceder al NIF")
            else:
                break
        except:
            print("Valor no valido")
        
    while True:
        try:
            nifNumeros = int(input("Ingrese los 8 digitos del NIF"))
            if nifNumeros > 10000000 and nifNumeros < 99999999:
                break
            else:
                print("valor no valido")
        except:
            print("Valor ingresado no valido")
            
    nifCaracteres = input("Ingrese los 3 caracteres: ")
    while nifCaracteres == "" or nifCaracteres == " ":
        nifCaracteres = input("Ingrese los 3 caracteres correctamente: ")
    
    nif= (f"{nifNumeros}-{nifCaracteres}")

    usuario = {
        "Nombre" : nombre,
        "Edad" : edad,
        "NIF" : nif
        
    }
    
    usuarioLista.append(usuario)

    

        
def limpiar():
    os.system("cls")

    
        
            

usuarioLista = []



while True:
    
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir certificados")
    print("4.- Salir")
    
    while True:
        try:
            op = int(input("Ingrese una de las opciones: "))
            limpiar()
            break
        except:
            print("Valor seleccionado no valido")
            limpiar()
    
    if op == 1:
        registro()
        print(usuarioLista)
        input("Enter para continuar")
        limpiar()
        
    if op == 2:
        print(usuarioLista)
        input("Enter para continuar")
        limpiar()
        
    if op == 3:
        print("hola3")
        
    if op == 4:
        print("Jesus Alejandro Martinez Rivas deme un 7")
        break