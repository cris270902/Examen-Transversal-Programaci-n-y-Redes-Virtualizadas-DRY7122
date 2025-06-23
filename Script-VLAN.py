vlan = int(input("Ingrese numero de VLAN IPV4: "))

if 1 <= vlan <= 99 or 1004 <= vlan <= 1005:
    print("VLAN DE RANGO NORMAL")
elif 1006  <= vlan <= 1007 or 4093 <= vlan <= 4094:
    print("VLAN DE RANGO Extendida")
