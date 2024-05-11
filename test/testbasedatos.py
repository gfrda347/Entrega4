import unittest
from unittest.mock import patch
from src.controller.controlador import conectar_db, agregar_usuario, agregar_liquidacion, consultar_usuario, eliminar_usuario

class TestDatabaseFunctions(unittest.TestCase):

    @patch('database.psycopg2.connect')
    def test_conectar_db_success(self, mock_connect):
        mock_connect.return_value = 'mock_connection'
        result = conectar_db()
        self.assertEqual(result, 'mock_connection')

    @patch('database.psycopg2.connect')
    def test_conectar_db_error(self, mock_connect):
        mock_connect.side_effect = Exception('Test exception')
        result = conectar_db()
        self.assertIsNone(result)

    @patch('database.conectar_db')
    def test_agregar_usuario_success(self, mock_conectar_db):
        mock_conn = mock_conectar_db.return_value
        mock_cursor = mock_conn.cursor.return_value
        agregar_usuario('John', 'Doe', '12345678', 'john@example.com', '1234567890', '2022-01-01', '2023-12-31', 5000)
        mock_cursor.execute.assert_called_with(
            "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            ('John', 'Doe', '12345678', 'john@example.com', '1234567890', '2022-01-01', '2023-12-31', 5000)
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('database.conectar_db')
    def test_agregar_usuario_error(self, mock_conectar_db):
        mock_conectar_db.return_value = None
        with self.assertRaises(Exception):
            agregar_usuario('John', 'Doe', '12345678', 'john@example.com', '1234567890', '2022-01-01', '2023-12-31', 5000)

    @patch('database.conectar_db')
    def test_agregar_liquidacion_success(self, mock_conectar_db):
        mock_conn = mock_conectar_db.return_value
        mock_cursor = mock_conn.cursor.return_value
        agregar_liquidacion(1000, 500, 800, 100, 300, 200, 2500, 1)
        mock_cursor.execute.assert_called_with(
            "INSERT INTO liquidacion (Indemnizacion, Vacaciones, Cesantias, Intereses_Sobre_Cesantias, Prima_Servicios, Retencion_Fuente, Total_A_Pagar, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (1000, 500, 800, 100, 300, 200, 2500, 1)
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('database.conectar_db')
    def test_agregar_liquidacion_error(self, mock_conectar_db):
        mock_conectar_db.return_value = None
        with self.assertRaises(Exception):
            agregar_liquidacion(1000, 500, 800, 100, 300, 200, 2500, 1)

    @patch('database.conectar_db')
    def test_consultar_usuario_success(self, mock_conectar_db):
        mock_conn = mock_conectar_db.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = (1, 'John', 'Doe', '12345678', 'john@example.com', '1234567890', '2022-01-01', '2023-12-31', 5000)
        consultar_usuario(1)
        mock_cursor.execute.assert_called_with("SELECT * FROM usuarios WHERE ID_Usuario = %s", (1,))
        mock_conn.close.assert_called_once()

    @patch('database.conectar_db')
    def test_consultar_usuario_error(self, mock_conectar_db):
        mock_conectar_db.return_value = None
        with self.assertRaises(Exception):
            consultar_usuario(1)

    @patch('database.conectar_db')
    def test_eliminar_usuario_success(self, mock_conectar_db):
        mock_conn = mock_conectar_db.return_value
        mock_cursor = mock_conn.cursor.return_value
        eliminar_usuario(1)
        mock_cursor.execute.assert_called_with("DELETE FROM usuarios WHERE ID_Usuario = %s", (1,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('database.conectar_db')
    def test_eliminar_usuario_error(self, mock_conectar_db):
        mock_conectar_db.return_value = None
        with self.assertRaises(Exception):
            eliminar_usuario(1)

if __name__ == '__main__':
    unittest.main()
