# gerador de código - tarefa 4

implementação de um gerador de código para máquina de pilha baseado nos exemplos vistos em aula e nas referências fornecidas.

# comandos de teste

- `python src/teste/testar.py`  
  executa o suite unitário principal, com asserts que checam a presença das instruções geradas para cada funcionalidade.
- `python src/executar_todos_testes.py`  
  roda cada script isolado em `src/teste`, exibindo o código produzido e verificando se a geração ocorre sem erros.
- `python src/regressao_exemplos.py`  
  compara o código gerado pelas funções de `exemplos_teste` com os snapshots em `exemplo/expected`, garantindo regressão controlada.
- `python src/main.py`  
  apresenta todos os exemplos integrados, servindo como demonstração manual do código emitido para cada recurso.

# papel de cada script principal

- `src/gerador_codigo.py`: coração do projeto. mantém tabela de símbolos, gera instruções de máquina de pilha para operadores, estruturas de controle, arrays e structs. todas as demais camadas usam este módulo para produzir código.
- `src/exemplos_teste.py`: expõe funções `teste_01_*` a `teste_11_*` que criam instâncias de `GeradorCodigo`, constroem programas exemplo e retornam o código emitido. serve tanto para demonstração (`main.py`) quanto para regressão.
- `src/main.py`: vitrine interativa. importa `exemplos_teste` e imprime sequencialmente o código gerado, útil para apresentação manual.
- `src/teste/testar.py`: suíte agregadora com asserts que validam o texto das instruções para cada cenário. auxilia a detectar regressões na geração.
- `src/teste/teste_*.py`: casos unitários específicos. cada arquivo descreve o programa fonte, gera o código e imprime o resultado; alguns verificam propriedades adicionais.
- `src/executar_todos_testes.py`: orquestra a execução de cada teste em `src/teste`, relatando sucesso ou falha. garante que todos os scripts rodem no ambiente correto.
- `src/regressao_exemplos.py`: percorre `exemplo/teste_*.txt`, invoca a função homônima em `exemplos_teste` e compara com snapshots em `exemplo/expected`. útil para revisão automática do código gerado.

# artefatos de teste em `exemplo/`

- `exemplo/teste_*.txt`: documentação executável. cada arquivo contém a descrição do programa fonte e o trecho “código gerado”, alinhado com a saída atual do gerador. serve como referência humana e base para a regressão.
- `exemplo/expected/*.txt`: snapshots atualizados pelo script de regressão. mantêm a saída esperada para comparação automática.
- `exemplo/exemplos`: script opcional que demonstra as funcionalidades, semelhante ao `main.py`, porém organizado em funções auxiliares.
- `exemplo/testes`: conjunto de entradas adicionais que podem ser usados manualmente com `main.py` ou scripts customizados.

# aderência ao enunciado

- expressão de atribuição (`expressao_atribuicao`) transforma comandos em expressões reutilizáveis, conforme solicitado.
- operadores de pré e pós incremento/decremento (`pre_incremento`, `pos_incremento`, `pre_decremento`, `pos_decremento`) geram o fluxo correto na pilha.
- operador `+=` está implementado via `atribuicao_adicao`, acumulando e preservando o resultado.
- operador condicional `?:` utiliza rótulos gerados dinamicamente (`operador_condicional`) para saltos `jzer` e `jmp`.
- comandos `do-while`, `for`, `break` e `continue` são suportados por `inicio_do_while`, `fim_do_while`, `inicio_for`, `fim_for`, `break_cmd` e `continue_cmd`.
- structs recebem suporte completo (`declarar_struct`, `declarar_variavel_struct`, `atribuir_campo_struct`, etc.), atendendo ao requisito adicional de 2 pontos.
- bônus:
  - arrays de inteiros (`declarar_array`, `atribuir_array_elemento`, `carregar_array_elemento`).
  - arrays de structs e structs com arrays (`declarar_array_struct`, `atribuir_campo_struct_array`, `carregar_campo_struct_array`).

cada funcionalidade possui:
- teste automatizado em `src/teste/*.py`
- exemplo documentado em `exemplo/teste_*.txt`
- cobertura no relatório de regressão


## estrutura do projeto

```
t4_construcaoDeCompiladores/
├── src/                    # código fonte
│   └── gerador_codigo.py  # implementação principal
├── testes/                # testes automatizados
│   ├── testar.py          # testes automatizados completos
│   ├── executar_todos_testes.py  # executa todos os testes
│   └── teste_*.py         # testes individuais (10 arquivos)
├── exemplos/              # exemplos de uso
│   ├── exemplo_uso.py     # exemplos detalhados
│   ├── exemplos_teste.py  # funções de teste
│   └── main.py            # demonstração completa
├── docs/                  # documentação
│   ├── README.md          # este arquivo
│   ├── COMO_TESTAR.md     # guia de testes
│   ├── TESTE_RAPIDO.md    # guia rápido
│   ├── README_TESTES.md   # documentação dos testes
│   └── teste_*.txt        # exemplos documentados (10 arquivos)
├── output/                # saída gerada (opcional)
├── COMANDOS.md            # todos os comandos para executar
└── enunciadoT4.txt        # enunciado da tarefa
```

## início rápido

### executar testes automatizados

```bash
python testes/testar.py
```

### ver demonstração completa

```bash
python exemplos/main.py
```

### executar um teste específico

```bash
python testes/teste_01_expressao_atribuicao.py
```

para mais comandos, veja [COMANDOS.md](COMANDOS.md)

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

## uso básico

```python
import sys
sys.path.append('src')
from gerador_codigo import GeradorCodigo

# cria um novo gerador
gc = GeradorCodigo()

# inicia o programa
gc.inicio_programa()

# declara variáveis
gc.declarar_variavel("x", "integer", 4)

# gera código de exemplo
gc.ldc(5)
gc.expressao_atribuicao("x")

# finaliza o programa
gc.fim_programa()

# exibe o código gerado
print(gc.get_codigo())
```

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

## documentação

- [COMANDOS.md](COMANDOS.md) - todos os comandos para executar
- [docs/COMO_TESTAR.md](docs/COMO_TESTAR.md) - guia detalhado de como testar
- [docs/TESTE_RAPIDO.md](docs/TESTE_RAPIDO.md) - guia rápido de teste
- [docs/README_TESTES.md](docs/README_TESTES.md) - documentação dos testes individuais

## referências

- `refsTexto/geracaoCodigo_rascunho.txt`: exemplo de geração de código visto em aula
- `refsTexto/19-Final-Code-Generation.txt`: referência sobre geração de código final
- `refsTexto/16-Intermediate-Representation.txt`: representação intermediária
- `refsTexto/18-Processor-Architectures.txt`: arquiteturas de processadores
- `refsTexto/x64_cheatsheet.txt`: referência de instruções x64


todos os testes passaram (10/10) ✓

