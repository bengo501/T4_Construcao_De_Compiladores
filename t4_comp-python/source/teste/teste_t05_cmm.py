#teste t05.cmm: for com várias variações
#for (i=1;i<=5;i++)
#for (;i<=13;) { ... i++; }
#for (;;) { ... if (i<105) continue; if (i>110) break; ... }
#for aninhados
#for com +=
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4)
    gc.declarar_variavel("j", "integer", 4)
    
    # teste 1: for (i=1;i<=5;i++)
    gc.ldc(1)
    gc.atribuir_variavel("i")
    gc.inicio_for()
    gc.carregar_variavel("i")
    gc.ldc(5)
    gc.leq()  # i <= 5
    gc.teste_for()
    # corpo vazio (só write, que não implementamos)
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("i")
    gc.fim_for()
    
    # teste 2: for (;i<=13;) { ... i++; }
    gc.ldc(10)
    gc.atribuir_variavel("i")
    gc.inicio_for()
    gc.carregar_variavel("i")
    gc.ldc(13)
    gc.leq()  # i <= 13
    gc.teste_for()
    # corpo (write não implementado)
    gc.pos_incremento("i")
    gc.drop()
    gc.fim_for()
    
    # teste 3: for (;;) { ... if (i<105) continue; if (i>110) break; ... }
    gc.ldc(100)
    gc.atribuir_variavel("i")
    gc.inicio_for()
    # teste sempre verdadeiro (não há teste, então sempre entra)
    gc.ldc(1)  # true
    gc.teste_for()
    # i++
    gc.pos_incremento("i")
    gc.drop()
    # if (i<105) continue;
    gc.carregar_variavel("i")
    gc.ldc(105)
    gc.les()  # i < 105
    rotulo_else3, rotulo_fim3 = gc.inicio_if()
    gc.jzer(rotulo_else3)
    gc.continue_cmd()
    gc.fim_if()
    # if (i>110) break;
    gc.carregar_variavel("i")
    gc.ldc(110)
    gc.grt()  # i > 110
    rotulo_else4, rotulo_fim4 = gc.inicio_if()
    gc.jzer(rotulo_else4)
    gc.break_cmd()
    gc.fim_if()
    # corpo (write não implementado)
    gc.fim_for()
    
    # teste 4: for (i=1; i<=3;i++) for (j=1; j<=3;j++)
    gc.ldc(1)
    gc.atribuir_variavel("i")
    gc.inicio_for()
    gc.carregar_variavel("i")
    gc.ldc(3)
    gc.leq()  # i <= 3
    gc.teste_for()
    # for interno: for (j=1; j<=3;j++)
    gc.ldc(1)
    gc.atribuir_variavel("j")
    gc.inicio_for()
    gc.carregar_variavel("j")
    gc.ldc(3)
    gc.leq()  # j <= 3
    gc.teste_for()
    # corpo (write não implementado, calcular i*j)
    gc.carregar_variavel("i")
    gc.carregar_variavel("j")
    gc.mul()  # i * j
    gc.drop()  # descarta resultado
    gc.carregar_variavel("j")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("j")
    gc.fim_for()
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("i")
    gc.fim_for()
    
    # teste 5: for (i=1; i<=3;i+=1) for (j=1; j<=3;j+=1)
    gc.ldc(1)
    gc.atribuir_variavel("i")
    gc.inicio_for()
    gc.carregar_variavel("i")
    gc.ldc(3)
    gc.leq()  # i <= 3
    gc.teste_for()
    # for interno: for (j=1; j<=3;j+=1)
    gc.ldc(1)
    gc.atribuir_variavel("j")
    gc.inicio_for()
    gc.carregar_variavel("j")
    gc.ldc(3)
    gc.leq()  # j <= 3
    gc.teste_for()
    # corpo (write não implementado, calcular i*j)
    gc.carregar_variavel("i")
    gc.carregar_variavel("j")
    gc.mul()  # i * j
    gc.drop()  # descarta resultado
    # j += 1
    gc.carregar_variavel("j")
    gc.ldc(1)
    gc.atribuicao_adicao("j")
    gc.drop()
    gc.fim_for()
    # i += 1
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.atribuicao_adicao("i")
    gc.drop()
    gc.fim_for()
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t05.cmm: for com várias variações")
    print()
    print("programa fonte:")
    print("int i; int j;")
    print("for (i=1;i<=5;i++)")
    print("for (;i<=13;) { ... i++; }")
    print("for (;;) { ... if (i<105) continue; if (i>110) break; ... }")
    print("for (i=1; i<=3;i++) for (j=1; j<=3;j++)")
    print("for (i=1; i<=3;i+=1) for (j=1; j<=3;j+=1)")
    print()
    print("codigo gerado:")
    print(gerar_teste())

