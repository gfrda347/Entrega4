import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controller.controlador import conectar_db, agregar_usuario, agregar_liquidacion, consultar_usuario, eliminar_usuario

def main():
    while True:
        print("Selecciona una opción:")
        print("1. Agregar usuario")
        print("2. Agregar liquidación")
        print("3. Consultar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Ingresa el número de la opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del usuario: ")
            apellido = input("Ingresa el apellido del usuario: ")
            documento_identidad = input("Ingresa el documento de identidad del usuario: ")
            correo_electronico = input("Ingresa el correo electrónico del usuario: ")
            telefono = input("Ingresa el teléfono del usuario: ")
            fecha_ingreso = input("Ingresa la fecha de ingreso del usuario (AAAA-MM-DD): ")
            fecha_salida = input("Ingresa la fecha de salida del usuario (AAAA-MM-DD): ")
            salario = float(input("Ingresa el salario del usuario: "))
            agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario)
            print("Usuario agregado exitosamente.")

        elif opcion == "2":
            indemnizacion = float(input("Ingresa el valor de la indemnización: "))
            vacaciones = float(input("Ingresa el valor de las vacaciones: "))
            cesantias = float(input("Ingresa el valor de las cesantías: "))
            intereses_sobre_cesantias = float(input("Ingresa el valor de los intereses sobre cesantías: "))
            prima_servicios = float(input("Ingresa el valor de la prima de servicios: "))
            retencion_fuente = float(input("Ingresa el valor de la retención en la fuente: "))
            total_a_pagar = float(input("Ingresa el valor total a pagar: "))
            id_usuario = int(input("Ingresa el ID del usuario: "))
            agregar_liquidacion(indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario)
            print("Liquidación agregada exitosamente.")

        elif opcion == "3":
            id_usuario = int(input("Ingresa el ID del usuario a consultar: "))
            consultar_usuario(id_usuario)

        elif opcion == "4":
            id_usuario = int(input("Ingresa el ID del usuario a eliminar: "))
            eliminar_usuario(id_usuario)
            print("Usuario eliminado exitosamente.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
