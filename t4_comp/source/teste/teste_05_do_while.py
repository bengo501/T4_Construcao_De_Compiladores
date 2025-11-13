#teste 5: comando do-while
#adicionar um comando do-while
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para comando do-while
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4) # declara var
    
    gc.ldc(0) # inicializa i
    gc.atribuir_variavel("i")
    
    rotulo_inicio, rotulo_fim = gc.inicio_do_while() # inicio do do-while
    
    gc.pos_incremento("i") # i++
    gc.drop()  # descarta valor retornado
    
    gc.carregar_variavel("i") # i
    gc.ldc(10) # 10
    gc.les()  # i < 10 (condicao)
    
    gc.fim_do_while()
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 5: comando do-while")
    print("adicionar um comando do-while")
    print()
    print("programa fonte:")
    print("i : integer;")
    print("i := 0;")
    print("do {")
    print("    i++;")
    print("} while (i < 10);")
    print()
    print("codigo gerado:")
    print(gerar_teste())


