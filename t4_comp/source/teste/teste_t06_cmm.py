#teste t06.cmm: incremento/decremento em atribuições
#a = 1;
#b = a++;
#c = ++a + b++;
#--c;
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
    
    # b = a++;
    gc.pos_incremento("a")  # retorna valor original de a, incrementa a
    gc.atribuir_variavel("b")  # b = valor original de a
    
    # c = ++a + b++;
    # primeiro: ++a (incrementa a, retorna valor novo)
    gc.pre_incremento("a")
    # segundo: b++ (retorna valor original de b, incrementa b)
    gc.pos_incremento("b")
    # terceiro: soma os dois valores
    gc.add()
    # quarto: c = resultado
    gc.atribuir_variavel("c")
    
    # --c;
    gc.pre_decremento("c")
    gc.drop()  # descarta valor retornado
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t06.cmm: incremento/decremento em atribuições")
    print()
    print("programa fonte:")
    print("int a; int b; int c;")
    print("a = 1;")
    print("b = a++;")
    print("c = ++a + b++;")
    print("--c;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

