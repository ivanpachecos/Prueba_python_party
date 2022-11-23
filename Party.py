ingreso_name = (input("Ingrese su nombre: "))
ingreso_edad = int(input("Ingrese su edad: "))

if ingreso_edad <= 17:
    print(f"No puede ingresar usted tiene {ingreso_edad}, es Menor de edad ")

else:
    print(f"SU edad es {ingreso_edad}, puede ingresar")
    print("==============================================")
    print(f"Binevenido {ingreso_name}, Disfrute la fiesta ")
    print("==============================================")
