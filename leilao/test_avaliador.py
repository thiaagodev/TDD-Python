import unittest
from unittest import TestCase

from dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):

        cleiton = Usuario('Cleiton')
       
        self.lance_do_cleiton = Lance(cleiton, 150)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        jorge = Usuario('Jorge')
        lance_do_jorge = Lance(jorge, 100)

        self.leilao.propoe(self.lance_do_cleiton)
        self.leilao.propoe(lance_do_jorge)

        menor_valor_esperado = 100
        maior_valor_esperado = 150
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        jorge = Usuario('Jorge')

        lance_do_jorge = Lance(jorge, 100)

        self.leilao.propoe(lance_do_jorge)
        self.leilao.propoe(self.lance_do_cleiton)

        menor_valor_esperado = 100
        maior_valor_esperado = 150
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_do_cleiton)

        menor_valor_esperado = 150
        maior_valor_esperado = 150
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        jorge = Usuario('Jorge')
        vini = Usuario('Vini')

        lance_do_vini = Lance(vini, 300)
        lance_do_jorge = Lance(jorge, 200)
        
        self.leilao.propoe(self.lance_do_cleiton)
        self.leilao.propoe(lance_do_jorge)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 150
        maior_valor_esperado = 300
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


unittest.main()
