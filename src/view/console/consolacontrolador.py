import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controller.controlador import conectar_db, agregar_usuario, agregar_liquidacion, consultar_usuario, eliminar_usuario, eliminar_liquidacion

def main_menu():
    while True:
        print("Selecciona una opción:")
        print("1. Agregar usuario")
        print("2. Agregar liquidación")
        print("3. Consultar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        print("6. Eliminar Liquidación")

        try:
            opcion = int(input("Ingresa el número de la opción: "))
        except ValueError:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            continue

        if opcion == 1:
            nombre = input("Ingresa el nombre del usuario: ")
            apellido = input("Ingresa el apellido del usuario: ")
            documento_identidad = input("Ingresa el documento de identidad del usuario: ")
            correo_electronico = input("Ingresa el correo electrónico del usuario: ")
            telefono = input("Ingresa el teléfono del usuario: ")
            fecha_ingreso = input("Ingresa la fecha de ingreso del usuario (AAAA-MM-DD): ")
            fecha_salida = input("Ingresa la fecha de salida del usuario (AAAA-MM-DD): ")
            try:
                salario = float(input("Ingresa el salario del usuario: "))
            except ValueError:
                print("Salario inválido. Por favor, ingresa un valor numérico.")
                continue
            agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario)
            print("Usuario agregado exitosamente.")

        elif opcion == 2:
            try:
                indemnizacion = float(input("Ingresa el valor de la indemnización: "))
            except ValueError:
                print("Indemnización inválida. Por favor, ingresa un valor numérico.")
                continue
            try:
                vacaciones = float(input("Ingresa el valor de las vacaciones: "))
            except ValueError:
                print("Vacaciones inválidas. Por favor, ingresa un valor numérico.")
                continue
            try:
                cesantias = float(input("Ingresa el valor de las cesantías: "))
            except ValueError:
                print("Cesantías inválidas. Por favor, ingresa un valor numérico.")
                continue
            try:
                intereses_sobre_cesantias = float(input("Ingresa el valor de los intereses sobre cesantías: "))
            except ValueError:
                print("Intereses sobre cesantías inválidos. Por favor, ingresa un valor numérico.")
                continue
            try:
                prima_servicios = float(input("Ingresa el valor de la prima de servicios: "))
            except ValueError:
                print("Prima de servicios inválida. Por favor, ingresa un valor numérico.")
                continue
            try:
                retencion_fuente = float(input("Ingresa el valor de la retención en la fuente: "))
            except ValueError:
                print("Retención en la fuente inválida. Por favor, ingresa un valor numérico.")
                continue
            try:
                total_a_pagar = float(input("Ingresa el valor total a pagar: "))
            except ValueError:
                print("Total a pagar inválido. Por favor, ingresa un valor numérico.")
                continue
            try:
                id_usuario = int(input("Ingresa el ID del usuario: "))
            except ValueError:
                print("ID de usuario inválido. Por favor, ingresa un valor numérico.")
                continue
            agregar_liquidacion(indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario)
            print("Liquidación agregada exitosamente.")

        elif opcion == 3:
            try:
                id_usuario = int(input("Ingresa el ID del usuario a consultar: "))
            except ValueError:
                print("ID de usuario inválido. Por favor, ingresa un valor numérico.")
                continue
            consultar_usuario(id_usuario)

        elif opcion == 4:
            try:
                id_usuario = int(input("Ingresa el ID del usuario a eliminar: "))
            except ValueError:
                print("ID de usuario inválido. Por favor, ingresa un valor numérico.")
                continue
            try:
                eliminar_usuario(id_usuario)
                print("Usuario eliminado exitosamente.")
            except ValueError:
                print("Error al eliminar el usuario. Por favor, verifica el ID.")

        elif opcion == 5:
            print("Saliendo delmenú...")
            sys.exit()

        elif opcion == 6:
            try:
                id_liquidacion = int(input("Ingresa el ID de la liquidación a eliminar: "))
            except ValueError:
                print("ID de liquidación inválido. Por favor, ingresa un valor numérico.")
                continue
            try:
                eliminar_liquidacion(id_liquidacion)
                print("Liquidación eliminada exitosamente.")
            except ValueError:
                print("Error al eliminar la liquidación. Por favor, verifica el ID.")

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main_menu()