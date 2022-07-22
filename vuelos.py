import numpy as np

asientos=np.array([[j+i*6 for j in range(1,7)] for i in range(7)], dtype=object)
pasajeros=[]

def ocupar_asientos(asientos, numero_asiento):
    asientos[asientos==numero_asiento]='X'
    return asientos

def desocupar_asientos(asientos, numero_asiento):
    for i in range(len(asientos)):
        for j in range(len(asientos[i])):
            index=i*len(asientos[i])+j
            if index==numero_asiento-1:
                asientos[i,j]=numero_asiento
    return asientos    
    
def compra_asiento(asientos):
    monto=0
    nombrePasajero=input('Nombre pasajero ')
    rutPasajero=input('Rut pasajero ')
    telefonoPasajero=input('Telefono psajero ')
    bancoPasajero=input('indique cual es su banco (bancoDuoc tiene un 15 % de descuento) ').lower()
    numero_asiento=int(input('elija su asiento (1-30 asiento normal, 31-42 asiento vip) '))
    if numero_asiento in range(1,31):
         monto=78900
    elif numero_asiento in range(31,43):
        monto=240000
    if bancoPasajero=='bancoduoc':
        monto=monto*0.85
    continuar=input(f'El pasajero {rutPasajero}, ha elegido el asiento {numero_asiento}, por el que debe cancelar un monto de ${monto}. Dese continuar?(s/n) ')
    if continuar=='s':
        pasajeros.append([nombrePasajero,rutPasajero,telefonoPasajero,numero_asiento])
        ocupar_asientos(asientos, numero_asiento)
    return pasajeros

def anular_pasaje(asientos, pasajeros):
    rut=input('rut del pasajero ')
    asiento=int(input('asiento '))
    for pasajero in pasajeros:
        if rut in pasajero:
            desocupar_asientos(asientos, asiento)
            pasajeros.remove(pasajero)
    return pasajeros

def modificar_datos(pasajeros):
    rut=input('Ingrese su rut sin puntos y con digito verificador ')
    numero_asiento=int(input('numero de asiento '))
    for pasajero in pasajeros:
        if rut in pasajero and numero_asiento in pasajero:
            condicion=True
            while condicion:
                op=int(input('1. cambio de nombre \n2. cambio de rut  \n3. ccambio de telefono \n4. Salir \n'))
                if op==1:
                    nombre=input('Ingrese nuevo nombre ')
                    pasajero[0]=nombre
                elif op==2:
                    rut=input('Ingrese nuevo rut')
                    pasajero[1]=rut
                elif op==3:
                    telefono=input('Ingrese nuevo telefono ')
                    pasajero[2]=telefono
                elif op==4:
                    condicion=False
            break
    return pasajeros
        
condicion=True
while condicion:
    op=int(input('1. Ver asientos disponibles \n2. Comprar asiento \n3. Anular pasaje \n4. Modificar datos de pasajero \n5. Salir \n'))
    if op==1:
        print('Asientos disponibles')
        print(asientos)
    elif op==2:
        print(compra_asiento(asientos))
    elif op==3:
        print(anular_pasaje(asientos, pasajeros))
    elif op==4:
        print(modificar_datos(pasajeros))
    elif op==5:
        condicion=False