# arquivos necessários para entrega - t4

## resumo executivo

**obrigatório para entrega:**
- `src/gerador_codigo.py` - código principal
- `src/teste/teste_01_*.py` até `teste_08_*.py` - 8 arquivos de teste
- `README.md` - documentação básica

**opcional (mas recomendado):**
- testes bonus (`teste_09_*.py` até `teste_11_*.py`)
- scripts auxiliares (`main.py`, `executar_todos_testes.py`)

**não necessário:**
- pastas `refs/`, `refsTexto/`, `doc/`, `output/`, `__pycache__/`

## requisitos do enunciado

o enunciado pede:
- alterar o exemplo de geração de código para as estruturas solicitadas
- **para cada exercício realizado apresentar pelo menos um arquivo de teste**
- fazer programas pequenos que vão introduzindo os novos itens implementados

## estrutura mínima necessária

### 1. código principal (obrigatório)

```
src/
  └── gerador_codigo.py          # implementação principal do gerador
```

### 2. arquivos de teste (obrigatórios - um por funcionalidade)

**funcionalidades principais (9,0 pontos):**
```
src/teste/
  ├── teste_01_expressao_atribuicao.py      # transformar atribuição em expressão
  ├── teste_02_incremento_decremento.py     # pós e pré incremento/decremento
  ├── teste_03_operador_mais_igual.py      # operador +=
  ├── teste_04_operador_condicional.py      # operador ?:
  ├── teste_05_do_while.py                  # comando do-while
  ├── teste_06_for.py                       # comando for
  ├── teste_07_break_continue.py            # comandos break e continue
  └── teste_08_struct.py                    # variáveis do tipo struct (2,0 pontos)
```

**funcionalidades bonus (opcional, mas implementadas):**
```
src/teste/
  ├── teste_09_array_inteiros.py           # arrays de inteiros (bonus)
  ├── teste_10_struct_com_array.py          # structs com arrays (bonus)
  └── teste_11_array_de_structs.py          # arrays de structs (bonus)
```

### 3. documentação básica (recomendado)

```
README.md                    # explicação do projeto e como executar
```

### 4. arquivos auxiliares (opcionais, mas úteis)

```
src/
  ├── main.py                # script para executar exemplos
  ├── executar_todos_testes.py  # script para rodar todos os testes
  └── teste/
      └── testar.py          # script de validação dos testes
```

## arquivos que NÃO são necessários para entrega

### podem ser excluídos:
- `__pycache__/` - arquivos compilados do python
- `refs/` - referências de estudo (pdfs, pptx)
- `refsTexto/` - textos de referência
- `doc/` - documentação extra (muitos .md)
- `output/` - arquivos de saída gerados
- `enunciado/` - cópia do enunciado (já conhecido pelo professor)
- arquivos `.txt` duplicados em `exemplo/`

### observações:
- os arquivos `.txt` em `exemplo/` parecem ser duplicados dos testes
- a pasta `exemplo/` pode ser removida se os testes estão em `src/teste/`

## estrutura final recomendada para entrega

```
t4_construcaoDeCompiladores/
├── README.md
└── src/
    ├── gerador_codigo.py
    ├── main.py (opcional)
    ├── executar_todos_testes.py (opcional)
    └── teste/
        ├── testar.py (opcional)
        ├── teste_01_expressao_atribuicao.py
        ├── teste_02_incremento_decremento.py
        ├── teste_03_operador_mais_igual.py
        ├── teste_04_operador_condicional.py
        ├── teste_05_do_while.py
        ├── teste_06_for.py
        ├── teste_07_break_continue.py
        ├── teste_08_struct.py
        ├── teste_09_array_inteiros.py (bonus)
        ├── teste_10_struct_com_array.py (bonus)
        └── teste_11_array_de_structs.py (bonus)
```

## resumo

### obrigatório:
1. `src/gerador_codigo.py` - código principal
2. `src/teste/teste_01_*.py` até `teste_08_*.py` - testes das funcionalidades principais
3. `README.md` - documentação básica

### recomendado:
4. `src/teste/teste_09_*.py` até `teste_11_*.py` - testes bonus
5. scripts auxiliares (`main.py`, `executar_todos_testes.py`, `testar.py`)

### não necessário:
- pastas de referência (`refs/`, `refsTexto/`)
- documentação excessiva (`doc/` com muitos arquivos)
- arquivos temporários (`__pycache__/`, `output/`)
- duplicatas

## status dos arquivos

todos os arquivos de teste necessários estão presentes:
- `teste_01_expressao_atribuicao.py` ✓
- `teste_02_incremento_decremento.py` ✓
- `teste_03_operador_mais_igual.py` ✓
- `teste_04_operador_condicional.py` ✓
- `teste_05_do_while.py` ✓
- `teste_06_for.py` ✓
- `teste_07_break_continue.py` ✓
- `teste_08_struct.py` ✓
- `teste_09_array_inteiros.py` ✓ (bonus)
- `teste_10_struct_com_array.py` ✓ (bonus)
- `teste_11_array_de_structs.py` ✓ (bonus)

