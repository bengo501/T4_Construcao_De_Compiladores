#script de teste completo - verifica todas as funcionalidades
import _import_helper # import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo #importa o módulo gerador_codigo
#---------------------------------------------------------------------------------------------------------
def testar_expressao_atribuicao():    #testa expressão de atribuição
    print("testando: expressão de atribuição")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    gc.declarar_variavel("x", "integer", 4) #declara a variável x
    gc.declarar_variavel("y", "integer", 4) #declara a variável y
    
    gc.ldc(5)
    gc.expressao_atribuicao("x") #expressão de atribuição para a variável x
    gc.expressao_atribuicao("y") #expressão de atribuição para a variável y
    
    gc.fim_programa() #fim do programa
    codigo = gc.get_codigo() #obtém o código gerado
    
    # verifica se contém instruções esperadas
    assert "DUP" in codigo, "deve conter DUP para expressão de atribuição" #verifica se o código contém a instrução DUP
    assert "STA _x" in codigo, "deve atribuir a x" #verifica se o código contém a instrução STA _x
    assert "STA _y" in codigo, "deve atribuir a y" #verifica se o código contém a instrução STA _y
    print("  [ok] expressao de atribuicao") #exibe a mensagem de sucesso
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_incremento():    #testa incremento e decremento
    print("testando: incremento e decremento") #exibe a mensagem de teste
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa() #início do programa
    gc.declarar_variavel("a", "integer", 4) #declara a variável a
    
    gc.pre_incremento("a") #pré-incremento para a variável a
    gc.pos_incremento("a") #pós-incremento para a variável a
    gc.pre_decremento("a") #pré-decremento para a variável a
    gc.pos_decremento("a") #pós-decremento para a variável a
    
    gc.fim_programa() #fim do programa
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "LDA _a" in codigo, "deve carregar variável a" #verifica se o código contém a instrução LDA _a
    assert "ADD" in codigo, "deve usar ADD para incremento" #verifica se o código contém a instrução ADD
    assert "SUB" in codigo, "deve usar SUB para decremento" #verifica se o código contém a instrução SUB
    print("  [ok] incremento/decremento") #exibe a mensagem de sucesso
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_operador_mais_igual():    #testa operador +=
    print("testando: operador +=") #exibe a mensagem de teste
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    gc.declarar_variavel("x", "integer", 4) #declara a variável x
    
    gc.ldc(10) #carrega o valor 10
    gc.atribuir_variavel("x") #atribuição para a variável x
    gc.ldc(5) #carrega o valor 5
    gc.atribuicao_adicao("x") #atribuição aditiva para a variável x
    
    gc.fim_programa() #fim do programa
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "LDA _x" in codigo, "deve carregar x" #verifica se o código contém a instrução LDA _x
    assert "ADD" in codigo, "deve usar ADD" #verifica se o código contém a instrução ADD
    assert "STA _x" in codigo, "deve atribuir a x" #verifica se o código contém a instrução STA _x
    print("  [ok] operador +=") #exibe a mensagem de sucesso
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_operador_condicional():#testa operador condicional ?:
    print("testando: operador condicional ?:")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo  
    gc.inicio_programa() #início do programa
    gc.declarar_variavel("x", "integer", 4) #declara a variável x
    gc.declarar_variavel("y", "integer", 4) #declara a variável y
    gc.declarar_variavel("z", "integer", 4) #declara a variável z
    
    gc.carregar_variavel("x") #carrega a variável x
    gc.carregar_variavel("y") #carrega a variável y
    gc.grt() #comparação maior
    
    rotulo_else = gc.ts.novo_rotulo_cod() #cria um novo rótulo de código
    rotulo_fim = gc.ts.novo_rotulo_cod() #cria um novo rótulo de código
    
    gc.jzer(rotulo_else) #pula para o rótulo de código else
    gc.carregar_variavel("x") #carrega a variável x
    gc.jmp(rotulo_fim) #pula para o rótulo de código fim
    gc.emitir_rotulo(rotulo_else) #emite o rótulo de código else    
    gc.carregar_variavel("y") #carrega a variável y
    gc.emitir_rotulo(rotulo_fim) #emite o rótulo de código fim
    
    gc.fim_programa() #fim do programa
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "GRT" in codigo, "deve usar GRT para comparação" #verifica se o código contém a instrução GRT
    assert "JZER" in codigo, "deve usar JZER para condicional" #verifica se o código contém a instrução JZER
    assert "JMP" in codigo, "deve usar JMP" #verifica se o código contém a instrução JMP
    print("  [ok] operador condicional ?:")
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_do_while():  #testa comando do-while
    print("testando: comando do-while")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    gc.declarar_variavel("i", "integer", 4) #declara a variável i
    
    rotulo_inicio, rotulo_fim = gc.inicio_do_while() #início do do-while
    gc.pos_incremento("i")
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.fim_do_while()
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "JNZ" in codigo, "deve usar JNZ para do-while"
    print("  [ok] do-while")
    return True
