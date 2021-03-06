import unittest
from code.backend_algorithm import Splitter


class BasicTestCase(unittest.TestCase):
    """Contiene los metodos para las pruebas unitarias."""

    def setUp(self):
        self.splitter = Splitter()
        self.empty = []  # empty array for testing empty array result==0
        self.array = [1, 3, 3, 8, 4, 3, 2, 3, 3]  # an array with the values that add up to 15 each division giving 1 as output
        self.notsplit = [1, 3, 3, 8, 4, 3, 2, 3, 2]  # The output of this array must be -1
 
        self.resultempty = self.splitter.canBeSplitted(self.empty)
        self.result = self.splitter.canBeSplitted(self.array)
        self.resultnotsplit = self.splitter.canBeSplitted(self.notsplit)

    def tearDown(self):
        del self.splitter
        self.empty = None
        self.array = None
        self.resultempty = None
        self.result = None

    def test_splitter_exists(self):
        """Comprueba que el objeto de Splitter exista."""
        self.assertNotEqual(self.splitter, None)

    def test_arrayIsEmpty(self):
        """Comprueba si el array ingresado esta vacio.

        La salida esperada es 0
        """
        self.assertEqual(self.resultempty, 0)
        self.assertNotEqual(self.result, 0)

    def test_array_can_be_splitted(self):
        """Comprueba si se puede separar el array.

        La salida esperada es 1.
        """
        self.assertEqual(self.result, 1)
        self.assertNotEqual(self.result, -1)
        self.assertNotEqual(self.result, 0)

    def test_array_cannot_be_splitted(self):
        """Comprueba si el array no puede ser separado.

        La salida esperada es -1
        """
        self.assertEqual(self.resultnotsplit, -1)
        self.assertNotEqual(self.resultnotsplit, 1)
        self.assertNotEqual(self.resultnotsplit, 0)
