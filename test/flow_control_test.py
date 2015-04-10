# -*- coding: utf-8 -*-

import unittest
from sample import flow_control_sample

class IfTestCase(unittest.TestCase):

    def setUp(self):
        self.list = [1, 2, 3, 4, 5, 6, 'Emicida', 'Criolo']
        self.dict = {'nome': 'Bruno Konrad', 'idade': 21}

    def test_basic(self):
        m = flow_control_sample.basic_if(20)
        self.assertEqual(m, flow_control_sample.MESSAGE)

    def test_basic_failure(self):
        m = flow_control_sample.basic_if(20, 21, 'Nunca será')
        self.assertIsNone(m)

    def test_in(self):
        # Verificando se um VALOR está dentro de um objeto List
        emicida = flow_control_sample.value_in_if(self.list, 'Emicida')
        one = flow_control_sample.value_in_if(self.list, 1, 'Oh, that is the one')
        # verificando se uma CHAVE está dentro de um objeto Dictionary
        bruno = flow_control_sample.value_in_if(self.dict, 'nome')

        self.assertEqual(emicida, flow_control_sample.MESSAGE)
        self.assertEqual(one, 'Oh, that is the one')
        self.assertEqual(bruno, flow_control_sample.MESSAGE)

    def test_in_failure(self):
        racionais = flow_control_sample.value_in_if(self.list, 'Racionais')
        gostos = flow_control_sample.value_in_if(self.dict, 'gostos', fail='Sem graça')

        self.assertIsNone(racionais)
        self.assertEqual(gostos, 'Sem graça')

    def _sum(self, x, s):
        return x + s

    def test_basic_for(self):
        result = flow_control_sample.basic_for(3, lambda x, y: (x * 2) + y)
        s = flow_control_sample.basic_for(10, self._sum)
        s_withou_7 = flow_control_sample.basic_for_continue(10, self._sum, lambda x: x == 7)

        self.assertEqual(result, 6)
        self.assertEqual(s, 45)
        self.assertEqual(s_withou_7, 38)

    def test_function_args(self):
        l = flow_control_sample.basic_function_args(1, 2, 3, 4, 5, 6)
        pessoa = flow_control_sample.basic_function_kwargs(nome='Bruno Konrad', idade=21)

        self.assertEqual(l, (1, 2, 3, 4, 5, 6))
        self.assertEqual(pessoa, self.dict)


if __name__ == '__main__':
    unittest.main()
