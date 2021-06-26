import sys
sys.path.append('')

from leilao.exceptions import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self.__valor_e_valido(valor):
            raise LanceInvalido('Não pode propor um lance com valor maior que o da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    def __valor_e_valido(self, valor):
        return valor <= self.__carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    def propoe(self, lance: Lance):
        if self.__lance_e_valido(lance):
            if not self.__tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def __tem_lances(self):
        return self.__lances

    def __usuarios_diferentes(self, lance):
        if self.lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O usuário não pode fazer mais de um lance!')

    def __valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o valor do lance anterior!')

    def __lance_e_valido(self, lance):
        return not self.__tem_lances() or (self.__usuarios_diferentes(lance) and 
        self.__valor_maior_que_lance_anterior(lance))

    @property
    def lances(self):
        return self.__lances[:]


