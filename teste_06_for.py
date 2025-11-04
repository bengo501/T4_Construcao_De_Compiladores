"""
teste 6: comando for
adicionar o comando for (as 3 expressões do for podem ser vazias)
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para comando for"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara variável
    gc.declarar_variavel("i", "integer", 4)
    
    # for (i := 0; i < 10; i++)
    # expressão inicial: i := 0
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    rotulo_teste, rotulo_incremento, rotulo_fim = gc.inicio_for()
    
    # teste: i < 10
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.teste_for()
    
    # corpo do loop (vazio neste exemplo)
    
    # incremento: i++
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("i")
    
    gc.fim_for()
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 6: comando for")
    print("adicionar o comando for (as 3 expressoes do for podem ser vazias)")
    print()
    print("programa fonte:")
    print("i : integer;")
    print("for (i := 0; i < 10; i++) {")
    print("    // corpo vazio")
    print("}")
    print()
    print("codigo gerado:")
    print(gerar_teste())

