class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

usuario = Usuario("jontx", "supercontraseña")

print("Nombre de usuario:", usuario.nombre_usuario)
print("Contraseña:", usuario.contraseña)