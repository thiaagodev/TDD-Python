import unittest
from unittest import TestCase

from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        cleiton = Usuario('Cleiton')
        jorge = Usuario('Jorge')

        lance_do_jorge = Lance(jorge, 100)
        lance_do_cleiton = Lance(cleiton, 150)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_jorge)
        leilao.lances.append(lance_do_cleiton)

        
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        manor_valor_esperado = 100
        maior_valor_esperado = 150
        self.assertEqual(manor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


unittest.main()
