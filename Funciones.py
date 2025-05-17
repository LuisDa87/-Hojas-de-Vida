import json
contadorexperiencias = 0

def CrearHojaDeVida(HojasDeVida):
        
    while True:
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        print("--------------------------------------------------------------")
        print("\033[93m Datos personales.\033[0m")
        print("--------------------------------------------------------------")

        try:
            nombre = input("Digite tu nombre: ")
            documento = input("Digite tu documento: ")
            contacto = input("Digite tu numero de contacto: ")
            direccion = input("Digite tu direccion: ")
            correo = input("Digite tu correo: ")
            fechanacimiento = input("Digite tu fecha de nacimiento: ")
        except ValueError:
            print("No puedes ingresar datos vacios")
            break
        else:
            print("\033[92m Datos personales guardados correctamente\033[0m")

    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        
        print("--------------------------------------------------------------")
        print("	\033[93m Formación academica.\033[0m")
        print("--------------------------------------------------------------")

        try: 
            titulo = input("Digite el nivel academico: ")
            institucion = input("Digite el nombre completo de la institución donde se formo: ")
            anos = int(input("Digite los años de duración de la carrera: "))
        except ValueError:
            print("Ingresa un numero valido")
            break
        else:
            print("\033[92m Formacion academica guardada correctamente\033[0m")

    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        print("--------------------------------------------------------------")
        print("	\033[93m Experiencia laboral.\033[0m")
        print("--------------------------------------------------------------")
        ListaExperiencias = []
        Experiencias = {}

        try:
            cantidadexperiencias = int(input("Cuantas experiencias desea insertar: "))
        except ValueError:
            print("Ingresa un numero mayor a 0")

        #global contadorexperiencias
        for i in range(cantidadexperiencias):
            
            #contadorexperiencias += contadorexperiencias
            
            try:    
                empresa = input("Digite el nombre de la empresa donde laboro: ")
                cargo = input("¿Cual fue su cargo?: ")  
                funciones = input("¿Cuales eran tus funciones principales?: ")
                duracion = input("¿Por cuanto tiempo trabajo en esta empresa?: ")
            except ValueError:
                print("Ingrese datos validos")
                break
            else:
                print("\033[92m Experiencias guardadas correctamente\033[0m")

            Experiencias[empresa]={
                "Cargo": cargo,
                "Funciones": funciones,
                "Duracion": duracion
            }
        

        ListaExperiencias.append(Experiencias)

    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        print("--------------------------------------------------------------")
        print("	\033[93m Referencias personales.\033[0m")
        print("--------------------------------------------------------------")
        ListaReferencias=[]
        try:
            cantidadreferencias = int(input("Cuantas referencias deseas insertar: "))
        except ValueError:
            print("Ingresa un numero mayor a 0")
            break
        Referencia={}
        for i in range(cantidadreferencias):
            contadorreferencias += 1
            try:
                nombrereferencia = input("Digite el nombre de la referencia personal: ")
                cargoreferencia = input("¿Cual es el cargo que tiene acualmente?: ")  
                empresareferencia = input("Digite el nombre de la empresa donde trabaja actualmente: ")
                telefonoreferencia = input("Telefono acualizado del referente: ")
            except ValueError:
                print("Ingrese datos validos")
                break
            else:
                print("\033[92m Referencias personales guardadas correctamente\033[0m")
            
            Referencia[contadorreferencias]={
                "nombre":nombrereferencia,
                "cargo":cargoreferencia,
                "empresa":empresareferencia,
                "telefono":telefonoreferencia

            }
        
        ListaReferencias.append(Referencia)

    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        print("--------------------------------------------------------------")
        print("	\033[93m Habilidades o certificaciones adicionales.\033[0m")
        print("--------------------------------------------------------------")
        try:
            preguntahabilidades = int(input("¿Cuentas con alguna habilidad o certificación adicional? 1.SI / 2.NO: "))
        except ValueError:
            print("Ingresa una opcion de las dos (1. Si --- 2. No)")
            break
        if preguntahabilidades == 1:
            adicional = input("¿Con que habilidades o certificados adicionales cuentas?: ")
        elif preguntahabilidades == 2:
            adicional = "No aplica"

        HojasDeVida[(documento)]={
            "Datos":{
                "Nombre": nombre,
                "Documento":documento,
                "Contacto": contacto,
                "Direccion": direccion,
                "Correo": correo,
                "Fechanacimiento": fechanacimiento
            },
            "Formacion":{
                "Institucion": institucion,
                "Titulo": titulo,
                "Años": anos,
            },

            "Experiencias": ListaExperiencias,

            "Referencias":ListaReferencias,

            "Habilidades": {
                "Habilidad":adicional
            }
        }

        print("--------------------------------------------------------------")
        print("	\033[92m Hoja de vida creada exitosamente \033[0m")
        for i in HojasDeVida[documento].items():
            print("--------------------------------------------------------------")
            print(f"\033[93m {i}\033[0m")
            print("--------------------------------------------------------------")
            
        break
    





