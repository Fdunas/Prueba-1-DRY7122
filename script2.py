# Script de Python para solicitar y validar información del alumno
def main():

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    codigo_seccion = input("Ingrese su Código-sección: ")
    sede = input("Ingrese su sede: ")

    if codigo_seccion == "DRY7122-003V":
        print(f"Información del alumno:")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Código-sección: {codigo_seccion}")
        print(f"Sede: {sede}")
    else:
        print("El alumno no pertenece a la sección DRY7122-003V.")


if __name__ == "__main__":
    main()

