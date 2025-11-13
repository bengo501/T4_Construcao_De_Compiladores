#teste 11: array de structs (bonus completo)
#permitir criar array de structs
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para array de structs
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    #declara a struct Ponto com campos x e y
    gc.declarar_struct("Ponto", [
        ("x", "integer", 4),
        ("y", "integer", 4)
    ]) #declara a struct Ponto
    
    # declara array de structs: arr : array [5] of Ponto;
    gc.declarar_array_struct("arr", "Ponto", 5) #declara a array de structs arr do tipo Ponto com 5 elementos
    
    gc.declarar_variavel("x", "integer", 4) #declara a variável x do tipo integer
    
    # arr[0].x := 10
    gc.ldc(10)  # valor 10
    gc.ldc(0)  # indice 0
    gc.atribuir_campo_struct_array("arr", "x") #atribui o valor 10 ao campo x da struct arr
    
    # arr[0].y := 20
    gc.ldc(20)  # valor 20
    gc.ldc(0)  # indice 0
    gc.atribuir_campo_struct_array("arr", "y") #atribui o valor 20 ao campo y da struct arr
    
    # arr[1].x := 30
    gc.ldc(30)  # valor 30
    gc.ldc(1)  # indice 1
    gc.atribuir_campo_struct_array("arr", "x") #atribui o valor 30 ao campo x da struct arr
    
    # x := arr[0].x
    gc.ldc(0) #carrega o valor 0
    gc.carregar_campo_struct_array("arr", "x") #carrega o valor do campo x da struct arr
    gc.atribuir_variavel("x") #atribui o valor do campo x da struct arr à variável x
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 11: array de structs (bonus completo)")
    print("permitir criar array de structs")
    print()
    print("programa fonte:")
    print("struct Ponto {")
    print("    x : integer;")
    print("    y : integer;")
    print("};")
    print("arr : array [5] of Ponto;")
    print("arr[0].x := 10;")
    print("arr[0].y := 20;")
    print("arr[1].x := 30;")
    print("x : integer;")
    print("x := arr[0].x;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