#---------------------------------------------------------------------------------------------------------
def testar_for():    #testa comando for
    print("testando: comando for")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa() #início do programa
    gc.declarar_variavel("i", "integer", 4) #declara a variável i
    
    gc.ldc(0) #carrega o valor 0
    gc.atribuir_variavel("i") #atribuição para a variável i
    
    rotulo_teste, rotulo_incremento, rotulo_fim = gc.inicio_for() #início do for
    gc.carregar_variavel("i") #carrega a variável i
    gc.ldc(10) #carrega o valor 10
    gc.les() #comparação menor ou igual
    gc.teste_for() #teste do for    
    
    gc.carregar_variavel("i") #carrega a variável i
    gc.ldc(1) #carrega o valor 1
    gc.add() #adição
    gc.atribuir_variavel("i") #atribuição para a variável i
    gc.fim_for() #fim do for
    
    gc.fim_programa()
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "JMP" in codigo, "deve usar JMP" #verifica se o código contém a instrução JMP
    assert "JZER" in codigo, "deve usar JZER para teste" #verifica se o código contém a instrução JZER
    print("  [ok] for")
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_break_continue():    #testa break e continue
    print("testando: break e continue")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    gc.declarar_variavel("i", "integer", 4) #declara a variável i
    
    rotulo_inicio, rotulo_fim = gc.inicio_while() #início do while
    gc.break_cmd() #comando break
    gc.continue_cmd() #comando continue
    gc.fim_while() #fim do while
    
    gc.fim_programa()
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "JMP" in codigo, "deve usar JMP para break/continue" #verifica se o código contém a instrução JMP
    print("  [ok] break e continue") #exibe a mensagem de sucesso
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_struct():    #testa variáveis do tipo struct
    print("testando: variáveis do tipo struct") #exibe a mensagem de teste
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    
    gc.declarar_struct("Ponto", [
        ("x", "integer", 4),
        ("y", "integer", 4)
    ]) #declara a struct Ponto
    
    gc.declarar_variavel_struct("p", "Ponto") #declara a variável p
    
    gc.ldc(10) #carrega o valor 10
    gc.carregar_variavel("p") #carrega a variável p
    gc.ldc(0) #carrega o valor 0
    gc.add() #adição
    gc.emitir("STI") #emite a instrução STI
    
    gc.fim_programa()
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "_p DS 8" in codigo, "deve reservar 8 bytes para struct" #verifica se o código contém a instrução _p DS 8
    assert "STI" in codigo, "deve usar STI para armazenar em struct" #verifica se o código contém a instrução STI
    print("  [ok] struct")
    return True
