class CinemaView:
    def obter_dados(self):
        nome = input("Nome do cinema: ")
        cidade = input("Cidade: ")
        capacidade = int(input("Capacidade: "))
        return nome, cidade, capacidade

    def mostrar(self, cinemas):
        print("\n=== Cinemas ===")
        for c in cinemas:
            print(f"[{c.id}] {c.nome} | {c.cidade} | Cap: {c.capacidade}")
        print("================\n")

    def mensagem(self, msg):
        print(f">> {msg}\n")


class FilmeView:
    def obter_dados(self):
        titulo = input("Título: ")
        genero = input("Gênero: ")
        diretor = input("Diretor: ")
        return titulo, genero, diretor

    def mostrar(self, filmes):
        print("\n=== Filmes ===")
        if not filmes:
            print("Nenhum filme encontrado.")
        for f in filmes:
            print(f"[{f.id}] {f.titulo} | {f.genero} | Dir: {f.diretor}")
        print("==============\n")

    def mensagem(self, msg):
        print(f">> {msg}\n")


class SessaoView:
    def obter_dados(self):
        id_cinema = int(input("ID do Cinema: "))
        id_filme  = int(input("ID do Filme: "))
        data      = input("Data (DD/MM/AAAA): ")
        horario   = input("Horário (HH:MM): ")
        sala      = input("Sala: ")
        return id_cinema, id_filme, data, horario, sala

    def obter_publico(self):
        id_sessao = int(input("ID da Sessão: "))
        publico   = int(input("Quantidade de público: "))
        return id_sessao, publico

    def mostrar(self, sessoes):
        print("\n=== Sessões ===")
        if not sessoes:
            print("Nenhuma sessão cadastrada.")
        for s in sessoes:
            print(f"[{s.id}] Cinema:{s.id_cinema} | Filme:{s.id_filme} | {s.data} {s.horario} | Sala:{s.sala} | Público:{s.publico}")
        print("================\n")

    def mensagem(self, msg):
        print(f">> {msg}\n")