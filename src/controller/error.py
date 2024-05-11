from controller.controlador import conectar_db
import psycopg2

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (Exception, psycopg2.Error) as error:
            print(f"Error en la función {func.__name__}: {error}")
            conn = conectar_db()
            if conn:
                conn.rollback()  # Revertir la transacción en caso de error
                conn.close()
    return wrapper

@handle_error
def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, (nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario))
            conn.commit()
            print("Usuario agregado correctamente.")
        conn.close()

@handle_error
def agregar_liquidacion(indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO liquidacion (Indemnizacion, Vacaciones, Cesantias, Intereses_Sobre_Cesantias, Prima_Servicios, Retencion_Fuente, Total_A_Pagar, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, (indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario))
            conn.commit()
            print("Liquidación agregada correctamente.")
        conn.close()

@handle_error
def consultar_usuario(id_usuario):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM usuarios WHERE ID_Usuario = %s"
            cur.execute(sql, (id_usuario,))
            usuario = cur.fetchone()
            if usuario:
                print("Datos del usuario:")
                print("ID_Usuario:", usuario[0])
                print("Nombre:", usuario[1])
                print("Apellido:", usuario[2])
                print("Documento_Identidad:", usuario[3])
                print("Correo_Electronico:", usuario[4])
                print("Telefono:", usuario[5])
                print("Fecha_Ingreso:", usuario[6])
                print("Fecha_Salida:", usuario[7])
                print("Salario:", usuario[8])
            else:
                print("No se encontró el usuario.")
        conn.close()

@handle_error
def eliminar_usuario(id_usuario):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = "DELETE FROM usuarios WHERE ID_Usuario = %s"
            cur.execute(sql, (id_usuario,))
            conn.commit()
            print("Usuario eliminado correctamente.")
        conn.close()
