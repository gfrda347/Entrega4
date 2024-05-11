from model.calculadora import CalculadoraLiquidacion
import psycopg2

# Credenciales de la base de datos
PGHOST='ep-lively-snow-a5tp6y2b.us-east-2.aws.neon.tech'
PGDATABASE='Entrega4'
PGUSER='neondb_owner'
PGPASSWORD='************'

# Función para conectarse a la base de datos
def conectar_db():
    try:
        conn = psycopg2.connect(
            host=PGHOST,
            database=PGDATABASE,
            user=PGUSER,
            password=PGPASSWORD
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a la base de datos:", error)
        return None

# Función para agregar un nuevo usuario
def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario))
                conn.commit()
                print("Usuario agregado correctamente.")
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar el usuario:", error)

# Función para agregar una nueva liquidación
def agregar_liquidacion(indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO liquidacion (Indemnizacion, Vacaciones, Cesantias, Intereses_Sobre_Cesantias, Prima_Servicios, Retencion_Fuente, Total_A_Pagar, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario))
                conn.commit()
                print("Liquidación agregada correctamente.")
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar la liquidación:", error)

# Función para consultar los datos de un usuario
def consultar_usuario(id_usuario):
    try:
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
    except (Exception, psycopg2.Error) as error:
        print("Error al consultar el usuario:", error)

# Función para eliminar un usuario
def eliminar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "DELETE FROM usuarios WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                conn.commit()
                print("Usuario eliminado correctamente.")
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar el usuario:", error)

