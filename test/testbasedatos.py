import sys
sys.path.append(".")
from src.controller.controlador import conectar_db, agregar_usuario, agregar_liquidacion, consultar_usuario, eliminar_usuario
import unittest
from unittest.mock import patch, MagicMock
import psycopg2

class TestFunciones(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_agregar_usuario_exitoso(self, mock_connect):
    # Configurar el mock para simular una conexión exitosa
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1  # Simular que se insertó un registro
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

    # Llamar a la función con datos válidos
        agregar_usuario("Juan", "Pérez", "1234567890", "juan@example.com", "555-1234", "2022-01-01", "2022-12-31", 50000)

    # Verificar que se ejecutó el comando SQL correcto
        mock_cursor.execute.assert_called_with("INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", ("Juan", "Pérez", "1234567890", "juan@example.com", "555-1234", "2022-01-01", "2022-12-31", 50000))

    @patch('psycopg2.connect')
    def test_agregar_usuario_error(self, mock_connect):
    # Configurar el mock para simular un error de conexión
        mock_connect.side_effect = psycopg2.Error("Error de conexión simulado")

    # Capturar la salida de la función
        with self.assertLogs() as captured:
            agregar_usuario("Juan", "Pérez", "1234567890", "juan@example.com", "555-1234", "2022-01-01", "2022-12-31", 50000)
            self.assertEqual(captured.records[0].getMessage(), "Error al agregar el usuario: Error de conexión simulado")


if __name__ == '__main__':
    unittest.main()
