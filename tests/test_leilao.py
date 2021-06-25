import unittest
from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):

        self.cleiton = Usuario('Cleiton')
       
        self.lance_do_cleiton = Lance(self.cleiton, 150)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        jorge = Usuario('Jorge')
        lance_do_jorge = Lance(jorge, 100)

        self.leilao.propoe(lance_do_jorge)
        self.leilao.propoe(self.lance_do_cleiton)

        menor_valor_esperado = 100
        maior_valor_esperado = 150
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        jorge = Usuario('Jorge')
        lance_do_jorge = Lance(jorge, 100)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_cleiton)
            self.leilao.propoe(lance_do_jorge)

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

    # se o leilão não tiver lances deve permitir propor um lance
    def test_deve_permitir_porpor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_cleiton)
        
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    # se o último usuario for diferente deve permitir propor um lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        jorge = Usuario('Jorge')
        lance_do_jorge = Lance(jorge, 200)

        self.leilao.propoe(self.lance_do_cleiton)
        self.leilao.propoe(lance_do_jorge)

        quantidade_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances)

    # se o último usuario for o mesmo não deve permitir propor um lance
    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_cleiton_200 = Lance(self.cleiton, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_cleiton)
            self.leilao.propoe(lance_do_cleiton_200)


unittest.main()
