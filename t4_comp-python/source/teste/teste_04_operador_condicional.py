#teste 4: operador condicional ?:
#adicionar o operador condicional "?:"

import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para operador condicional ?:
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("x", "integer", 4) # declara vars x, y e z
    gc.declarar_variavel("y", "integer", 4)
    gc.declarar_variavel("z", "integer", 4)
    
    gc.ldc(10) # inicializa x
    gc.atribuir_variavel("x")
    gc.ldc(5) # inicializa y    
    gc.atribuir_variavel("y")
    
    gc.carregar_variavel("x")# x > y ? x : y (expressao condicional)
    gc.carregar_variavel("y") # x > y (condicao) 
    gc.grt()  # x > y
    
    rotulo_else = gc.ts.novo_rotulo_cod()
    rotulo_fim = gc.ts.novo_rotulo_cod()
    
    gc.jzer(rotulo_else)  # se falso, pula para else
    gc.carregar_variavel("x")  # exp2
    gc.jmp(rotulo_fim)
    gc.emitir_rotulo(rotulo_else)
    gc.carregar_variavel("y")  # exp3
    gc.emitir_rotulo(rotulo_fim)
    
    gc.atribuir_variavel("z") # z := x > y ? x : y (expressao condicional)
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 4: operador condicional ?:")
    print("adicionar o operador condicional '?:'")
    print()
    print("programa fonte:")
    print("x : integer;")
    print("y : integer;")
    print("z : integer;")
    print("x := 10;")
    print("y := 5;")
    print("z := x > y ? x : y;  // z recebe o maior entre x e y")
    print()
    print("codigo gerado:")
    print(gerar_teste())


