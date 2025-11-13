#teste t02.cmm: operador += encadeado
#a = b = c = 1;
#a += b += c += 5;
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("a", "integer", 4)
    gc.declarar_variavel("b", "integer", 4)
    gc.declarar_variavel("c", "integer", 4)
    
    # a = b = c = 1;
    gc.ldc(1)
    gc.expressao_atribuicao("c")
    gc.expressao_atribuicao("b")
    gc.expressao_atribuicao("a")
    gc.drop()  # descarta valor final
    
    # a += b += c += 5;
    # primeiro: c += 5 (c já está na pilha como valor atual, mas precisamos carregar)
    # na verdade, para encadeamento, precisamos fazer da direita para esquerda
    # c += 5: carrega c, empilha 5, soma, atribui a c (mantém valor)
    gc.carregar_variavel("c")
    gc.ldc(5)
    gc.add()
    gc.dup()  # duplica para retornar valor
    gc.atribuir_variavel("c")  # c = c + 5
    
    # b += c (valor de c já está na pilha)
    gc.carregar_variavel("b")
    gc.add()  # b + c
    gc.dup()  # duplica para retornar valor
    gc.atribuir_variavel("b")  # b = b + c
    
    # a += b (valor de b já está na pilha)
    gc.carregar_variavel("a")
    gc.add()  # a + b
    gc.dup()  # duplica para retornar valor
    gc.atribuir_variavel("a")  # a = a + b
    gc.drop()  # descarta valor final
    
    # a += 1;
    gc.carregar_variavel("a")
    gc.ldc(1)
    gc.atribuicao_adicao("a")
    gc.drop()
    
    # b += 2;
    gc.carregar_variavel("b")
    gc.ldc(2)
    gc.atribuicao_adicao("b")
    gc.drop()
    
    # c += 3;
    gc.carregar_variavel("c")
    gc.ldc(3)
    gc.atribuicao_adicao("c")
    gc.drop()
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t02.cmm: operador += encadeado")
    print()
    print("programa fonte:")
    print("int a; int b; int c;")
    print("a = b = c = 1;")
    print("a += b += c += 5;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

