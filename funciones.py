import time,os, msvcrt



cilindro_5k  = 12500
cilindro_15k = 25500

pedidos=[]
cont_5 = 0
cont_15=0



def opc_1():
    total = 0
    cont_15=0
    cont_5 = 0
    print("REGISTRAR PEDIDO")
    rut = int(input("Ingres su rut: "))
    nombre =validar_nombre()
    direccion =  input("Ingrese su dirección: ")
    comuna = input("Ingrese su comuna: ")
    while True:
        print(f"1.Cilindro de 5 kilos  Valor {cilindro_5k}$")
        print(f"2.Cilindro de 15 kilos Valor{cilindro_15k}")
        print("3.Salir")
        opcion = int(input("Ingrese opción: "))
        if opcion ==1:
            total=total+cilindro_5k
            cont_5 = cont_5+1
            print("CILINDRO AGREAGADO EXITOSAMENTE")
        elif opcion ==2:
            total = total+cilindro_15k
            cont_15 = cont_15+1
            print("CILINDRO AGREGADO EXITOSAMENTE")
        else:
            break
        pedido = {
            "rut":rut,
            "nombre":nombre,
            "direccion":direccion,
            "comuna":comuna,
            "total":total,
            "cil 5K":cilindro_5k,
            "cil 15K":cilindro_15k
            }
        pedidos.append(pedido)


def opc_2():
    if len(pedidos)==0:
        print("NO HAY PEDIDOS")
    else:
        print("Mostrar pedido")
        for x in pedidos:
            print(f"RUT: {x['rut']} CLIENTE: {x['nombre']} Dirección: {x['direccion']} COMUNA: {x['comuna']}Cil.5K {x['cil 5K']} Cil.15K{x['cil 15K']} TOTAL: {x['total']}")
        print("Se mostrara durante 5 segundos")
        time.sleep(5)


def opc_3():
    if len(pedidos)==0:
        print("NO HAY PEDIDOS")
    else:
        print("BUSCAR PEDIDO")
        busrut= input("INGRESE SU RUT")
        for i in pedidos:
            if i == busrut:
                (print(f"RUT: {i["rut"]} CLIENTE: {i["nombre"]} Dirección: {i["direccion"]} COMUNA: {i["comuna"]} TOTAL: {i["total"]}"))
        print("Se mostrara durante 5 segundos")
        time.sleep(5)


def opc4():
    with open ("pedido.csv ","w", newline="")as archivo:
        archivo(pedidos)



def limpiar():
    os.system('cls')        


def validar_nombre():
    nombre= input("Ingrese su nombre: ")
    if len(nombre) < 3:
        print("ERROR! El nombre debe tener al menos 3 caracteres")

    
def opc_5():
    print("Hasta Luego")
    exit()    