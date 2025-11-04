"""
teste 2: incremento e decremento
expressões de pós e pré incremento/decremento
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para incremento e decremento"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara variáveis
    gc.declarar_variavel("a", "integer", 4)
    gc.declarar_variavel("b", "integer", 4)
    
    # inicializa
    gc.ldc(0)
    gc.atribuir_variavel("a")
    gc.ldc(0)
    gc.atribuir_variavel("b")
    
    # pré-incremento: ++a
    gc.pre_incremento("a")
    gc.drop()  # descarta valor retornado
    
    # pós-incremento: b++
    gc.pos_incremento("b")
    gc.drop()  # descarta valor retornado
    
    # pré-decremento: --a
    gc.pre_decremento("a")
    gc.drop()
    
    # pós-decremento: b--
    gc.pos_decremento("b")
    gc.drop()
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 2: incremento e decremento")
    print("expressoes de pos e pre incremento/decremento")
    print()
    print("programa fonte:")
    print("a : integer;")
    print("b : integer;")
    print("a := 0;")
    print("b := 0;")
    print("++a;      // pre-incremento")
    print("b++;      // pos-incremento")
    print("--a;      // pre-decremento")
    print("b--;      // pos-decremento")
    print()
    print("codigo gerado:")
    print(gerar_teste())

