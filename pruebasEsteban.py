HojaDeVida = {

}

def actualizarHojaDeVida(HojaDeVida):
    print("3. Actualizar hoja de vida.")

    validarDocumento = str(input("Digite su número de cedula: "))

    if HojaDeVida.__len__() == 0:
        print("No se han registrado hojas de vida hasta el momento.")
    else:
        if validarDocumento in HojaDeVida:

            validarOpcion = int(input("Digite la opción que quiere actualizar 1.Datos Personales / 2.Experiencia / 3.Referencia: "))
    
            if validarOpcion == 1:
                print("--------------------------------------------------------------")
                print("Nuevos datos personales.")
                print("--------------------------------------------------------------")

                try:
                    actualizarContacto = input("Digita tu nuevo numero de contacto: ")
                    actualizarDireccion = input("Digita tu nueva direccion: ")
                    actualizarCorreo = input("Digita tu nuevo correo: ")
                    actualizarFechanacimiento = input("Digite tu fecha de nacimiento: ")

                    HojaDeVida[(validarDocumento)["Datos"]].update({"Contacto":actualizarContacto})
                    HojaDeVida[(validarDocumento)["Datos"]].update({"Direccion":actualizarDireccion})
                    HojaDeVida[(validarDocumento)["Datos"]].update({"Correo":actualizarCorreo})
                    HojaDeVida[(validarDocumento)["Datos"]].update({"Fechanacimiento":actualizarFechanacimiento})
                except ValueError:
                    print("No puedes ingresar datos vacios, letras o caratecteres especiales.")

            elif validarOpcion == 2:
                print("Nueva experiencia.")
            elif validarOpcion == 3:
                print("Nueva referencia.")
            else:
                print("ERROR. Debes digitar una opción valida.")
        else:
            print("Este número de documento no se encuentra registrado.")
