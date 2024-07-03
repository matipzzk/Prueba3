from funciones import *




cilindro_5k  = 12500
cilindro_15k = 25500

pedidos=[]
cont_5 = 0
cont_15=0
total = 0

while True:
    limpiar()
    print("""Bienvenido a Gaxplosive
    1.Registrar pedido
    2.Mostrar pedido
    3.Buscar pedido por RUT
    4.Imprimir hoja de ruta
    5.salir
      """)
    opc = int(input("Ingrese opción: "))
    if opc ==1:
        limpiar()
        opc_1()
    elif opc==2:
        limpiar()
        opc_2()
    elif opc==3:
        limpiar()
        opc_3()
    elif opc==4:
        limpiar()
        opc4()
    else:
        opc_5()
