usuarios = []

def registrar_usuario():
    print("Registro de usuario:")
    nombre = input("Ingresa tu nombre: ")
    contrasena = input("Ingresa tu contraseña: ")
    usuarios.append({'nombre': nombre, 'contrasena': contrasena})
    print("¡Usuario registrado con éxito!\n")

def iniciar_sesion():
    print("Inicio de sesión:")
    nombre = input("Ingresa tu nombre de usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    for usuario in usuarios:
        if usuario['nombre'] == nombre and usuario['contrasena'] == contrasena:
            print("¡Inicio de sesión exitoso!\n")
            return
    print("Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.\n")

while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.\n")
