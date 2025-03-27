def hacer_menu():
    print("1. Registrar nuevo cliente.")
    print("2. Eliminar cliente.")
    print("0. Salir del Sistema.")
    print("... seleccione una opcion.")
    opcion = int(input())
    return opcion

def registrar_clientes():  
    nombre_cliente = input("digite el nombre:")
    apellido_cliente = input("digite el apellido:")
    cedula_cliente=input("digite la cedula:")
    aux_info_cliente [nombre_cliente , apellido_cliente , cedula_cliente]
    return aux_info_cliente

def guardar_cliente(info_cliente , bd_cliente):
    bd_cliente.append(info_cliente)
    return bd_cliente

def incluir_nueva_lista():
    aux_lista =[]
    cantidad_nuevas = int(input("digite la cantidad nueva de clientes"))
    for i in range(0 ,cantidad_nuevas, 1):
        aux= registrar_clientes()
        aux_lista.append(aux)
    print(aux_lista)
    #return aux_lista


    
#*zona principal de codigo*
incluir_nueva_lista
base_datos_clientes = [5]
while True:
        aux_opcion= hacer_menu()
        match aux_opcion:
            case 1:
                aux_info_cliente = registrar_clientes()
            case 2:
                aux_lista = incluir_nueva_lista()
                base_datos_clientes.extend(aux_lista)




base_datos_clientes=[]
aux_opcion= hacer_menu()  
aux_info_cliente= registrar_clientes()

aux_basedatos= guardar_cliente(aux_info_cliente, base_datos_clientes)
base_datos_clientes=aux_basedatos
print (base_datos_clientes)

aux_info_cliente = registrar_clientes()