def ConsultarHojaDeVida(HojasDeVida):
    while True:
        try:
            opcion = int(input("Como desea buscar la hoja de vida? (1. Documento - 2. Correo electronico - 3. Nombre): \n>> "))
        except ValueError:
            print("Ingrese valores validos")
            break
        else:
            if opcion == 1:
                buscador= input("Ingrese documento: \n>> ")
                print(HojasDeVida[buscador])
            
            elif opcion == 2:
                buscador = input("Ingrese correo: ")
                for i in HojasDeVida:
                    if HojasDeVida[i]["Datos"]["Correo"] == buscador:
                        print(HojasDeVida[i])

            elif opcion == 3:
                buscador = input("Ingrese el nombre: ")
                for i in HojasDeVida:
                    if HojasDeVida[i]["Datos"]["Nombre"] == buscador:
                        print(HojasDeVida[i])           
            

            else:
                print("Opcion no valida")
                break




def GenerarReporte(HojasDeVida):
    with open("HojasDeVida.json", "w") as f:
        json.dump(HojasDeVida, f, indent=4) 


def actualizarHojaDeVida(HojasDeVida):

    validarDocumento = input("Digite su número de cedula: ")

    if HojasDeVida.__len__() == 0:
        print("No se han registrado hojas de vida hasta el momento.")
    else:
        if validarDocumento in HojasDeVida:

            validarOpcion = int(input("Digite la opción que quiere modificar 1.Datos Personales / 2.Experiencia / 3.Formación: "))
    
            if validarOpcion == 1:
                print("--------------------------------------------------------------")
                print("Actualizar datos personales.")
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
                print("Modificar experiencias laborales.")
                print("--------------------------------------------------------------")

                try:
                    actualizarCantidadExperiencias = int(input("Cuantas experiencias desea insertar: "))
                except ValueError:
                    print("Ingresa un numero mayor a 0.")

                    #contadoractualizar = contadorexperiencias
                for i in range(actualizarCantidadExperiencias):
                    #contadoractualizar = contadorexperiencias + 1
                    try:    
                        actualizarEmpresa = input("Digite el nombre de la empresa donde laboro: ")
                        actualizarCargo = input("¿Cual fue su cargo?: ")  
                        actualizarFunciones = input("¿Cuales eran tus funciones principales?: ")
                        actualizarDuracion = input("¿Por cuanto tiempo trabajo en esta empresa?: ")

                        HojasDeVida[(validarDocumento)]['Experiencias'][0][actualizarEmpresa]={
                                "Cargo": actualizarCargo,
                                "Funciones": actualizarFunciones,
                                "Duracion": actualizarDuracion
                        }
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
                print("Modificar formación academica.")
                print("--------------------------------------------------------------")

                try:
                    agregarFormacion = int(input("¿Que cantidad de formaciones academicas desea agregar?: "))
                except ValueError:
                    print("Ingresa un numero mayor a 0.")

                    #contadoractualizar = contadorexperiencias
                for i in range(agregarFormacion):
                    #contadoractualizar = contadorexperiencias + 1
                    try:    
                        actualizarTitulo = input("Digite el nivel academico: ")
                        actualizarInstitucion = input("Digite el nombre completo de la institución donde se formo: ")
                        actualizarAnos = int(input("Digite los años de duración de la carrera: "))

                        HojasDeVida[(validarDocumento)]['Formacion'][0][actualizarEmpresa]={
                                "Cargo": actualizarCargo,
                                "Funciones": actualizarFunciones,
                                "Duracion": actualizarDuracion
                        }
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
            else:
                print("ERROR. Debes digitar una opción valida.")
        else:
            print("Este número de documento no se encuentra registrado.")
        
#cantidad_exp=obtener_datos("Ingrese la cantidad de experiencias laborales: ", int)

#for i in range(cantidad_exp):
    #"Experiencia": {"Empresa":"Riwi", "Cargo":"Programador", "Funciones":"Programar", "Duracion":"10 Meses"},
    #empresa = obtener_datos("Ingrese el nombre de la empresa donde laboro: ", str)
    #{HojasDeVida[documento]["Empresa"][empresa]}
    #cargo = obtener_datos("Cual fue su cargo: ", str)  
    #{HojasDeVida[documento]["Cargo"][cargo]}
    #funciones = obtener_datos("Cuales eran tus funciones principales: ", str)
    #{HojasDeVida[documento]["Empresa"][empresa]}
    #duracion = obtener_datos("Por cuanto tiempo trabajo en esta empresa: ")
    #{HojasDeVida[documento]["Empresa"][empresa]}

    #print(f"Tu {i+1} primera experiencia laboral fue registrada con exito ")
    #HojasDeVida[(documento)]={
    #    "Experiencia":{
    #        "Empresa": empresa,
    #        "Cargo": cargo,
    #       "Funciones": funciones,
    #        "Duracion": duracion
    #   }
    #}#


