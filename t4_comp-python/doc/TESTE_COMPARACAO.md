# script de teste com comparação

## descrição

o script `src/teste_comparacao.py` executa os testes individuais e mostra:
1. programa fonte (do arquivo .txt)
2. código gerado (executando o teste)
3. código esperado (do arquivo .txt)
4. comparação entre gerado e esperado

## como usar

### executar todos os testes
```bash
python src/teste_comparacao.py
```

### exemplo de saída
```
======================================================
teste 8: struct simples
======================================================
executando: teste\teste_08_struct.py

programa fonte:
struct Ponto {
    x : integer;
    y : integer;
};
p : Ponto;
p.x := 10;
p.y := 20;

codigo gerado:
JMP _start
_p DS 8
LDC 10
LDA _p
LDC 0
ADD
STI
_start: NOP
HALT

codigo esperado:
JMP _start
_p DS 8
LDC 10
LDA _p
LDC 0
ADD
STI
LDC 20
LDA _p
LDC 4
ADD
STI
_start: NOP
HALT

[erro] código gerado diverge do esperado

diferenças:
  linha 8:
    gerado:   _start: NOP
    esperado: LDC 20
  linha 9:
    gerado:   HALT
    esperado: LDA _p
  ...
```

## estrutura

### arquivos necessários

1. **arquivos de teste** (`src/teste/teste_XX_*.py`)
   - executados pelo script
   - geram código de exemplo

2. **arquivos de referência** (`exemplo/teste_XX_*.txt`)
   - contêm programa fonte e código esperado
   - usados para comparação

### formato dos arquivos .txt

```
teste X: descrição
programa: descrição do programa

programa fonte:
código fonte do programa...

código gerado:
código esperado...
```

## funcionalidades

### extração automática
- extrai programa fonte dos arquivos .txt
- extrai código esperado dos arquivos .txt
- extrai código gerado da saída dos testes

### comparação inteligente
- normaliza espaços em branco
- compara linha por linha
- mostra diferenças detalhadas

### resumo de resultados
- mostra quantos testes passaram/falharam
- lista testes que falharam
- código de saída: 0 se todos passaram, 1 se algum falhou

## exemplos de uso

### executar um teste específico
edite o script para executar apenas um teste:
```python
# em executar_todos(), modifique:
TESTES = [
    ("struct simples", "teste_08_struct.py"),
]
```

### ver apenas diferenças
o script mostra apenas as linhas que diferem entre gerado e esperado.

### atualizar código esperado
se o código gerado estiver correto, atualize o arquivo .txt correspondente em `exemplo/`.

## diferenças em relação a outros scripts

| script | propósito | mostra código esperado |
|--------|-----------|------------------------|
| `testar.py` | validação com asserts | não |
| `exemplos_teste.py` | geração de exemplos | não |
| `executar_todos_testes.py` | executa testes externos | não |
| `teste_comparacao.py` | comparação visual | sim |

## resumo

este script é útil para:
- verificar se o código gerado está correto
- comparar código gerado com o esperado
- identificar diferenças facilmente
- validar implementações visualmente