#---------------------------------------------------------------------------------------------------------
def testar_array():    #testa arrays de inteiros
    print("testando: arrays de inteiros")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    
    gc.declarar_array("arr", "integer", 4, 5)
    
    gc.ldc(0) #carrega o valor 0
    gc.ldc(10) #carrega o valor 10
    gc.atribuir_array_elemento("arr") #atribuição para o elemento do array
    
    gc.ldc(2) #carrega o valor 2
    gc.carregar_array_elemento("arr") #carrega o elemento do array
    
    gc.fim_programa() 
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "_arr DS 20" in codigo, "deve reservar 20 bytes para array" #verifica se o código contém a instrução _arr DS 20
    assert "STI" in codigo, "deve usar STI para array" #verifica se o código contém a instrução STI
    assert "LDI" in codigo, "deve usar LDI para carregar de array" #verifica se o código contém a instrução LDI
    print("  [ok] arrays de inteiros") #exibe a mensagem de sucesso
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def testar_struct_com_array():    #testa struct com array
    print("testando: struct com array") 
    print("testando: struct com array")
    gc = GeradorCodigo() #instancia o objeto GeradorCodigo
    gc.inicio_programa()
    
    gc.declarar_struct("Pessoa", [
        ("idade", "integer", 4),
        ("scores", "array[3]", 12)
    ]) #declara a struct Pessoa
    
    gc.declarar_variavel_struct("p", "Pessoa") #declara a variável p
    
    gc.ldc(100) #carrega o valor 100
    gc.carregar_variavel("p") #carrega a variável p
    gc.ldc(4) #carrega o valor 4
    gc.add() #adição
    gc.ldc(0) #carrega o valor 0
    gc.ldc(4) #carrega o valor 4
    gc.mul() #multiplicação
    gc.add() #adição
    gc.emitir("STI") #emite a instrução STI
    
    gc.fim_programa()
    codigo = gc.get_codigo() #obtém o código gerado
    
    assert "_p DS 16" in codigo, "deve reservar 16 bytes" #verifica se o código contém a instrução _p DS 16
    assert "STI" in codigo, "deve usar STI para struct com array" #verifica se o código contém a instrução STI
    print("  [ok] struct com array")
    return True #retorna True se o teste passou
#---------------------------------------------------------------------------------------------------------
def executar_todos_testes():     #executa todos os testes
    print("======================================================")
    print("executando testes do gerador de código")
    print("======================================================")
    print()
    
    testes = [
        testar_expressao_atribuicao,    #teste 1 expressao de atribuicao
        testar_incremento,    #teste 2 incremento e decremento
        testar_operador_mais_igual,    #teste 3 operador mais igual
        testar_operador_condicional,    #teste 4 operador condicional
        testar_do_while,    #teste 5 comando do while
        testar_for,    #teste 6 comando for
        testar_break_continue,    #teste 7 break e continue 
        testar_struct,    #teste 8 struct simples
        testar_array,    #teste 9 array de inteiros
        testar_struct_com_array    #teste 10 struct com array
    ] #lista de testes
    
    resultados = [] #lista de resultados
    for teste in testes:
        try:
            resultado = teste()
            resultados.append(("ok", teste.__name__))
        except AssertionError as e:
            print(f"  [erro] {e}")
            resultados.append(("erro", teste.__name__))
        except Exception as e:
            print(f"  [excecao] {e}")
            resultados.append(("exceção", teste.__name__))
        print()
    
    print("======================================================")
    print("resumo dos testes")
    print("======================================================")
    
    ok = sum(1 for status, _ in resultados if status == "ok")
    erros = sum(1 for status, _ in resultados if status != "ok")
    
    print(f"testes passaram: {ok}/{len(testes)}")
    print(f"testes falharam: {erros}/{len(testes)}")
    
    if erros > 0:
        print("\ntestes que falharam:")
        for status, nome in resultados:
            if status != "ok":
                print(f"  - {nome}: {status}")
    
    print()
    return erros == 0
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":    #executa todos os testes
    sucesso = executar_todos_testes()
    if sucesso:
        print("[ok] todos os testes passaram!")
    else:
        print("[erro] alguns testes falharam")
    exit(0 if sucesso else 1)

