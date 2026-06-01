import os
import subprocess


def limpar_tela():
    """Limpa o console do usuário (suporta nativamente Windows e Unix/Mac)."""
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
