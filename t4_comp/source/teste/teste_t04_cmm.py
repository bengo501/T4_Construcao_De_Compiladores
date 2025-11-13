#teste t04.cmm: break e continue aninhados
#while (true) { ... if (i>3) break; ... while (j<=6) { j++; if (j < 2 || j > 4) continue; ... } }
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4)
    gc.declarar_variavel("j", "integer", 4)
    
    # i = 0;
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    # while (true) {
    rotulo_inicio_while, rotulo_fim_while = gc.inicio_while()
    # condição sempre verdadeira (não precisa testar, sempre entra)
    
    # if (i>3) break;
    gc.carregar_variavel("i")
    gc.ldc(3)
    gc.grt()  # i > 3
    rotulo_else1, rotulo_fim1 = gc.inicio_if()
    gc.jzer(rotulo_else1)
    gc.break_cmd()  # break
    gc.fim_if()
    
    # j = 0;
    gc.ldc(0)
    gc.atribuir_variavel("j")
    
    # while (j<=6) {
    rotulo_inicio_while2, rotulo_fim_while2 = gc.inicio_while()
    gc.carregar_variavel("j")
    gc.ldc(6)
    gc.leq()  # j <= 6
    gc.jzer(rotulo_fim_while2)
    
    # j++;
    gc.pos_incremento("j")
    gc.drop()
    
    # if (j < 2 || j > 4) continue;
    # j < 2
    gc.carregar_variavel("j")
    gc.ldc(2)
    gc.les()  # j < 2
    # j > 4
    gc.carregar_variavel("j")
    gc.ldc(4)
    gc.grt()  # j > 4
    # j < 2 || j > 4 (ou lógico)
    gc.operador_ou_logico()
    # agora temos na pilha: 1 se (j < 2 || j > 4), 0 caso contrário
    rotulo_else2, rotulo_fim2 = gc.inicio_if()
    gc.jzer(rotulo_else2)
    gc.continue_cmd()  # continue
    gc.fim_if()
    
    gc.fim_while()  # fim do while interno
    
    # i++;
    gc.pos_incremento("i")
    gc.drop()
    
    gc.jmp(rotulo_inicio_while)  # volta para início do while externo
    gc.emitir_rotulo(rotulo_fim_while)  # fim do while externo
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t04.cmm: break e continue aninhados")
    print()
    print("programa fonte:")
    print("int i; int j;")
    print("i = 0;")
    print("while (true) {")
    print("    if (i>3) break;")
    print("    j = 0;")
    print("    while (j<=6) {")
    print("        j++;")
    print("        if (j < 2 || j > 4) continue;")
    print("    }")
    print("    i++;")
    print("}")
    print()
    print("codigo gerado:")
    print(gerar_teste())

