"""
teste 11: array de structs (bonus completo)
permitir criar array de structs
"""

import sys
import os
# ajusta o path dependendo de onde está o arquivo
if os.path.exists('src/gerador_codigo.py'):
    sys.path.insert(0, 'src')
elif os.path.exists('../src/gerador_codigo.py'):
    sys.path.insert(0, '../src')
else:
    sys.path.insert(0, '.')
from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para array de structs"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara struct Ponto
    gc.declarar_struct("Ponto", [
        ("x", "integer", 4),
        ("y", "integer", 4)
    ])
    
    # declara array de structs: arr : array [5] of Ponto;
    gc.declarar_array_struct("arr", "Ponto", 5)
    
    gc.declarar_variavel("x", "integer", 4)
    
    # arr[0].x := 10
    gc.ldc(10)  # valor
    gc.ldc(0)  # índice 0
    gc.atribuir_campo_struct_array("arr", "x")
    
    # arr[0].y := 20
    gc.ldc(20)  # valor
    gc.ldc(0)  # índice 0
    gc.atribuir_campo_struct_array("arr", "y")
    
    # arr[1].x := 30
    gc.ldc(30)  # valor
    gc.ldc(1)  # índice 1
    gc.atribuir_campo_struct_array("arr", "x")
    
    # x := arr[0].x
    gc.ldc(0)  # índice 0
    gc.carregar_campo_struct_array("arr", "x")
    gc.atribuir_variavel("x")
    
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

