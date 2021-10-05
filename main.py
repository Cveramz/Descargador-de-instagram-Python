import instaloader #pip install instaloader


ig=instaloader.Instaloader()
nombre=str(input("Ingrese un usuario: "))
try:
    print("Se guardará junto al ejecutable, en la carpeta "+nombre+"\ ")
    print("Cargando...\n")
    ig.download_profile(nombre, profile_pic_only=False)

except:
    print("\nEl usuario ingresado tiene la cuenta privada")
    print("Solo se ha guardado la foto de perfil")
