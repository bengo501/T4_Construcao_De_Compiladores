"""
executa todos os testes individuais
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
TEST_DIR = BASE_DIR / "teste"
TESTES = [
    ("expressao de atribuicao", "testar.py"),
    ("incremento e decremento", "teste_02_incremento_decremento.py"),
    ("operador mais igual", "teste_03_operador_mais_igual.py"),
    ("operador condicional", "teste_04_operador_condicional.py"),
    ("comando do while", "teste_05_do_while.py"),
    ("comando for", "teste_06_for.py"),
    ("break e continue", "teste_07_break_continue.py"),
    ("struct simples", "teste_08_struct.py"),
    ("array de inteiros", "teste_09_array_inteiros.py"),
    ("struct com array", "teste_10_struct_com_array.py"),
    ("array de structs", "teste_11_array_de_structs.py"),
]


def executar_teste(indice, descricao, arquivo):
    """executa um teste específico"""
    print(f"\n{'=' * 60}")
    print(f"teste {indice}: {descricao}")
    print(f"{'=' * 60}")

    caminho = TEST_DIR / arquivo
    if not caminho.exists():
        print(f"arquivo {arquivo} nao encontrado em {TEST_DIR}")
        return False

    print(f"executando: {caminho.relative_to(BASE_DIR)}\n")

    try:
        resultado = subprocess.run(
            [sys.executable, str(caminho)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            cwd=PROJECT_ROOT,
        )
        print(resultado.stdout)
        if resultado.stderr:
            print("erros:")
            print(resultado.stderr)
        return resultado.returncode == 0
    except Exception as e:  # pylint: disable=broad-except
        print(f"erro ao executar {arquivo}: {e}")
        return False


def executar_todos():
    """executa todos os testes"""
    print("=" * 60)
    print("executando todos os testes individuais")
    print("=" * 60)

    resultados = []
    for indice, (descricao, arquivo) in enumerate(TESTES, start=1):
        sucesso = executar_teste(indice, descricao, arquivo)
        resultados.append((indice, descricao, sucesso))

    print("\n" + "=" * 60)
    print("resumo dos testes")
    print("=" * 60)

    sucessos = sum(1 for _, _, s in resultados if s)
    falhas = len(resultados) - sucessos

    print(f"testes executados: {len(resultados)}")
    print(f"testes passaram: {sucessos}")
    print(f"testes falharam: {falhas}")

    if falhas > 0:
        print("\ntestes que falharam:")
        for indice, descricao, sucesso in resultados:
            if not sucesso:
                print(f"  - teste {indice}: {descricao}")

    return falhas == 0


if __name__ == "__main__":
    sucesso = executar_todos()
    if sucesso:
        print("\n[ok] todos os testes passaram!")
    else:
        print("\n[erro] alguns testes falharam")
    sys.exit(0 if sucesso else 1)