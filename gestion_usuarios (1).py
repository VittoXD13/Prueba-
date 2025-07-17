usuarios = {}

def validar_sexo(sexo):
    return sexo in ["M", "F"]

def ingresar_usuario():
    nombre=input("Ingrese nombre de usuario: ")
    if nombre in usuarios:
        print("Usuario ya existe, intente otro")
        return
    
    sexo=input("Ingrese sexo: ")
    while not validar_sexo(sexo):
        print("Debe ingresar M o F solamente")
        sexo=input("Ingrese sexo: ")

    contraseña=input("Ingrese contraseña: ")

    usuarios[nombre]={"sexo": sexo, "contraseña": contraseña}
    print("Usuario ingresado con éxito")

def buscar_usuario():
    nombre=input("Ingrese usuario a buscar: ")
    if nombre in usuarios:
        datos=usuarios[nombre]
        print(f"sexo: {datos['sexo']} contraseña: {datos['contraseña']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    nombre=input("Ingrese usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado con éxito")
    else:
        print("No se pudo eliminar usuario")

def main():
    while True:
        print("____MENU PRINCIPAL____")
        print("1.-Ingresar usuario")
        print("2.-Buscar usuario")
        print("3.-Eliminar usuario")
        print("4.-Salir")

        opcion=input("Ingrese opción: ")

        if opcion=="1":
            ingresar_usuario()
        elif opcion=="2":
            buscar_usuario()
        elif opcion=="3":
            eliminar_usuario()
        elif opcion=="4":
            print("Programa terminado")
            break
        else:
            print("Debe ingresar una opción válida")

main()