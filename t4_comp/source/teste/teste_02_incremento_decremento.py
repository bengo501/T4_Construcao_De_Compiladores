#teste 2 incremento e decremento
#expressões de pós e pré incremento/decremento

import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera código de teste para incremento e decremento
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("a", "integer", 4)  # declara variaveis
    gc.declarar_variavel("b", "integer", 4)
    
    gc.ldc(0)    # inicializa variaveis
    gc.atribuir_variavel("a")
    gc.ldc(0)
    gc.atribuir_variavel("b")
    
    gc.pre_incremento("a")# pre-incremento: ++a
    gc.drop()  # descarta valor retornado
    
    gc.pos_incremento("b")  # pos-incremento: b++
    gc.drop()  # descarta valor retornado
    
    # pre-decremento: --a
    gc.pre_decremento("a")
    gc.drop()
    
    # pos-decremento: b--
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


