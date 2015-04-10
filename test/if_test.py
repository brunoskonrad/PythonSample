# -*- coding: utf-8 -*-

import unittest
from sample import if_sample

class IfTestCase(unittest.TestCase):

    def setUp(self):
        self.list = [1, 2, 3, 4, 5, 6, 'Emicida', 'Criolo']
        self.dict = {'nome': 'Bruno Konrad', 'idade': 21}

    def test_basic(self):
        m = if_sample.basic(20)
        self.assertEqual(m, if_sample.MESSAGE)

    def test_basic_failure(self):
        m = if_sample.basic(20, 21, 'Nunca será')
        self.assertIsNone(m)

    def test_in(self):
        # Verificando se um VALOR está dentro de um objeto List
        emicida = if_sample.value_in(self.list, 'Emicida')
        one = if_sample.value_in(self.list, 1, 'Oh, that is the one')
        # verificando se uma CHAVE está dentro de um objeto Dictionary
        bruno = if_sample.value_in(self.dict, 'nome')

        self.assertEqual(emicida, if_sample.MESSAGE)
        self.assertEqual(one, 'Oh, that is the one')
        self.assertEqual(bruno, if_sample.MESSAGE)

    def test_in_failure(self):
        racionais = if_sample.value_in(self.list, 'Racionais')
        gostos = if_sample.value_in(self.dict, 'gostos', fail='Sem graça')

        self.assertIsNone(racionais)
        self.assertEqual(gostos, 'Sem graça')


if __name__ == '__main__':
    unittest.main()
