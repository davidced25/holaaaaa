# Clase Nodo (Habitacion)
class Huesped:
    def __init__(self, num): 
        self.num = num
        self.estado = "Libre"
        self.cedula = None
        self.nombre = None
        self.hora = None
        self.siguiente = None


# Clase Lista Enlazada
class Hotel:
    def __init__(self):  
        self.cabeza = None

    # Crear habitaciones
    def agregar_habitacion(self, num):
        nuevo = Huesped(num)
 # Agregar al final de la lista
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
            # Recorrer hasta el final de la lista
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Asignar habitacion
    def asignar_habitacion(self):
        cedula = input("Ingrese cedula: ")
        nombre = input("Ingrese nombre: ")
        hora = input("Ingrese hora de llegada: ")

        actual = self.cabeza
        # Recorrer la lista para encontrar la primera habitacion libre y asignarla al huesped
        while actual:
            if actual.estado == "Libre":
                actual.estado = "Ocupado"
                actual.cedula = cedula
                actual.nombre = nombre
                actual.hora = hora
                print("Habitacion asignada:", actual.num)
                return
            actual = actual.siguiente

        print("No hay habitaciones disponibles.")

    # Liberar habitacion por cedula
    def liberar_habitacion(self):
        cedula = input("Ingrese cedula del huesped que sale: ")

        actual = self.cabeza
        # Recorrer la lista para encontrar la habitacion ocupada por esa cedula
        while actual:
            if actual.cedula == cedula:
                actual.estado = "Libre"
                actual.cedula = None
                actual.nombre = None
                actual.hora = None
                print("Habitacion liberada correctamente.")
                return
            actual = actual.siguiente

        print("Cedula no encontrada.")

    # Mostrar habitaciones libres
    def mostrar_libres(self):
        actual = self.cabeza
        print("Habitaciones libres:")
        # Recorrer la lista y mostrar solo las habitaciones que estan libres
        while actual:
            if actual.estado == "Libre":
                print("Habitacion", actual.num)
            actual = actual.siguiente

    # Mostrar habitaciones ocupadas
    def mostrar_ocupadas(self):
        actual = self.cabeza
        print("Habitaciones ocupadas:")
        while actual:
            if actual.estado == "Ocupado":
                print("Habitacion:", actual.num,
                      "Cedula:", actual.cedula,
                      "Nombre:", actual.nombre,
                      "Llegada:", actual.hora)
            actual = actual.siguiente

    # Buscar huesped por cedula
    def buscar_cedula(self):
        cedula = input("Ingrese cedula a buscar: ")
        actual = self.cabeza

        while actual:
            if actual.cedula == cedula:
                print("Huesped encontrado:")
                print("Habitacion:", actual.num)
                print("Nombre:", actual.nombre)
                print("Hora llegada:", actual.hora)
                return
            actual = actual.siguiente

        print("No existe un huesped con esa cedula.")
    
    #funcion insertar pila en huesped
    def push(self, num):
        nuevo = Huesped(num)
        nuevo.siguiente = self.cabeza
        self.superior = nuevo
        self.num += 1

    def pop(self):
        if self.cabeza is None:
            print("La pila esta vacia")
            return
        else:
            dato = self.cabeza.num
            self.cabeza = self.cabeza.siguiente
            self.num -= 1
            return dato
        
    def esta_vacia(self):
        if self.cabeza is None:
            return True
        else:
            return False
    def contar_elementos(self):
        cont=0
        actual = self.cabeza
        while actual is not None:
            cont += 1
            actual = actual.siguiente
        return cont


        


# PROGRAMA PRINCIPAL

hotel = Hotel()

# Crear habitaciones
cantidad = int(input("Ingrese numero de habitaciones del hotel: "))
for i in range(1, cantidad + 1):
    hotel.agregar_habitacion(i)

# Menu
while True:
    print("\n------ MENU HOTEL ------")
    print("1. Asignar habitacion")
    print("2. Liberar habitacion")
    print("3. Mostrar habitaciones libres")
    print("4. Mostrar habitaciones ocupadas")
    print("5. Buscar huesped por cedula")
    print("6. Salir")

    opcion = int(input("Seleccione una opcion: ")) 

    if opcion == 1:   
        hotel.asignar_habitacion()
    elif opcion == 2:
        hotel.liberar_habitacion()
    elif opcion == 3:
        hotel.mostrar_libres()
    elif opcion == 4:
        hotel.mostrar_ocupadas()
    elif opcion == 5:
        hotel.buscar_cedula()
    elif opcion == 6:
        print("Saliendo del sistema...")
        break
    elif opcion == 7:
        print("Numero de elementos en la pila:", hotel.contar_elementos())
    else:
        print("Opcion invalida.")
