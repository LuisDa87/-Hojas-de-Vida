def actualizarHojaDeVida(HojasDeVida):

    validarDocumento = input("Digite su número de cedula: ")

    if HojasDeVida.__len__() == 0:
        print("No se han registrado hojas de vida hasta el momento.")
    else:
        if validarDocumento in HojasDeVida:

            validarOpcion = int(input("Digite la opción que quiere actualizar 1.Datos Personales / 2.Experiencia / 3.Referencia: "))
    
            if validarOpcion == 1:
                print("--------------------------------------------------------------")
                print("Nuevos datos personales.")
                print("--------------------------------------------------------------")

                try:
                    actualizarNombre = input("Digita tu nombre completo: ")
                    actualizarDocumento = input("Digita tu número de documento: ")
                    actualizarContacto = input("Digita tu nuevo numero de contacto: ")
                    actualizarDireccion = input("Digita tu nueva direccion: ")
                    actualizarCorreo = input("Digita tu nuevo correo: ")
                    actualizarFechanacimiento = input("Digite tu fecha de nacimiento: ")

                    HojasDeVida[(validarDocumento)]["Datos"].update({"Nombre":actualizarNombre})
                    HojasDeVida[(validarDocumento)]["Datos"].update({"Documento":actualizarDocumento})
                    HojasDeVida[(validarDocumento)]["Datos"].update({"Contacto":actualizarContacto})
                    HojasDeVida[(validarDocumento)]["Datos"].update({"Direccion":actualizarDireccion})
                    HojasDeVida[(validarDocumento)]["Datos"].update({"Correo":actualizarCorreo})
                    HojasDeVida[(validarDocumento)]["Datos"].update({"Fechanacimiento":actualizarFechanacimiento})

                    print("Datos actualizados.")
                    print("--------------------------------------------------------------")
                    print("	\033[92m Hoja de vida creada exitosamente \033[0m")
                    for i in HojasDeVida[validarDocumento].items():
                        print("--------------------------------------------------------------")
                        print(f"\033[93m {i}\033[0m")
                        print("--------------------------------------------------------------")
                except ValueError:
                    print("No puedes ingresar datos vacios, letras o caratecteres especiales.")

            elif validarOpcion == 2:
                print("--------------------------------------------------------------")
                print("Agregar experiencia laboral.")
                print("--------------------------------------------------------------")

                try:
                    actualizarCantidadExperiencias = int(input("Cuantas experiencias desea insertar: "))
                except ValueError:
                    print("Ingresa un numero mayor a 0.")

                contadorexperiencias = 0
                for i in range(actualizarCantidadExperiencias):
                    contadorexperiencias += 1
                    try:    
                        actualizarEmpresa = input("Digite el nombre de la empresa donde laboro: ")
                        actualizarCargo = input("¿Cual fue su cargo?: ")  
                        actualizarFunciones = input("¿Cuales eran tus funciones principales?: ")
                        actualizarDuracion = input("¿Por cuanto tiempo trabajo en esta empresa?: ")

                        for i in HojasDeVida:
                    

                        HojasDeVida[(validarDocumento)]['Experiencias'].append(actualizarEmpresa, actualizarCargo, actualizarFunciones, actualizarDuracion)

                        print("Experiencias actualizadas.")
                        print("Datos actualizados.")

                        print("--------------------------------------------------------------")
                        print("	\033[92m Hoja de vida creada exitosamente \033[0m")
                        for i in HojasDeVida[validarDocumento].items():
                            print("--------------------------------------------------------------")
                            print(f"\033[93m {i}\033[0m")
                            print("--------------------------------------------------------------")
                    except ValueError:
                        print("Ingrese datos validos")
                        break
                    else:
                        print("\033[92m Experiencias guardadas correctamente\033[0m")
            elif validarOpcion == 3:
                print("--------------------------------------------------------------")
                print("Agregar referencia.")
                print("--------------------------------------------------------------")

            else:
                print("ERROR. Debes digitar una opción valida.")
        else:
            print("Este número de documento no se encuentra registrado.")