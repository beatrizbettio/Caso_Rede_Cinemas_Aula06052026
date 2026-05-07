class Cinema:
    def __init__(self, nome, cidade, capacidade, id=None):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.capacidade = capacidade

class Filme:
    def __init__(self, titulo, genero, diretor, id=None):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.diretor = diretor

class Sessao:
    def __init__(self, id_cinema, id_filme, data, horario, sala, publico=0, id=None):
        self.id = id
        self.id_cinema = id_cinema
        self.id_filme = id_filme
        self.data = data
        self.horario = horario
        self.sala = sala
        self.publico = publico