vlan = int(input("Ingrese la vlan para ver si es estandar o extendida: "))

if vlan >= 1006 and 4096:
    print("esta vlan es extendida")

elif vlan <= 1005:
    print ("esta vlan es estandar")

else:
    print("esta vlan no existe")