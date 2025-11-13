#teste 1 expressão de atribuição
#transformar comando de atribuição em expressão de atribuição
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para expressão de atribuição
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("x", "integer", 4)   # declara vars
    gc.declarar_variavel("y", "integer", 4)
    
    gc.ldc(5)    # x := 5 (expressao de atribuicao)
    gc.expressao_atribuicao("x")
    
    gc.expressao_atribuicao("y")# y := x := 5 (cadeia de atribuicoes)
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 1: expressao de atribuicao")
    print("transformar comando de atribuicao em expressao de atribuicao")
    print()
    print("programa fonte:")
    print("x : integer;")
    print("y : integer;")
    print("x := 5;")
    print("y := x := 5;  // cadeia de atribuicoes")
    print()
    print("codigo gerado:")
    print(gerar_teste())

