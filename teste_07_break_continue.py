"""
teste 7: comandos break e continue
adicionar comandos break e continue
"""

from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para comandos break e continue"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara variável
    gc.declarar_variavel("i", "integer", 4)
    
    # inicializa i
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    # while (i < 10)
    rotulo_inicio, rotulo_fim = gc.inicio_while()
    
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.jzer(rotulo_fim)
    
    gc.pos_incremento("i")
    gc.drop()
    
    # if (i == 5) continue
    gc.carregar_variavel("i")
    gc.ldc(5)
    gc.eq()
    rotulo_else1, rotulo_fim1 = gc.inicio_if()
    gc.jzer(rotulo_else1)
    gc.continue_cmd()
    gc.fim_if()
    
    # if (i == 8) break
    gc.carregar_variavel("i")
    gc.ldc(8)
    gc.eq()
    rotulo_else2, rotulo_fim2 = gc.inicio_if()
    gc.jzer(rotulo_else2)
    gc.break_cmd()
    gc.fim_if()
    
    gc.jmp(rotulo_inicio)
    gc.emitir_rotulo(rotulo_fim)
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 7: comandos break e continue")
    print("adicionar comandos break e continue")
    print()
    print("programa fonte:")
    print("i : integer;")
    print("i := 0;")
    print("while (i < 10) {")
    print("    i++;")
    print("    if (i == 5) continue;")
    print("    if (i == 8) break;")
    print("}")
    print()
    print("codigo gerado:")
    print(gerar_teste())

