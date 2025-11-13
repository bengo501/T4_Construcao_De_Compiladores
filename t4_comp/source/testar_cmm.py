#script para testar os arquivos .cmm
#executa os testes correspondentes aos arquivos t01.cmm até t08.cmm
import subprocess
import sys
from pathlib import Path

# configuração de paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
TEST_DIR = BASE_DIR / "teste"

# lista de testes cmm
TESTES_CMM = [
    ("t01.cmm: expressão de atribuição complexa", "teste_t01_cmm.py"),
    ("t02.cmm: operador += encadeado", "teste_t02_cmm.py"),
    ("t03.cmm: incremento/decremento complexo", "teste_t03_cmm.py"),
    ("t04.cmm: break e continue aninhados", "teste_t04_cmm.py"),
    ("t05.cmm: for com várias variações", "teste_t05_cmm.py"),
    ("t06.cmm: incremento/decremento em atribuições", "teste_t06_cmm.py"),
    ("t07.cmm: operador condicional ?: aninhado", "teste_t07_cmm.py"),
    ("t08.cmm: do-while", "teste_t08_cmm.py"),
]

def executar_teste(arquivo_teste):
    """executa um teste e retorna a saída"""
    caminho = TEST_DIR / arquivo_teste
    if not caminho.exists():
        return None
    
    try:
        resultado = subprocess.run(
            [sys.executable, str(caminho)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            cwd=PROJECT_ROOT,
        )
        return resultado.stdout
    except Exception as e:
        return f"erro ao executar: {e}"

def mostrar_teste(indice, descricao, arquivo_teste):
    """executa um teste e mostra resultado"""
    print("=" * 60)
    print(f"teste {indice}: {descricao}")
    print("=" * 60)
    print(f"executando: teste\\{arquivo_teste}")
    print()
    
    # executa o teste
    saida_teste = executar_teste(arquivo_teste)
    
    if saida_teste:
        # mostra saída
        linhas = saida_teste.splitlines()
        em_codigo = False
        codigo_linhas = []
        
        for linha in linhas:
            if "codigo gerado" in linha.lower():
                em_codigo = True
                continue
            if em_codigo and linha.strip():
                codigo_linhas.append(linha)
            elif em_codigo and not linha.strip() and codigo_linhas:
                break
        
        if codigo_linhas:
            print("codigo gerado:")
            print("\n".join(codigo_linhas))
            print()
        else:
            print("codigo gerado: (não encontrado na saída)")
            print(saida_teste)
    else:
        print("[erro] teste não encontrado ou erro ao executar")
    
    print()
    return True

def executar_todos():
    """executa todos os testes cmm"""
    print("=" * 60)
    print("testes dos arquivos .cmm")
    print("=" * 60)
    print()
    
    for indice, (descricao, arquivo_teste) in enumerate(TESTES_CMM, start=1):
        try:
            mostrar_teste(indice, descricao, arquivo_teste)
        except Exception as e:
            print(f"[erro] erro ao processar teste {indice}: {e}")
            print()
    
    print("=" * 60)
    print("fim dos testes")
    print("=" * 60)

if __name__ == "__main__":
    executar_todos()

