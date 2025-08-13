import unittest
from nome import sobrenome_na_ordem

print(sobrenome_na_ordem('José', 'Dias', 'Saraiva'))

class NomeTest(unittest.TestCase):

    def test_sobrenome_na_ordem(self):

        nome_completo = sobrenome_na_ordem('João', 'Madureira', 'Silva')
        self.assertEqual(nome_completo, 'João Silva Madureira')

unittest.main(argv=[''], exit=False)