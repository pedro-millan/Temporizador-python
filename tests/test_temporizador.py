import unittest
from src.main import Temporizador

class TestTemporizador(unittest.TestCase):

    def setUp(self):
        # Creamos un temporizador inicial para usar en los tests
        self.temporizador = Temporizador(23, 59, 59)

    def test_siguiente_segundo(self):
        self.temporizador.siguiente_segundo()
        self.assertEqual(str(self.temporizador), "00:00:00")

    def test_anterior_segundo(self):
        self.temporizador.anterior_segundo()
        self.assertEqual(str(self.temporizador), "23:59:58")

if __name__ == '__main__':
    unittest.main()