import sqlite3

def get_connection():
    conn = sqlite3.connect("cinema.db")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT,
            diretor TEXT
        );
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cinema INTEGER NOT NULL,
            id_filme INTEGER NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL,
            sala TEXT NOT NULL,
            publico INTEGER DEFAULT 0,
            FOREIGN KEY (id_cinema) REFERENCES cinemas(id),
            FOREIGN KEY (id_filme) REFERENCES filmes(id)
        );
    """)
    conn.commit()
    return conn