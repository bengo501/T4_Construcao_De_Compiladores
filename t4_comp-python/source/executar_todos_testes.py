# executa todos os testes individuais
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent #diretório raiz do projeto
PROJECT_ROOT = BASE_DIR.parent #diretório raiz do projeto
TEST_DIR = BASE_DIR / "teste" #diretório de testes
TESTES = [
    ("expressao de atribuicao", "teste_01_expressao_atribuicao.py"), #teste 1 expressao de atribuicao 
    ("incremento e decremento", "teste_02_incremento_decremento.py"), #teste 2 incremento e decremento
    ("operador mais igual", "teste_03_operador_mais_igual.py"), #teste 3 operador mais igual
    ("operador condicional", "teste_04_operador_condicional.py"), #teste 4 operador condicional
    ("comando do while", "teste_05_do_while.py"), #teste 5 comando do while
    ("comando for", "teste_06_for.py"), #teste 6 comando for
    ("break e continue", "teste_07_break_continue.py"), #teste 7 break e continue
    ("struct simples", "teste_08_struct.py"), #teste 8 struct simples
    ("array de inteiros", "teste_09_array_inteiros.py"), #teste 9 array de inteiros
    ("struct com array", "teste_10_struct_com_array.py"), #teste 10 struct com array
    ("array de structs", "teste_11_array_de_structs.py"), #teste 11 array de structs
] #lista de testes
#---------------------------------------------------------------------------------------------------------
def executar_teste(indice, descricao, arquivo): #executa um teste específico
    print(f"\n======================================================")
    print(f"teste {indice}: {descricao}") #exibe o nome do teste
    print(f"======================================================")

    caminho = TEST_DIR / arquivo #caminho do arquivo de teste
    if not caminho.exists(): #verifica se o arquivo de teste existe
        print(f"arquivo {arquivo} nao encontrado em {TEST_DIR}") 
        return False 

    print(f"executando: {caminho.relative_to(BASE_DIR)}\n") #exibe o caminho do arquivo de teste

    try: #tenta executar o arquivo de teste
        resultado = subprocess.run(  #executa o arquivo de teste
            [sys.executable, str(caminho)], 
            capture_output=True, #captura o resultado do teste
            text=True, #exibe o resultado do teste
            encoding="utf-8", #codifica o resultado do teste
            errors="ignore", #ignora os erros
            cwd=PROJECT_ROOT, #diretório raiz do projeto
        )
        print(resultado.stdout) #exibe o resultado do teste
        if resultado.stderr:
            print("erros:")
            print(resultado.stderr)
        return resultado.returncode == 0 #retorna True se o teste passou False se falhou
    except Exception as e:  # pylint: disable=broad-except
        print(f"erro ao executar {arquivo}: {e}")
        return False
#---------------------------------------------------------------------------------------------------------
def executar_todos():    #executa todos os testes
    print("======================================================")
    print("executando todos os testes individuais")
    print("======================================================")
    resultados = []
    for indice, (descricao, arquivo) in enumerate(TESTES, start=1): #executa todos os testes
        sucesso = executar_teste(indice, descricao, arquivo) #executa o teste especifico 
        resultados.append((indice, descricao, sucesso)) #adiciona o resultado do teste na lista

    print("\n" + "======================================================")
    print("resumo dos testes")
    print("======================================================")

    sucessos = sum(1 for _, _, s in resultados if s) #calcula o número de testes que passaram
    falhas = len(resultados) - sucessos #calcula o número de testes que falharam

    print(f"testes executados: {len(resultados)}")
    print(f"testes passaram: {sucessos}")
    print(f"testes falharam: {falhas}")

    if falhas > 0: #se houver testes que falharam
        print("\ntestes que falharam:")
        for indice, descricao, sucesso in resultados:
            if not sucesso:
                print(f"  - teste {indice}: {descricao}")
    return falhas == 0
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__": #executa todos os testes
    sucesso = executar_todos()  
    if sucesso: #todos os testes passaram
        print("\n[ok] todos os testes passaram!")
    else: #alguns testes falharam
        print("\n[erro] alguns testes falharam")
    sys.exit(0 if sucesso else 1) #0 se todos os testes passaram 
                                  #1 se alguns testes falharam