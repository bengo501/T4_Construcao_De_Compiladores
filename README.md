# gerador de código - tarefa 4

implementação de um gerador de código para máquina de pilha baseado nos exemplos vistos em aula e nas referências fornecidas.

## funcionalidades implementadas (9,0 pontos)

1. **expressão de atribuição**: transformar comando de atribuição em expressão de atribuição
   - permite cadeias de atribuições como `y := x := 5`

2. **incremento/decremento**: expressões de pós e pré incremento/decremento
   - pré-incremento: `++var`
   - pós-incremento: `var++`
   - pré-decremento: `--var`
   - pós-decremento: `var--`

3. **operador +=**: adicionar o operador "+="
   - `var += exp` é equivalente a `var := var + exp`

4. **operador condicional ?:** adicionar o operador condicional "?:"
   - `exp1 ? exp2 : exp3` retorna exp2 se exp1 é verdadeiro, senão exp3

5. **comando do-while**: adicionar um comando do-while
   - `do { comandos } while (expressão);`

6. **comando for**: adicionar o comando for
   - `for (exp1; exp2; exp3) { comandos }`
   - as 3 expressões podem ser vazias

7. **comandos break e continue**: adicionar comandos break e continue
   - `break` sai do loop mais interno
   - `continue` pula para a próxima iteração do loop mais interno

8. **variáveis do tipo struct** (2,0 pontos): adicionar possibilidade de usar variáveis do tipo struct
   - declaração de struct com campos
   - acesso a campos: `var.campo`

## funcionalidades bonus (1 ponto cada)

9. **arrays de inteiros**: gerar código (declaração e expressões) para arrays de inteiros
   - declaração: `arr : array [5] of integer;`
   - acesso: `arr[0] := 10;` e `x := arr[2];`

10. **structs com arrays**: permitir criar structs que tenham um array como campo da struct
    - struct pode conter array como campo
    - acesso: `p.scores[0] := 100;`

## arquivos

- `gerador_codigo.py`: implementação principal do gerador de código
- `exemplos_teste.py`: exemplos de uso para cada funcionalidade
- `exemplo_uso.py`: exemplos adicionais de uso
- `teste_01_expressao_atribuicao.txt` até `teste_10_struct_com_array.txt`: arquivos de teste documentando cada funcionalidade

## instruções da máquina de pilha

### instruções básicas
- `LDC N`: empilha constante N
- `LDA rotulo`: empilha conteúdo do endereço rotulo
- `STA rotulo`: desempilha e armazena no endereço rotulo
- `DUP`: duplica topo da pilha
- `DROP`: desempilha uma palavra (descarta topo da pilha)

### operações aritméticas
- `ADD`: desempilha RT1 e RT2, empilha RT2 + RT1
- `SUB`: desempilha RT1 e RT2, empilha RT2 - RT1
- `MUL`: desempilha RT1 e RT2, empilha RT2 * RT1
- `DIV`: desempilha RT1 e RT2, empilha RT2 / RT1
- `MOD`: desempilha RT1 e RT2, empilha RT2 % RT1
- `NEG`: desempilha RT1, empilha -RT1

### comparações
- `EQ`: desempilha RT1 e RT2, empilha 1 se RT2 == RT1, senão 0
- `NE`: desempilha RT1 e RT2, empilha 1 se RT2 != RT1, senão 0
- `GRT`: desempilha RT1 e RT2, empilha 1 se RT2 > RT1, senão 0
- `LES`: desempilha RT1 e RT2, empilha 1 se RT2 < RT1, senão 0
- `GEQ`: desempilha RT1 e RT2, empilha 1 se RT2 >= RT1, senão 0
- `LEQ`: desempilha RT1 e RT2, empilha 1 se RT2 <= RT1, senão 0

### controle de fluxo
- `JMP rotulo`: desvia para rótulo
- `JZER rotulo`: desempilha e, se zero, desvia para rótulo
- `JNZ rotulo`: desempilha e, se não zero, desvia para rótulo

### acesso indireto
- `LDI`: carrega indiretamente (desempilha endereço, empilha valor no endereço)
- `STI`: armazena indiretamente (desempilha valor e endereço, armazena valor no endereço)

### pseudo-instruções
- `DS N`: reserva N posições a partir do endereço atual
- `DC N`: armazena N no endereço corrente e reserva essa posição
- `NOP`: não faz nada (usado como rótulo)
- `HALT`: para execução

## uso

```python
from gerador_codigo import GeradorCodigo

gc = GeradorCodigo()
gc.inicio_programa()

# declara variáveis
gc.declarar_variavel("x", "integer", 4)

# gera código
gc.ldc(5)
gc.expressao_atribuicao("x")

gc.fim_programa()
print(gc.get_codigo())
```

## executar exemplos

```bash
python exemplos_teste.py
```

## referências

- `refsTexto/geracaoCodigo_rascunho.txt`: exemplo de geração de código visto em aula
- `refsTexto/19-Final-Code-Generation.txt`: referência sobre geração de código final
- `refsTexto/16-Intermediate-Representation.txt`: representação intermediária
- `refsTexto/18-Processor-Architectures.txt`: arquiteturas de processadores
- `refsTexto/x64_cheatsheet.txt`: referência de instruções x64

