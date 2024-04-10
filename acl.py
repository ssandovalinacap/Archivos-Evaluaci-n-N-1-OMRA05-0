# Script en Python para identificar el tipo de ACL IPv4
numero_acl = int(input("Ingrese el número de ACL IPv4: "))

if numero_acl >= 1 and numero_acl <= 99:
    print("ACL Estándar")
elif numero_acl >= 100 and numero_acl <= 199:
    print("ACL Extendida")
else:
    print("El número no corresponde a una lista de acceso.")
