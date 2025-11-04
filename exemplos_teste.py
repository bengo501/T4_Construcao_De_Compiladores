"""
exemplos de teste para cada funcionalidade
cada função gera código de exemplo para uma funcionalidade específica
"""

from gerador_codigo import GeradorCodigo

def teste_01_expressao_atribuicao():
    """teste: expressão de atribuição"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("x", "integer", 4)
    gc.declarar_variavel("y", "integer", 4)
    
    # x := 5 (expressão de atribuição)
    gc.ldc(5)
    gc.expressao_atribuicao("x")
    
    # y := x := 5 (cadeia de atribuições)
    gc.expressao_atribuicao("y")
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_02_incremento_decremento():
    """teste: incremento e decremento"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("a", "integer", 4)
    gc.declarar_variavel("b", "integer", 4)
    
    gc.ldc(0)
    gc.atribuir_variavel("a")
    gc.ldc(0)
    gc.atribuir_variavel("b")
    
    # pré-incremento: ++a
    gc.pre_incremento("a")
    gc.emitir("DROP")  # descarta valor retornado
    
    # pós-incremento: b++
    gc.pos_incremento("b")
    gc.emitir("DROP")  # descarta valor retornado
    
    # pré-decremento: --a
    gc.pre_decremento("a")
    gc.emitir("DROP")
    
    # pós-decremento: b--
    gc.pos_decremento("b")
    gc.emitir("DROP")
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_03_operador_mais_igual():
    """teste: operador +="""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("x", "integer", 4)
    
    # inicializa x
    gc.ldc(10)
    gc.atribuir_variavel("x")
    
    # x += 5
    gc.ldc(5)
    gc.atribuicao_adicao("x")
    gc.emitir("DROP")  # descarta valor retornado
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_04_operador_condicional():
    """teste: operador condicional ?:"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
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
    
    gc.jzer(rotulo_else)
    gc.carregar_variavel("x")
    gc.jmp(rotulo_fim)
    gc.emitir_rotulo(rotulo_else)
    gc.carregar_variavel("y")
    gc.emitir_rotulo(rotulo_fim)
    
    gc.atribuir_variavel("z")
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_05_do_while():
    """teste: comando do-while"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4)
    
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    # do { i++ } while (i < 10)
    rotulo_inicio, rotulo_fim = gc.inicio_do_while()
    
    gc.pos_incremento("i")
    gc.emitir("DROP")
    
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    
    gc.fim_do_while()
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_06_for():
    """teste: comando for"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4)
    
    # for (i := 0; i < 10; i++)
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    rotulo_teste, rotulo_incremento, rotulo_fim = gc.inicio_for()
    
    # teste: i < 10
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.teste_for()
    
    # incremento: i++
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("i")
    
    gc.fim_for()
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_07_break_continue():
    """teste: comandos break e continue"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("i", "integer", 4)
    
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    # while (i < 10)
    rotulo_inicio, rotulo_fim = gc.inicio_while()
    
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.jzer(rotulo_fim)
    
    gc.pos_incremento("i")
    gc.emitir("DROP")
    
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

def teste_08_struct():
    """teste: variáveis do tipo struct"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara struct Ponto
    gc.declarar_struct("Ponto", [
        ("x", "integer", 4),
        ("y", "integer", 4)
    ])
    
    # declara variável do tipo Ponto
    gc.declarar_variavel_struct("p", "Ponto")
    
    # p.x := 10
    gc.ldc(10)
    gc.carregar_variavel("p")
    gc.ldc(0)  # offset do campo x
    gc.add()
    gc.emitir("STI")
    
    # p.y := 20
    gc.ldc(20)
    gc.carregar_variavel("p")
    gc.ldc(4)  # offset do campo y
    gc.add()
    gc.emitir("STI")
    
    gc.fim_programa()
    return gc.get_codigo()

def teste_09_array_inteiros():
    """teste: arrays de inteiros (bonus)"""
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

def teste_10_struct_com_array():
    """teste: struct com array (bonus)"""
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
    print("=== teste 1: expressão de atribuição ===")
    print(teste_01_expressao_atribuicao())
    print("\n=== teste 2: incremento e decremento ===")
    print(teste_02_incremento_decremento())
    print("\n=== teste 3: operador += ===")
    print(teste_03_operador_mais_igual())
    print("\n=== teste 4: operador condicional ?: ===")
    print(teste_04_operador_condicional())
    print("\n=== teste 5: comando do-while ===")
    print(teste_05_do_while())
    print("\n=== teste 6: comando for ===")
    print(teste_06_for())
    print("\n=== teste 7: break e continue ===")
    print(teste_07_break_continue())
    print("\n=== teste 8: struct ===")
    print(teste_08_struct())
    print("\n=== teste 9: arrays de inteiros (bonus) ===")
    print(teste_09_array_inteiros())
    print("\n=== teste 10: struct com array (bonus) ===")
    print(teste_10_struct_com_array())

