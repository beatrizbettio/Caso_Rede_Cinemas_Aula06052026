from controller.controllers import CinemaController, FilmeController, SessaoController
from view.views import CinemaView, FilmeView, SessaoView

def main():
    cinema_ctrl = CinemaController(CinemaView())
    filme_ctrl  = FilmeController(FilmeView())
    sessao_ctrl = SessaoController(SessaoView())

    opcoes = {
        "1": ("Cadastrar Cinema",            cinema_ctrl.cadastrar),
        "2": ("Listar Cinemas",              cinema_ctrl.listar),
        "3": ("Cadastrar Filme",             filme_ctrl.cadastrar),
        "4": ("Listar Filmes por Cinema",    filme_ctrl.listar_por_cinema),  # UC03
        "5": ("Cadastrar Sessão",            sessao_ctrl.cadastrar),         # UC01
        "6": ("Listar Sessões",              sessao_ctrl.listar),
        "7": ("Registrar Público",           sessao_ctrl.registrar_publico), # UC02
    }

    while True:
        print("=" * 36)
        print("      REDE DE CINEMAS — MENU")
        print("=" * 36)
        for k, (desc, _) in opcoes.items():
            print(f"  {k} - {desc}")
        print("  0 - Sair")
        print("=" * 36)
        op = input("Opção: ").strip()
        if op == "0":
            print("Encerrando sistema.")
            break
        elif op in opcoes:
            opcoes[op][1]()
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    main()