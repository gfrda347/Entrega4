import sys
import os
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)
from controller.controlador import conectar_db, agregar_usuario, agregar_liquidacion, consultar_usuario, eliminar_usuario
import unittest
from unittest.mock import patch, MagicMock
import SecretConfig

class TestConsultarUsuario(unittest.TestCase):
    def test_consultar_usuario(self):
        id_usuario = 1
        consultar_usuario(id_usuario)

class TestEliminarUsuario(unittest.TestCase):
    def test_eliminar_usuario(self):
        id_usuario = 1
        eliminar_usuario(id_usuario)

class TestConectarDBError(unittest.TestCase):
    def test_conectar_db_error(self):
        SecretConfig.PGHOST = "invalid_host"
        conn = conectar_db()
        self.assertIsNone(conn)

class TestConsultarUsuarioNoExistente(unittest.TestCase):
    def test_consultar_usuario_no_existente(self):
        id_usuario = 999
        consultar_usuario(id_usuario)

if __name__ == '__main__':
    unittest.main()
