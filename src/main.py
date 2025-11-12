# main demonstra todas as funcionalidades implementadas
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from exemplos_teste import *

if __name__ == "__main__":
    print("======================================================")
    print("gerador de código - tarefa 4")
    print("demonstração de todas as funcionalidades implementadas")
    print("======================================================")
    print()
    
    print("======================================================")
    print("teste 1: expressão de atribuição")
    print("======================================================")
    print(teste_01_expressao_atribuicao())
    print()
    
    print("======================================================")
    print("teste 2: incremento e decremento")
    print("======================================================")
    print(teste_02_incremento_decremento())
    print()
    
    print("======================================================")
    print("teste 3: operador +=")
    print("======================================================")
    print(teste_03_operador_mais_igual())
    print()
    
    print("======================================================")
    print("teste 4: operador condicional ?:")
    print("======================================================")
    print(teste_04_operador_condicional())
    print()
    
    print("======================================================")
    print("teste 5: comando do-while")
    print("======================================================")
    print(teste_05_do_while())
    print()
    
    print("======================================================")
    print("teste 6: comando for")
    print("======================================================")
    print(teste_06_for())
    print()
    
    print("======================================================")
    print("teste 7: break e continue")
    print("======================================================")
    print(teste_07_break_continue())
    print()
    
    print("======================================================")
    print("teste 8: variáveis do tipo struct")
    print("======================================================")
    print(teste_08_struct())
    print()
    
    print("======================================================")
    print("teste 9: arrays de inteiros (bonus)")
    print("======================================================")
    print(teste_09_array_inteiros())
    print()
    
    print("======================================================")
    print("teste 10: struct com array (bonus)")
    print("======================================================")
    print(teste_10_struct_com_array())
    print()
    
    print("======================================================")
    print("todos os testes foram executados com sucesso!")
    print("======================================================")

