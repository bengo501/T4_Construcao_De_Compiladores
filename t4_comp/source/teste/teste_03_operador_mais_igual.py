#teste 3: operador +=
#adicionar o operador "+="
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para operador +=
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("x", "integer", 4) # declara var
    
    gc.ldc(10) # inicializa x
    gc.atribuir_variavel("x")
    
    gc.ldc(5) # x += 5
    gc.atribuicao_adicao("x")
    gc.drop()  # descarta valor retornado
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 3: operador +=")
    print("adicionar o operador '+='")
    print()
    print("programa fonte:")
    print("x : integer;")
    print("x := 10;")
    print("x += 5;   // x = x + 5")
    print()
    print("codigo gerado:")
    print(gerar_teste())


