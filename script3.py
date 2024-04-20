# Función para determinar el tipo de ACL según el número proporcionado
def determinar_tipo_acl(numero_acl):
    if 1 <= numero_acl <= 99:
        return "ACL Estándar"
    elif 100 <= numero_acl <= 199:
        return "ACL Extendida"
    elif 200 <= numero_acl <= 2699:
        return "ACL Layer 2"
    elif 3000 <= numero_acl <= 3999:
        return "ACL Layer 3"
    else:
        return "El número no corresponde a una lista de control de acceso existente."

# Función principal
def main():
    numero_acl = int(input("Ingrese el número de ACL IPv4: "))
    

    tipo_acl = determinar_tipo_acl(numero_acl)
    print(f"El número de ACL {numero_acl} corresponde a una {tipo_acl}.")

# Llama a la función principal
if __name__ == "__main__":
    main()

