from service.services import CinemaService, FilmeService, SessaoService

class CinemaController:
    def __init__(self, view):
        self.service = CinemaService()
        self.view = view

    def cadastrar(self):
        nome, cidade, capacidade = self.view.obter_dados()
        try:
            self.service.cadastrar(nome, cidade, capacidade)
            self.view.mensagem("Cinema cadastrado com sucesso!")
        except ValueError as e:
            self.view.mensagem(f"Erro: {e}")

    def listar(self):
        self.view.mostrar(self.service.listar())


class FilmeController:
    def __init__(self, view):
        self.service = FilmeService()
        self.view = view

    def cadastrar(self):
        titulo, genero, diretor = self.view.obter_dados()
        self.service.cadastrar(titulo, genero, diretor)
        self.view.mensagem("Filme cadastrado com sucesso!")

    def listar(self):
        self.view.mostrar(self.service.listar())

    # UC03 — Listar Filmes em Cartaz por Cinema
    def listar_por_cinema(self):
        id_cinema = int(input("ID do Cinema: "))
        filmes = self.service.listar_por_cinema(id_cinema)
        self.view.mostrar(filmes)


class SessaoController:
    def __init__(self, view):
        self.service = SessaoService()
        self.view = view

    # UC01 — Cadastrar Sessão
    def cadastrar(self):
        dados = self.view.obter_dados()
        try:
            self.service.cadastrar(*dados)
            self.view.mensagem("Sessão cadastrada com sucesso!")
        except ValueError as e:
            self.view.mensagem(f"Erro: {e}")

    # UC02 — Registrar Público
    def registrar_publico(self):
        id_sessao, publico = self.view.obter_publico()
        try:
            self.service.registrar_publico(id_sessao, publico)
            self.view.mensagem("Público registrado com sucesso!")
        except ValueError as e:
            self.view.mensagem(f"Erro: {e}")

    def listar(self):
        self.view.mostrar(self.service.listar())