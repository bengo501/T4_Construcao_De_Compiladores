#teste 6: comando for
#adicionar o comando for (as 3 expressões do for podem ser vazias)
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para comando for
    gc = GeradorCodigo() 
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4) # declara var
    gc.ldc(0) # inicializa i
    gc.atribuir_variavel("i")
    gc.inicio_for() # inicio do for 
    gc.carregar_variavel("i") # i
    gc.ldc(10) # 10
    gc.les()  # i < 10 (condicao)
    gc.teste_for() # teste do for (corpo do loop)
<<<<<<< HEAD
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("i")
=======
    # incremento: i++
    gc.carregar_variavel("i") # i
    gc.ldc(1) # 1
    gc.add() # i + 1
    gc.atribuir_variavel("i") # i := i + 1
>>>>>>> 29756358e66b0592e4a1afb9bee37e0498906945
    gc.fim_for() # fim do for
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 6: comando for")
    print("adicionar o comando for (as 3 expressoes do for podem ser vazias)")
    print()
    print("programa fonte:")
    print("i : integer;")
    print("for (i := 0; i < 10; i++) {")
    print("    // corpo vazio")
    print("}")
    print()
    print("codigo gerado:")
    print(gerar_teste())


