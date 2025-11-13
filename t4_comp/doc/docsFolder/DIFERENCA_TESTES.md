# diferença entre os arquivos de teste

## resumo executivo

existem três arquivos diferentes que servem propósitos distintos:

1. **`testar.py`** - validação com assertions (testes unitários)
2. **`exemplos_teste.py`** - geração de exemplos (demonstração)
3. **`executar_todos_testes.py`** - orquestrador de testes (execução externa)

---

## 1. testar.py (`src/teste/testar.py`)

### propósito
script de teste com validação automática usando assertions

### características
- contém funções de teste com validações (asserts)
- verifica se o código gerado contém instruções específicas
- executa todos os testes internamente
- mostra resumo de passou/falhou
- usa `assert` para validar o código gerado

### exemplo de uso
```python
def testar_expressao_atribuicao():
    gc = GeradorCodigo()
    # ... gera código ...
    codigo = gc.get_codigo()
    
    # validações com assert
    assert "DUP" in codigo, "deve conter DUP"
    assert "STA _x" in codigo, "deve atribuir a x"
    return True
```

### quando usar
- para validar que a implementação está correta
- para verificar se instruções específicas são geradas
- para garantir que funcionalidades não quebram

### saída
```
testando: expressão de atribuição
  [ok] expressao de atribuicao
testando: incremento e decremento
  [ok] incremento/decremento
...
resumo dos testes
testes passaram: 10/10
```

---

## 2. exemplos_teste.py (`src/exemplos_teste.py`)

### propósito
gera código de exemplo para demonstração (sem validação)

### características
- contém funções que geram código
- apenas gera o código, não valida
- retorna o código gerado como string
- não usa assertions
- focado em demonstração/exibição

### exemplo de uso
```python
def teste_01_expressao_atribuicao():
    gc = GeradorCodigo()
    # ... gera código ...
    return gc.get_codigo()  # retorna código gerado
```

### quando usar
- para ver exemplos de código gerado
- para documentação
- para entender como usar a API
- para demonstrar funcionalidades

### saída
```
=== teste 1: expressão de atribuição ===
JMP _start
_x DS 4
_y DS 4
LDC 5
DUP
STA _x
...
```

---

## 3. executar_todos_testes.py (`src/executar_todos_testes.py`)

### propósito
executa os arquivos de teste individuais (`teste_XX_*.py`) externamente

### características
- orquestra a execução de múltiplos arquivos de teste
- usa `subprocess` para executar cada teste
- executa os arquivos `teste_01_*.py`, `teste_02_*.py`, etc.
- agrega resultados de múltiplos testes
- não contém os testes em si, apenas os executa

### exemplo de uso
```python
TESTES = [
    ("expressao de atribuicao", "teste_01_expressao_atribuicao.py"),
    ("incremento e decremento", "teste_02_incremento_decremento.py"),
    # ...
]

# executa cada arquivo externamente
subprocess.run([sys.executable, str(caminho)])
```

### quando usar
- para executar todos os testes individuais de uma vez
- para rodar testes que estão em arquivos separados
- para ter um resumo consolidado de todos os testes

### saída
```
======================================================
teste 1: expressao de atribuicao
======================================================
executando: teste/teste_01_expressao_atribuicao.py
teste 1: expressao de atribuicao
...
resumo dos testes
testes executados: 11
testes passaram: 11
testes falharam: 0
```

---

## comparação direta

| característica | testar.py | exemplos_teste.py | executar_todos_testes.py |
|----------------|-----------|-------------------|--------------------------|
| **localização** | `src/teste/` | `src/` | `src/` |
| **validação** | sim (asserts) | não | não (delega aos testes) |
| **executa testes externos** | não | não | sim |
| **gera código** | sim | sim | não |
| **mostra código gerado** | não | sim | sim (via testes) |
| **resumo de resultados** | sim | não | sim |
| **propósito principal** | validar implementação | demonstrar uso | orquestrar execução |

---

## arquivos relacionados

### arquivos de teste individuais (`src/teste/teste_XX_*.py`)
- `teste_01_expressao_atribuicao.py`
- `teste_02_incremento_decremento.py`
- `teste_03_operador_mais_igual.py`
- etc.

esses arquivos são executados por `executar_todos_testes.py` e geram código de exemplo similar a `exemplos_teste.py`, mas são arquivos separados para organização.

---

## quando usar cada um

### use `testar.py` quando:
- quiser validar que a implementação está correta
- quiser verificar se instruções específicas são geradas
- quiser garantir que funcionalidades não quebram
- quiser fazer testes unitários

### use `exemplos_teste.py` quando:
- quiser ver exemplos de código gerado
- quiser entender como usar a API
- quiser demonstrar funcionalidades
- quiser documentar o uso

### use `executar_todos_testes.py` quando:
- quiser executar todos os testes individuais de uma vez
- quiser rodar testes que estão em arquivos separados
- quiser ter um resumo consolidado de todos os testes
- quiser automatizar a execução de todos os testes

---

## fluxo de trabalho recomendado

1. **desenvolvimento**: use `testar.py` para validar durante o desenvolvimento
2. **demonstração**: use `exemplos_teste.py` ou os arquivos `teste_XX_*.py` para ver exemplos
3. **validação final**: use `executar_todos_testes.py` para executar todos os testes antes de entregar

---

## resumo

- **testar.py** = validação com assertions (testes unitários)
- **exemplos_teste.py** = geração de exemplos (demonstração)
- **executar_todos_testes.py** = orquestrador de testes (execução externa)

todos servem propósitos diferentes e complementares!

