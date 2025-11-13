# resumo: diferenças entre os arquivos de teste

## visão geral rápida

```
┌─────────────────────────────────────────────────────────────┐
│                    testar.py                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ validação com assertions (testes unitários)         │   │
│  │ - contém funções de teste com asserts               │   │
│  │ - valida se código gerado está correto              │   │
│  │ - mostra resumo: passou/falhou                      │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                exemplos_teste.py                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ geração de exemplos (demonstração)                  │   │
│  │ - contém funções que geram código                   │   │
│  │ - retorna código gerado como string                 │   │
│  │ - sem validação, apenas demonstra                   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│            executar_todos_testes.py                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ orquestrador de testes (execução externa)           │   │
│  │ - executa arquivos teste_XX_*.py externamente       │   │
│  │ - usa subprocess para rodar cada teste              │   │
│  │ - agrega resultados de múltiplos testes             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## comparação lado a lado

| aspecto | testar.py | exemplos_teste.py | executar_todos_testes.py |
|---------|-----------|-------------------|--------------------------|
| **localização** | `src/teste/` | `src/` | `src/` |
| **tipo** | validação | demonstração | orquestração |
| **valida com asserts** | sim | não | não |
| **gera código** | sim | sim | não |
| **mostra código gerado** | não | sim | sim (via testes) |
| **executa testes externos** | não | não | sim |
| **usa subprocess** | não | não | sim |
| **resumo de resultados** | sim | não | sim |
| **quantos testes** | 10 (internos) | 11 (funções) | 11 (arquivos) |

---

## exemplo de uso

### testar.py
```python
def testar_expressao_atribuicao():
    gc = GeradorCodigo()
    # ... gera código ...
    codigo = gc.get_codigo()
    
    # validação com assert
    assert "DUP" in codigo, "deve conter DUP"
    assert "STA _x" in codigo, "deve atribuir a x"
    return True
```

**saída:**
```
testando: expressão de atribuição
  [ok] expressao de atribuicao
```

### exemplos_teste.py
```python
def teste_01_expressao_atribuicao():
    gc = GeradorCodigo()
    # ... gera código ...
    return gc.get_codigo()  # retorna código
```

**saída:**
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

### executar_todos_testes.py
```python
TESTES = [
    ("expressao de atribuicao", "teste_01_expressao_atribuicao.py"),
    # ...
]

# executa cada arquivo externamente
subprocess.run([sys.executable, str(caminho)])
```

**saída:**
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
```

---

## quando usar cada um

### use testar.py quando:
- quiser validar que a implementação está correta
- quiser verificar se instruções específicas são geradas
- quiser fazer testes unitários rápidos
- quiser garantir que funcionalidades não quebram

### use exemplos_teste.py quando:
- quiser ver exemplos de código gerado
- quiser entender como usar a API
- quiser demonstrar funcionalidades
- quiser documentar o uso

### use executar_todos_testes.py quando:
- quiser executar todos os testes individuais de uma vez
- quiser rodar testes que estão em arquivos separados
- quiser ter um resumo consolidado de todos os testes
- quiser automatizar a execução de todos os testes

---

## arquivos relacionados

### arquivos de teste individuais
- `src/teste/teste_01_expressao_atribuicao.py`
- `src/teste/teste_02_incremento_decremento.py`
- `src/teste/teste_03_operador_mais_igual.py`
- etc.

esses arquivos são executados por `executar_todos_testes.py` e geram código de exemplo similar a `exemplos_teste.py`, mas são arquivos separados para organização.

---

## resumo em uma frase

- **testar.py** = validação com assertions (testes unitários)
- **exemplos_teste.py** = geração de exemplos (demonstração)
- **executar_todos_testes.py** = orquestrador de testes (execução externa)

