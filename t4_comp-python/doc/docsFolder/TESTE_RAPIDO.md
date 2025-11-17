# como testar o funcionamento da implementação

## método mais rápido: executar todos os testes

```bash
python testar.py
```

este comando executa todos os testes e verifica se todas as funcionalidades estão funcionando corretamente.

**saída esperada:**
```
============================================================
executando testes do gerador de código
============================================================

testando: expressão de atribuição
  [ok] expressao de atribuicao

testando: incremento e decremento
  [ok] incremento/decremento

...

============================================================
resumo dos testes
============================================================
testes passaram: 10/10
testes falharam: 0/10

[ok] todos os testes passaram!
```

## outros métodos de teste

### ver exemplos de código gerado

```bash
python main.py
```

mostra código de exemplo gerado para cada funcionalidade.

### executar testes individuais

```bash
python exemplos_teste.py
```

executa funções de teste individuais.

### criar seu próprio teste

```python
from gerador_codigo import GeradorCodigo

gc = GeradorCodigo()
gc.inicio_programa()

# declara variável
gc.declarar_variavel("x", "integer", 4)

# gera código
gc.ldc(5)
gc.expressao_atribuicao("x")

gc.fim_programa()

# exibe código gerado
print(gc.get_codigo())
```

## verificar arquivos de teste

cada funcionalidade tem um arquivo de teste documentado:

- `teste_01_expressao_atribuicao.txt`
- `teste_02_incremento_decremento.txt`
- `teste_03_operador_mais_igual.txt`
- `teste_04_operador_condicional.txt`
- `teste_05_do_while.txt`
- `teste_06_for.txt`
- `teste_07_break_continue.txt`
- `teste_08_struct.txt`
- `teste_09_array_inteiros.txt`
- `teste_10_struct_com_array.txt`

esses arquivos contêm exemplos de código fonte e o código gerado esperado.

## funcionalidades testadas

1. expressão de atribuição
2. incremento/decremento (++, --)
3. operador +=
4. operador condicional ?:
5. comando do-while
6. comando for
7. break e continue
8. variáveis do tipo struct
9. arrays de inteiros (bonus)
10. struct com array (bonus)

## dica

comece sempre executando `python testar.py` para verificar se tudo está funcionando antes de criar seus próprios testes.

