from model.models import Cinema, Filme, Sessao
from repository.repositories import CinemaRepository, FilmeRepository, SessaoRepository

class CinemaService:
    def __init__(self):
        self.repo = CinemaRepository()

    def cadastrar(self, nome, cidade, capacidade):
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser maior que zero.")
        self.repo.salvar(Cinema(nome, cidade, capacidade))

    def listar(self):
        return self.repo.listar()


class FilmeService:
    def __init__(self):
        self.repo = FilmeRepository()

    def cadastrar(self, titulo, genero, diretor):
        self.repo.salvar(Filme(titulo, genero, diretor))

    def listar(self):
        return self.repo.listar()

    def listar_por_cinema(self, id_cinema):
        return self.repo.listar_por_cinema(id_cinema)


class SessaoService:
    def __init__(self):
        self.repo = SessaoRepository()
        self.cinema_repo = CinemaRepository()
        self.filme_repo = FilmeRepository()

    # UC01 — Cadastrar Sessão
    def cadastrar(self, id_cinema, id_filme, data, horario, sala):
        if not self.cinema_repo.buscar_por_id(id_cinema):
            raise ValueError("Cinema não encontrado.")
        if not self.filme_repo.buscar_por_id(id_filme):
            raise ValueError("Filme não encontrado.")
        self.repo.salvar(Sessao(id_cinema, id_filme, data, horario, sala))

    # UC02 — Registrar Público
    def registrar_publico(self, id_sessao, publico):
        if publico < 0:
            raise ValueError("Público não pode ser negativo.")
        self.repo.atualizar_publico(id_sessao, publico)

    def listar(self):
        return self.repo.listar()