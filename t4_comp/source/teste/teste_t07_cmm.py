#teste t07.cmm: operador condicional ?: aninhado
#a = b = c = 10;
#++b;
#c--;
#me = a<=b && a<=c ? a : b <= c ? b : c;
#ma = a>=b && a>=c ? a : b >= c ? b : c;
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("a", "integer", 4)
    gc.declarar_variavel("b", "integer", 4)
    gc.declarar_variavel("c", "integer", 4)
    gc.declarar_variavel("ma", "integer", 4)
    gc.declarar_variavel("me", "integer", 4)
    
    # a = b = c = 10;
    gc.ldc(10)
    gc.expressao_atribuicao("c")
    gc.expressao_atribuicao("b")
    gc.expressao_atribuicao("a")
    gc.drop()
    
    # ++b;
    gc.pre_incremento("b")
    gc.drop()
    
    # c--;
    gc.pos_decremento("c")
    gc.drop()
    
    # me = a<=b && a<=c ? a : b <= c ? b : c;
    # primeiro: a<=b
    gc.carregar_variavel("a")
    gc.carregar_variavel("b")
    gc.leq()  # a <= b
    # segundo: a<=c
    gc.carregar_variavel("a")
    gc.carregar_variavel("c")
    gc.leq()  # a <= c
    # terceiro: a<=b && a<=c (e lógico)
    gc.operador_e_logico()
    # agora temos na pilha: 1 se (a<=b && a<=c), 0 caso contrário
    
    # se verdadeiro: me = a
    # se falso: me = (b <= c ? b : c)
    rotulo_else1, rotulo_fim1 = gc.inicio_if()
    gc.jzer(rotulo_else1)
    # verdadeiro: me = a
    gc.carregar_variavel("a")
    gc.jmp(rotulo_fim1)
    gc.emitir_rotulo(rotulo_else1)
    # falso: me = (b <= c ? b : c)
    gc.carregar_variavel("b")
    gc.carregar_variavel("c")
    gc.leq()  # b <= c
    rotulo_else2, rotulo_fim2 = gc.inicio_if()
    gc.jzer(rotulo_else2)
    gc.carregar_variavel("b")
    gc.jmp(rotulo_fim2)
    gc.emitir_rotulo(rotulo_else2)
    gc.carregar_variavel("c")
    gc.emitir_rotulo(rotulo_fim2)
    gc.emitir_rotulo(rotulo_fim1)
    gc.atribuir_variavel("me")
    
    # ma = a>=b && a>=c ? a : b >= c ? b : c;
    # primeiro: a>=b
    gc.carregar_variavel("a")
    gc.carregar_variavel("b")
    gc.geq()  # a >= b
    # segundo: a>=c
    gc.carregar_variavel("a")
    gc.carregar_variavel("c")
    gc.geq()  # a >= c
    # terceiro: a>=b && a>=c (e lógico)
    gc.operador_e_logico()
    # agora temos na pilha: 1 se (a>=b && a>=c), 0 caso contrário
    
    # se verdadeiro: ma = a
    # se falso: ma = (b >= c ? b : c)
    rotulo_else3, rotulo_fim3 = gc.inicio_if()
    gc.jzer(rotulo_else3)
    gc.carregar_variavel("a")
    gc.jmp(rotulo_fim3)
    gc.emitir_rotulo(rotulo_else3)
    gc.carregar_variavel("b")
    gc.carregar_variavel("c")
    gc.geq()  # b >= c
    rotulo_else4, rotulo_fim4 = gc.inicio_if()
    gc.jzer(rotulo_else4)
    gc.carregar_variavel("b")
    gc.jmp(rotulo_fim4)
    gc.emitir_rotulo(rotulo_else4)
    gc.carregar_variavel("c")
    gc.emitir_rotulo(rotulo_fim4)
    gc.emitir_rotulo(rotulo_fim3)
    gc.atribuir_variavel("ma")
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t07.cmm: operador condicional ?: aninhado")
    print()
    print("programa fonte:")
    print("int a; int b; int c; int ma; int me;")
    print("a = b = c = 10;")
    print("++b;")
    print("c--;")
    print("me = a<=b && a<=c ? a : b <= c ? b : c;")
    print("ma = a>=b && a>=c ? a : b >= c ? b : c;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

