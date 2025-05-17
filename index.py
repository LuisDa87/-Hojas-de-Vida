from Funciones import CrearHojaDeVida,ConsultarHojaDeVida, GenerarReporte, actualizarHojaDeVida
import json

HojasDeVida={

}

print("--- BIENENVENIDO A VITAECONSOLE ---\n")

print("--- MENÚ ---\n" 
    "1. Registrar hoja de vida.\n"
    "2. Consultar hoja de vida.\n"
    "3. Actualizar hoja de vida.\n"
    "4. Generar reporte.\n")

while True:
    
    opcion = int(input("Digite el número del proceso que desea realizar."))

    match opcion:
        case 1:
            print("1. Registrar hoja de vida.")
            CrearHojaDeVida(HojasDeVida)

        case 2:
            print("2. Consultar hoja de vida.")
            ConsultarHojaDeVida(HojasDeVida)
        case 3:
            print("3. Actualizar datos.")
            actualizarHojaDeVida(HojasDeVida)

        case 4:
            print("4. Generar reporte.")
            GenerarReporte(HojasDeVida)


