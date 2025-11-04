"""
teste 9: arrays de inteiros (bonus)
gerar código (declaração e expressões) para arrays de inteiros
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para arrays de inteiros"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara array de 5 inteiros
    gc.declarar_array("arr", "integer", 4, 5)
    
    gc.declarar_variavel("x", "integer", 4)
    
    # arr[0] := 10
    gc.ldc(0)  # índice
    gc.ldc(10)  # valor
    gc.atribuir_array_elemento("arr")
    
    # arr[2] := 20
    gc.ldc(2)  # índice
    gc.ldc(20)  # valor
    gc.atribuir_array_elemento("arr")
    
    # x := arr[2]
    gc.ldc(2)  # índice
    gc.carregar_array_elemento("arr")
    gc.atribuir_variavel("x")
    
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

