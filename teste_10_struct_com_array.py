"""
teste 10: struct com array (bonus)
permitir criar structs que tenham um array como campo da struct
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para struct com array"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara struct que contém array
    gc.declarar_struct("Pessoa", [
        ("idade", "integer", 4),
        ("scores", "array[3]", 12)  # array de 3 inteiros
    ])
    
    # declara variável do tipo Pessoa
    gc.declarar_variavel_struct("p", "Pessoa")
    
    # p.idade := 25
    gc.ldc(25)
    gc.carregar_variavel("p")
    gc.ldc(0)  # offset do campo idade
    gc.add()
    gc.emitir("STI")
    
    # p.scores[0] := 100
    gc.ldc(100)
    gc.carregar_variavel("p")
    gc.ldc(4)  # offset base do array scores
    gc.add()
    gc.ldc(0)  # índice 0
    gc.ldc(4)  # tamanho do elemento
    gc.mul()
    gc.add()
    gc.emitir("STI")
    
    # p.scores[1] := 90
    gc.ldc(90)
    gc.carregar_variavel("p")
    gc.ldc(4)  # offset base
    gc.add()
    gc.ldc(1)  # índice 1
    gc.ldc(4)
    gc.mul()
    gc.add()
    gc.emitir("STI")
    
    # p.scores[2] := 95
    gc.ldc(95)
    gc.carregar_variavel("p")
    gc.ldc(4)  # offset base
    gc.add()
    gc.ldc(2)  # índice 2
    gc.ldc(4)
    gc.mul()
    gc.add()
    gc.emitir("STI")
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 10: struct com array (bonus)")
    print("permitir criar structs que tenham um array como campo da struct")
    print()
    print("programa fonte:")
    print("struct Pessoa {")
    print("    idade : integer;")
    print("    scores : array [3] of integer;")
    print("};")
    print("p : Pessoa;")
    print("p.idade := 25;")
    print("p.scores[0] := 100;")
    print("p.scores[1] := 90;")
    print("p.scores[2] := 95;")
    print()
    print("codigo gerado:")
    print(gerar_teste())

