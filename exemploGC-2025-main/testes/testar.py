import os
import glob
import os.path

# Define o CLASSPATH para o diretório atual (para encontrar o Parser.class)
JAVA_COMMAND = "java -cp . Parser"

# Limpa executaveis e assemblies antigos para evitar confusão
def cleanup_files():
    print("--- Limpando arquivos antigos ---")
    os.system("rm -f *.s *_exec")
    os.system("rm -f testes/*.s testes/*_cmm_exec testes/*_c_exec")
    os.system("rm -f testes/c/*.s testes/c/*_cmm_exec testes/c/*_c_exec")

def rodar_teste(base_path, comparar_com_c=False):
    """Compila e executa um unico teste .cmm"""
    
    cmm_file = f"{base_path}.cmm"
    s_file = f"{base_path}.s"
    cmm_exec = f"{base_path}_cmm_exec"
    
    print("-" * 40)
    print(f"TESTANDO: {cmm_file}")

    # Certifica que o diretório de saída (ex: testes/) existe
    os.makedirs(os.path.dirname(base_path) or ".", exist_ok=True)
    
    # 1. Compilar .cmm -> .s
    if os.system(f"{JAVA_COMMAND} {cmm_file} > {s_file}") != 0:
        print(f"  [FALHA NO PARSER] Erro ao compilar {cmm_file}")
        return

    # 2. Montar .s -> exec
    if os.system(f"gcc -m32 -nostartfiles -no-pie -o {cmm_exec} {s_file}") != 0:
        print(f"  [FALHA NO GCC] Erro ao montar {s_file}")
        return

    # 3. Rodar seu executavel
    print(f"\n  SAIDA (Seu Compilador):")
    os.system(f"./{cmm_exec}")

    # 4. Compilar e rodar o gabarito .c (se existir)
    if comparar_com_c:
        # Caminho do .c é sempre {base_dir}/c/{base_name}.c
        base_name = os.path.basename(base_path)
        c_file = f"testes/c/{base_name}.c"
        c_exec = f"{base_path}_c_exec"
        
        if os.system(f"gcc -m32 -o {c_exec} {c_file}") != 0:
            print(f"  [AVISO] Nao foi possivel compilar o gabarito {c_file}")
        else:
            print(f"  SAIDA (Gabarito .c):")
            os.system(f"./{c_exec}")
    
    print("-" * 40)


# Mapeamento dos arquivos
testes_da_raiz = [
    f.replace(".cmm", "") 
    for f in glob.glob("teste_*.cmm") 
    if os.path.dirname(f) == '' and "bonus" not in f
]

testes_com_gabarito = [
    # "testes/t01", 
    # "testes/t02", 
    # "testes/t03", 
    # "testes/t04", 
    "testes/t05", 
    # "testes/t06", 
    "testes/t07",
    "teste_debug"
    # "testes/t08",
]


# --- EXECUÇÃO ---
cleanup_files()

# print("=== INICIANDO TESTES DA RAIZ COMENTADOS por enquanto ===")
# for base in testes_da_raiz:
#     rodar_teste(base, comparar_com_c=False)

print("\n=== INICIANDO TESTES DO PROFESSOR (com gabarito) ===")
for base in testes_com_gabarito:
    rodar_teste(base, comparar_com_c=True)

print("\n=== TESTES CONCLUIDOS ===")