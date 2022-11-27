


class Filme:
    def __init__(self,nome, ano, duracao) -> None:
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.likes = 0
    
    def set_likes(self):
        self.likes += 1

class Serie:
    def __init__(self,nome, ano, temporadas) -> None:
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('Vingadores', '2018', 160)

print(vingadores.nome)

atlanta = Serie('Atlanta', 2018,2)