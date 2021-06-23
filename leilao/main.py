from dominio import Leilao, Lance, Usuario, Avaliador

cleiton = Usuario('Cleiton')
jorge = Usuario('Jorge')

lance_do_jorge = Lance(jorge, 100)
lance_do_cleiton = Lance(cleiton, 150)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_cleiton)
leilao.lances.append(lance_do_jorge)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi {avaliador.maior_lance}')
