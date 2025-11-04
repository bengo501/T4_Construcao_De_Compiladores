"""
executa todos os testes individuais
"""

import subprocess
import sys

def executar_teste(numero):
    """executa um teste específico"""
    nome_arquivo = f"teste_{numero:02d}_*.py"
    print(f"\n{'='*60}")
    print(f"teste {numero}")
    print(f"{'='*60}")
    
    # encontra o arquivo correspondente
    import glob
    arquivos = glob.glob(f"teste_{numero:02d}_*.py")
    
    if not arquivos:
        print(f"arquivo teste_{numero:02d}_*.py nao encontrado")
        return False
    
    arquivo = arquivos[0]
    print(f"executando: {arquivo}")
    print()
    
    try:
        resultado = subprocess.run([sys.executable, arquivo], 
                                 capture_output=True, 
                                 text=True,
                                 encoding='utf-8',
                                 errors='ignore')
        print(resultado.stdout)
        if resultado.stderr:
            print("erros:")
            print(resultado.stderr)
        return resultado.returncode == 0
    except Exception as e:
        print(f"erro ao executar {arquivo}: {e}")
        return False

def executar_todos():
    """executa todos os testes"""
    print("=" * 60)
    print("executando todos os testes individuais")
    print("=" * 60)
    
    resultados = []
    for i in range(1, 11):
        sucesso = executar_teste(i)
        resultados.append((i, sucesso))
    
    print("\n" + "=" * 60)
    print("resumo dos testes")
    print("=" * 60)
    
    sucessos = sum(1 for _, s in resultados if s)
    falhas = len(resultados) - sucessos
    
    print(f"testes executados: {len(resultados)}")
    print(f"testes passaram: {sucessos}")
    print(f"testes falharam: {falhas}")
    
    if falhas > 0:
        print("\ntestes que falharam:")
        for numero, sucesso in resultados:
            if not sucesso:
                print(f"  - teste {numero}")
    
    return falhas == 0

if __name__ == "__main__":
    sucesso = executar_todos()
    if sucesso:
        print("\n[ok] todos os testes passaram!")
    else:
        print("\n[erro] alguns testes falharam")
    sys.exit(0 if sucesso else 1)

