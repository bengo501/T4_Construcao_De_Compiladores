"""
teste 1: expressão de atribuição
transformar comando de atribuição em expressão de atribuição
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para expressão de atribuição"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara variáveis
    gc.declarar_variavel("x", "integer", 4)
    gc.declarar_variavel("y", "integer", 4)
    
    # x := 5 (expressão de atribuição)
    gc.ldc(5)
    gc.expressao_atribuicao("x")
    
    # y := x := 5 (cadeia de atribuições)
    gc.expressao_atribuicao("y")
    
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

