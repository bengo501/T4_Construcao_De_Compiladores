"""
teste 4: operador condicional ?:
adicionar o operador condicional "?:"
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para operador condicional ?:"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara variáveis
    gc.declarar_variavel("x", "integer", 4)
    gc.declarar_variavel("y", "integer", 4)
    gc.declarar_variavel("z", "integer", 4)
    
    # inicializa
    gc.ldc(10)
    gc.atribuir_variavel("x")
    gc.ldc(5)
    gc.atribuir_variavel("y")
    
    # z := x > y ? x : y
    gc.carregar_variavel("x")
    gc.carregar_variavel("y")
    gc.grt()  # x > y
    
    rotulo_else = gc.ts.novo_rotulo_cod()
    rotulo_fim = gc.ts.novo_rotulo_cod()
    
    gc.jzer(rotulo_else)  # se falso, pula para else
    gc.carregar_variavel("x")  # exp2
    gc.jmp(rotulo_fim)
    gc.emitir_rotulo(rotulo_else)
    gc.carregar_variavel("y")  # exp3
    gc.emitir_rotulo(rotulo_fim)
    
    gc.atribuir_variavel("z")
    
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

