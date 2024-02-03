class Cliente:
    def __init__(self, nombre, apellido, edad, correo, altura, peso, mail, empleo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.altura = altura
        self.peso = peso
        self.empleo = empleo
        self.mail = mail

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_info(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nCorreo: {self.correo}\nAltura {self.altura}\nPeso {self.peso}"

    def realizar_compra(self, producto):
        return f"{self} ha comprado {producto}"