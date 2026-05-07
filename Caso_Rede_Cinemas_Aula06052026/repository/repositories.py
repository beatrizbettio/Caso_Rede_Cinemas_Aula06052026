from db.database import get_connection
from model.models import Cinema, Filme, Sessao

class CinemaRepository:
    def salvar(self, cinema):
        conn = get_connection()
        conn.execute(
            "INSERT INTO cinemas (nome, cidade, capacidade) VALUES (?, ?, ?)",
            (cinema.nome, cinema.cidade, cinema.capacidade)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        rows = conn.execute("SELECT id, nome, cidade, capacidade FROM cinemas").fetchall()
        conn.close()
        return [Cinema(r[1], r[2], r[3], r[0]) for r in rows]

    def buscar_por_id(self, id):
        conn = get_connection()
        row = conn.execute("SELECT id, nome, cidade, capacidade FROM cinemas WHERE id=?", (id,)).fetchone()
        conn.close()
        return Cinema(row[1], row[2], row[3], row[0]) if row else None


class FilmeRepository:
    def salvar(self, filme):
        conn = get_connection()
        conn.execute(
            "INSERT INTO filmes (titulo, genero, diretor) VALUES (?, ?, ?)",
            (filme.titulo, filme.genero, filme.diretor)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        rows = conn.execute("SELECT id, titulo, genero, diretor FROM filmes").fetchall()
        conn.close()
        return [Filme(r[1], r[2], r[3], r[0]) for r in rows]

    def buscar_por_id(self, id):
        conn = get_connection()
        row = conn.execute("SELECT id, titulo, genero, diretor FROM filmes WHERE id=?", (id,)).fetchone()
        conn.close()
        return Filme(row[1], row[2], row[3], row[0]) if row else None

    def listar_por_cinema(self, id_cinema):
        conn = get_connection()
        rows = conn.execute("""
            SELECT DISTINCT f.id, f.titulo, f.genero, f.diretor
            FROM filmes f
            JOIN sessoes s ON s.id_filme = f.id
            WHERE s.id_cinema = ?
        """, (id_cinema,)).fetchall()
        conn.close()
        return [Filme(r[1], r[2], r[3], r[0]) for r in rows]


class SessaoRepository:
    def salvar(self, sessao):
        conn = get_connection()
        conn.execute(
            "INSERT INTO sessoes (id_cinema, id_filme, data, horario, sala) VALUES (?, ?, ?, ?, ?)",
            (sessao.id_cinema, sessao.id_filme, sessao.data, sessao.horario, sessao.sala)
        )
        conn.commit()
        conn.close()

    def atualizar_publico(self, id_sessao, publico):
        conn = get_connection()
        conn.execute("UPDATE sessoes SET publico=? WHERE id=?", (publico, id_sessao))
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        rows = conn.execute(
            "SELECT id, id_cinema, id_filme, data, horario, sala, publico FROM sessoes"
        ).fetchall()
        conn.close()
        return [Sessao(r[1], r[2], r[3], r[4], r[5], r[6], r[0]) for r in rows]