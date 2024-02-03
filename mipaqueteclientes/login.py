# Base de datos (diccionario)
Basededatos = {}

# Función para registrar
def registrar_usuario():
    user = input("Ingrese su usuario: ")
    nombre = input("Ingrese su nombre: ")
    mail = input("Ingrese su mail: ")
    edad = input("Ingrese su edad: ")
    empleo = input("Ingrese su empleo: ")
    contrasena = input("Ingrese su contraseña: ")

    # Funcion para verificar si el usuario ya existe
    if user in Basededatos:
        print("El usuario ya está registrado.")
    else:
        # Sino continua con la siguiente función
        Basededatos[user] = {
            'Nombre': nombre,
            'Mail': mail,
            'Contraseña': contrasena,
            'Edad': edad,
            'Empleo': empleo
        }
        print("Usuario registrado exitosamente.")


# Función para iniciar sesión
def iniciar_sesion():
    user = input("Ingrese su Usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Funcion para verificar si el usuario está en la base de datos y la contraseña es correcta
    if user in Basededatos and Basededatos[user]['Contraseña'] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Email o contraseña incorrectos.")

 # Función para mostrar la información de un usuario
def mostrar_usuario():
    user = input("Ingrese el usuario que desea buscar: ")
    if user in Basededatos:
        usuario = Basededatos[user]
        edad = Basededatos[user]
        empleo = Basededatos[user]
        mail = Basededatos[user]
        print(f"Nombre: {usuario['Nombre']}")
        print(f"Edad: {edad['Edad']}")
        print(f"Empleo: {empleo['Empleo']}")
        print(f"Mail: {mail['Mail']}")

    else:
        print("Usuario no encontrado.")

# Menú principal
while True:
    print("\n--- Gestión de Usuarios ---")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar info")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
       mostrar_usuario()
    elif opcion == '4':
       print ("Gracias, vuelva prontos")
       break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")