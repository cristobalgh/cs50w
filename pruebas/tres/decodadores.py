def anunciar(f):
    def wrapper():
        print("A punto de ejecutar la función...")
        f()
        print("Listo con la ejecución de la función.")
    return wrapper
@anunciar
def hola():
    print("Hello world!")

hola()     
