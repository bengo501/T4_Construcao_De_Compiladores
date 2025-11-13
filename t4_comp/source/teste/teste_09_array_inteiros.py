#teste 9: arrays de inteiros (bonus)
#gerar código (declaração e expressões) para arrays de inteiros
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para arrays de inteiros
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_array("arr", "integer", 4, 5) #declara a array de 5 inteiros
    
    gc.declarar_variavel("x", "integer", 4) #declara variavel x do tipo integer
    
    # arr[0] := 10
    gc.ldc(0) #carrega o valor 0 (indice)
    gc.ldc(10) #carrega o valor 10 (valor)
    gc.atribuir_array_elemento("arr") #atribui o valor 10 ao array arr
    
    # arr[2] := 20
    gc.ldc(2) #carrega o valor 2 (indice)
    gc.ldc(20) #carrega o valor 20 (valor)
    gc.atribuir_array_elemento("arr") #atribui o valor 20 ao array arr
    
    # x := arr[2]
    gc.ldc(2) #carrega o valor 2 (indice)
    gc.carregar_array_elemento("arr") #carrega o elemento do array
    gc.atribuir_variavel("x") #atribui o valor a x
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 9: arrays de inteiros (bonus)")
    print("gerar codigo (declaracao e expressoes) para arrays de inteiros")
    print()
    print("programa fonte:")
    print("arr : array [5] of integer;")
    print("arr[0] := 10;")
    print("arr[2] := 20;")
    print("x : integer;")
    print("x := arr[2];")
    print()
    print("codigo gerado:")
    print(gerar_teste())


