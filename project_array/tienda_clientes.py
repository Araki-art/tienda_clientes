# * Zona de funciones *
def hacer_menu():
    print("\nMenú de Clientes")
    print("1. Registrar nuevo cliente.")
    print("2. Eliminar cliente.")
    print("0. Salir del Sistema.")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def registrar_clientes():  
    nombre_cliente = input("Digite el nombre: ")
    apellido_cliente = input("Digite el apellido: ")
    cedula_cliente = input("Digite la cédula: ")
    aux_info_cliente = [nombre_cliente, apellido_cliente, cedula_cliente]
    return aux_info_cliente

def guardar_cliente(info_cliente, bd_cliente):
    bd_cliente.append(info_cliente)
    return bd_cliente

def incluir_nueva_lista():
    aux_lista = []
    cantidad_nuevas = int(input("Digite la cantidad nueva de clientes: "))
    for _ in range(cantidad_nuevas):
        aux = registrar_clientes()
        aux_lista.append(aux)
    return aux_lista

def eliminar_cliente(bd_cliente):
    cedula = input("Ingrese la cédula del cliente a eliminar: ")
    for cliente in bd_cliente:
        if cliente[2] == cedula:
            bd_cliente.remove(cliente)
            print("Cliente eliminado correctamente.")
            return
    print("Cliente no encontrado.")

# * Zona principal de código *

base_datos_clientes = []

while True:
    aux_opcion = hacer_menu()
    
    match aux_opcion:
        case 1:
            aux_info_cliente = registrar_clientes()
            base_datos_clientes = guardar_cliente(aux_info_cliente, base_datos_clientes)
            print("Cliente registrado con éxito.")
        
        case 2:
            eliminar_cliente(base_datos_clientes)

        case 0:
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción no válida. Intente de nuevo.")

print("\nLista final de clientes:")
print(base_datos_clientes)
