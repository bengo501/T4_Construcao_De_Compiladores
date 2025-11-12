#teste 7: comandos break e continue
#adicionar comandos break e continue
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para comandos break e continue
    gc = GeradorCodigo()
    gc.inicio_programa()
    
<<<<<<< HEAD
    gc.declarar_variavel("i", "integer", 4) # declara var   
=======
    gc.declarar_variavel("i", "integer", 4) # declara var
>>>>>>> 29756358e66b0592e4a1afb9bee37e0498906945
    gc.ldc(0) # inicializa i
    gc.atribuir_variavel("i")
    rotulo_inicio, rotulo_fim = gc.inicio_while() # inicio do while
    gc.carregar_variavel("i") # i
    gc.ldc(10) # 10
    gc.les() # i < 10 (condicao)
    gc.jzer(rotulo_fim) # se falso, pula para fim
    gc.pos_incremento("i") # i++
    gc.drop() # descarta valor retornado
    gc.carregar_variavel("i") # i
    gc.ldc(5) # 5
    gc.eq() # i == 5 (condicao)
    rotulo_else1, rotulo_fim1 = gc.inicio_if() # inicio do if
    gc.jzer(rotulo_else1) # se falso, pula para else
    gc.continue_cmd() # continue
    gc.fim_if() # fim do if
    gc.carregar_variavel("i") # i
    gc.ldc(8) # 8
    gc.eq() # i == 8 (condicao)
    rotulo_else2, rotulo_fim2 = gc.inicio_if() # inicio do if
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


