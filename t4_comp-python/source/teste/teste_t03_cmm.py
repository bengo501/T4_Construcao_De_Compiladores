#teste t03.cmm: incremento/decremento complexo
#a = a++ + ++a;
#a += a++ + ++a;
#c = --b + b--;
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("a", "integer", 4)
    gc.declarar_variavel("b", "integer", 4)
    gc.declarar_variavel("c", "integer", 4)
    
    # a = 1;
    gc.ldc(1)
    gc.atribuir_variavel("a")
    
    # a = a++ + ++a;
    # primeiro: a++ (retorna valor original, depois incrementa)
    gc.pos_incremento("a")
    # segundo: ++a (incrementa, retorna valor novo)
    gc.pre_incremento("a")
    # terceiro: soma os dois valores
    gc.add()
    # quarto: a = resultado
    gc.atribuir_variavel("a")
    
    # a = 1;
    gc.ldc(1)
    gc.atribuir_variavel("a")
    
    # a += a++ + ++a;
    # primeiro: a++ (retorna valor original)
    gc.pos_incremento("a")
    # segundo: ++a (incrementa, retorna valor novo)
    gc.pre_incremento("a")
    # terceiro: soma os dois valores
    gc.add()
    # quarto: a += resultado (a = a + resultado)
    gc.carregar_variavel("a")
    gc.add()  # a + (a++ + ++a)
    gc.dup()
    gc.atribuir_variavel("a")
    gc.drop()
    
    # b = 10;
    gc.ldc(10)
    gc.atribuir_variavel("b")
    
    # c = --b + b--;
    # primeiro: --b (decrementa, retorna valor novo)
    gc.pre_decremento("b")
    # segundo: b-- (retorna valor original, depois decrementa)
    gc.pos_decremento("b")
    # terceiro: soma os dois valores
    gc.add()
    # quarto: c = resultado
    gc.atribuir_variavel("c")
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t03.cmm: incremento/decremento complexo")
    print()
    print("programa fonte:")
    print("int a; int b; int c;")
    print("a = 1;")
    print("a = a++ + ++a;")
    print("a = 1;")
    print("a += a++ + ++a;")
    print("b = 10;")
    print("c = --b + b--;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

