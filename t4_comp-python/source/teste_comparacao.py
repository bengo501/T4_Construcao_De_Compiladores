#script de teste com comparação
#executa os testes individuais e mostra código gerado vs código esperado
import subprocess
import sys
from pathlib import Path

# configuração de paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
TEST_DIR = BASE_DIR / "teste"
EXEMPLO_DIR = PROJECT_ROOT / "exemplo"

# lista de testes
TESTES = [
    ("expressao de atribuicao", "teste_01_expressao_atribuicao.py"),
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

def extrair_codigo_esperado(arquivo_txt):    #extrai o código esperado do arquivo .txt
    if not arquivo_txt.exists():
        return None
    
    conteudo = arquivo_txt.read_text(encoding="utf-8")
    
    # procura pelo marcador "código gerado:"
    marcador = "código gerado:"
    if marcador not in conteudo:
        return None
    
    # extrai o código após o marcador
    codigo = conteudo.split(marcador, 1)[1].strip()
    return codigo

def extrair_programa_fonte(arquivo_txt):    #extrai o programa fonte do arquivo .txt
    if not arquivo_txt.exists():
        return None
    
    conteudo = arquivo_txt.read_text(encoding="utf-8")
    
    # procura pelo marcador "programa fonte:"
    marcador = "programa fonte:"
    if marcador not in conteudo:
        return None
    
    # extrai até "código gerado:"
    codigo_marcador = "código gerado:"
    if codigo_marcador in conteudo:
        programa = conteudo.split(marcador, 1)[1].split(codigo_marcador, 1)[0].strip()
    else:
        programa = conteudo.split(marcador, 1)[1].strip()
    
    return programa

def executar_teste(arquivo_teste):    #executa um teste e retorna a saída
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

def extrair_codigo_gerado(saida):    #extrai o código gerado da saída do teste
    if not saida:
        return None
    
    linhas = saida.splitlines()
    codigo_linhas = []
    em_codigo = False
    
    # procura pelo marcador "codigo gerado:" ou "código gerado:"
    for i, linha in enumerate(linhas):
        linha_lower = linha.lower().strip()
        
        # encontra o marcador
        if "codigo gerado" in linha_lower:
            em_codigo = True
            continue
        
        # se está na seção de código, coleta as linhas
        if em_codigo:
            # para na próxima linha vazia se houver muitas linhas vazias seguidas
            # ou se encontrar outro marcador
            if linha.strip() == "" and i < len(linhas) - 1:
                # verifica se a próxima linha também está vazia ou é outro marcador
                if i + 1 < len(linhas):
                    prox_linha = linhas[i + 1].strip()
                    if prox_linha == "" or "teste" in prox_linha.lower() or "programa" in prox_linha.lower():
                        break
            codigo_linhas.append(linha)
    
    if not codigo_linhas:
        return None
    
    # remove linhas vazias do final
    while codigo_linhas and not codigo_linhas[-1].strip():
        codigo_linhas.pop()
    
    codigo = "\n".join(codigo_linhas).strip()
    return codigo if codigo else None

def comparar_codigos(gerado, esperado):    #compara dois códigos e retorna se são iguais
    if not gerado or not esperado:
        return False
    
    # normaliza: remove espaços extras e linhas vazias no final
    gerado_normalizado = "\n".join(linha.rstrip() for linha in gerado.strip().splitlines())
    esperado_normalizado = "\n".join(linha.rstrip() for linha in esperado.strip().splitlines())
    
    return gerado_normalizado == esperado_normalizado

def mostrar_teste(indice, descricao, arquivo_teste):    #executa um teste e mostra resultado com comparação
    print("=" * 60)
    print(f"teste {indice}: {descricao}")
    print("=" * 60)
    print(f"executando: teste\\{arquivo_teste}")
    print()
    
    # executa o teste
    saida_teste = executar_teste(arquivo_teste)
    
    # extrai código gerado
    codigo_gerado = extrair_codigo_gerado(saida_teste)
    
    # encontra arquivo .txt correspondente
    nome_base = arquivo_teste.replace(".py", "")
    arquivo_txt = EXEMPLO_DIR / f"{nome_base}.txt"
    
    # extrai código esperado e programa fonte
    codigo_esperado = extrair_codigo_esperado(arquivo_txt)
    programa_fonte = extrair_programa_fonte(arquivo_txt)
    
    # mostra programa fonte (do arquivo .txt se disponível, senão da saída)
    if programa_fonte:
        print("programa fonte:")
        print(programa_fonte)
        print()
    elif saida_teste:
        # tenta extrair programa fonte da saída
        linhas = saida_teste.splitlines()
        programa_linhas = []
        em_programa = False
        for linha in linhas:
            if "programa fonte" in linha.lower():
                em_programa = True
                continue
            if em_programa:
                if "codigo gerado" in linha.lower():
                    break
                # pula linha vazia logo após "programa fonte:"
                if not programa_linhas and linha.strip() == "":
                    continue
                programa_linhas.append(linha)
        if programa_linhas:
            print("programa fonte:")
            print("\n".join(programa_linhas).strip())
            print()
    
    # mostra código gerado
    if codigo_gerado:
        print("codigo gerado:")
        print(codigo_gerado)
        print()
    else:
        print("codigo gerado: (não encontrado na saída)")
        if saida_teste:
            print("saída completa:")
            print(saida_teste)
        print()
    
    # mostra código esperado
    if codigo_esperado:
        print("codigo esperado:")
        print(codigo_esperado)
        print()
    else:
        print("codigo esperado: (arquivo .txt não encontrado ou formato inválido)")
        if arquivo_txt.exists():
            print(f"arquivo existe: {arquivo_txt}")
        print()
    
    # compara códigos
    passou = False
    if codigo_gerado and codigo_esperado:
        if comparar_codigos(codigo_gerado, codigo_esperado):
            print("[ok] código gerado corresponde ao esperado")
            passou = True
        else:
            print("[erro] código gerado diverge do esperado")
            print()
            print("diferenças:")
            gerado_linhas = codigo_gerado.splitlines()
            esperado_linhas = codigo_esperado.splitlines()
            max_len = max(len(gerado_linhas), len(esperado_linhas))
            diferencas_encontradas = False
            for i in range(max_len):
                gerado_linha = gerado_linhas[i] if i < len(gerado_linhas) else ""
                esperado_linha = esperado_linhas[i] if i < len(esperado_linhas) else ""
                # normaliza para comparação (remove espaços à direita)
                gerado_linha_norm = gerado_linha.rstrip()
                esperado_linha_norm = esperado_linha.rstrip()
                if gerado_linha_norm != esperado_linha_norm:
                    diferencas_encontradas = True
                    print(f"  linha {i+1}:")
                    print(f"    gerado:   {gerado_linha}")
                    print(f"    esperado: {esperado_linha}")
            if not diferencas_encontradas and len(gerado_linhas) != len(esperado_linhas):
                print(f"  (número de linhas diferente: {len(gerado_linhas)} vs {len(esperado_linhas)})")
    elif codigo_gerado:
        print("[aviso] código esperado não encontrado para comparação")
    elif codigo_esperado:
        print("[erro] código gerado não encontrado")
    else:
        print("[erro] nenhum código encontrado")
    
    print()
    return passou

def executar_todos():    #executa todos os testes com comparação
    print("=" * 60)
    print("testes com comparação (código gerado vs esperado)")
    print("=" * 60)
    print()
    
    resultados = [] #lista de resultados
    for indice, (descricao, arquivo_teste) in enumerate(TESTES, start=1):
        try:
            # executa o teste e mostra resultado
            passou = mostrar_teste(indice, descricao, arquivo_teste)
            resultados.append((indice, descricao, passou))
        except Exception as e:
            print(f"[erro] erro ao processar teste {indice}: {e}")
            resultados.append((indice, descricao, False))
            print()
    
    # mostra resumo
    print("=" * 60)
    print("resumo dos testes")
    print("=" * 60)
    
    total = len(resultados)
    passaram = sum(1 for _, _, p in resultados if p)
    falharam = total - passaram
    
    print(f"testes executados: {total}")
    print(f"testes passaram: {passaram}")
    print(f"testes falharam: {falharam}")
    
    if falharam > 0:
        print()
        print("testes que falharam:")
        for indice, descricao, passou in resultados:
            if not passou:
                print(f"  - teste {indice}: {descricao}")
    
    print()
    return falharam == 0

if __name__ == "__main__":
    sucesso = executar_todos()
    if sucesso:
        print("[ok] todos os testes passaram!")
    else:
        print("[erro] alguns testes falharam")
    sys.exit(0 if sucesso else 1)

