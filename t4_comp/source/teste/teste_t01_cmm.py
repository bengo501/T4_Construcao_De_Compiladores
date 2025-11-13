#teste t01.cmm: expressão de atribuição complexa
#a = b = c = 5;
#a = (b = (c = 7) * 3) + 2;
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("a", "integer", 4)
    gc.declarar_variavel("b", "integer", 4)
    gc.declarar_variavel("c", "integer", 4)
    
    # a = b = c = 5;
    gc.ldc(5)
    gc.expressao_atribuicao("c")
    gc.expressao_atribuicao("b")
    gc.expressao_atribuicao("a")
    gc.drop()  # descarta valor final
    
    # a = (b = (c = 7) * 3) + 2;
    # primeiro: c = 7
    gc.ldc(7)
    gc.expressao_atribuicao("c")
    # segundo: c * 3
    gc.ldc(3)
    gc.mul()
    # terceiro: b = (c * 3)
    gc.expressao_atribuicao("b")
    # quarto: b + 2
    gc.ldc(2)
    gc.add()
    # quinto: a = (b + 2)
    gc.expressao_atribuicao("a")
    gc.drop()  # descarta valor final
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t01.cmm: expressão de atribuição complexa")
    print()
    print("programa fonte:")
    print("int a; int b; int c;")
    print("a = b = c = 5;")
    print("a = (b = (c = 7) * 3) + 2;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

