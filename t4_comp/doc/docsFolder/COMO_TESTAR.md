# como testar o funcionamento da implementação

este documento explica como testar todas as funcionalidades implementadas.

## método 1: executar todos os testes de uma vez

### usando o script de teste completo

```bash
python testar.py
```

este script executa todos os testes e verifica se cada funcionalidade está funcionando corretamente.

### usando o arquivo principal

```bash
python main.py
```

este arquivo demonstra todas as funcionalidades gerando código de exemplo para cada uma.

## método 2: executar testes individuais

### usando o arquivo de exemplos

```bash
python exemplos_teste.py
```

este arquivo contém funções de teste individuais que você pode executar separadamente.

### testar uma funcionalidade específica

você pode modificar o arquivo `exemplos_teste.py` para executar apenas uma função:

```python
from exemplos_teste import teste_01_expressao_atribuicao

print(teste_01_expressao_atribuicao())
```

## método 3: criar seus próprios testes

### exemplo básico

```python
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

### exemplo com loop

```python
from gerador_codigo import GeradorCodigo

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

print(gc.get_codigo())
```

## método 4: verificar arquivos de teste

cada funcionalidade tem um arquivo de teste documentado:

- `teste_01_expressao_atribuicao.txt` - expressão de atribuição
- `teste_02_incremento_decremento.txt` - incremento/decremento
- `teste_03_operador_mais_igual.txt` - operador +=
- `teste_04_operador_condicional.txt` - operador condicional ?:
- `teste_05_do_while.txt` - comando do-while
- `teste_06_for.txt` - comando for
- `teste_07_break_continue.txt` - break e continue
- `teste_08_struct.txt` - variáveis do tipo struct
- `teste_09_array_inteiros.txt` - arrays de inteiros (bonus)
- `teste_10_struct_com_array.txt` - struct com array (bonus)

esses arquivos contêm exemplos de código fonte e o código gerado esperado.

## verificações que você deve fazer

### 1. verificar se o código é gerado corretamente

execute os testes e verifique se:
- o código gerado contém as instruções esperadas
- os rótulos são gerados corretamente
- as variáveis são declaradas corretamente

### 2. verificar se todas as funcionalidades estão implementadas

use o script `testar.py` que verifica automaticamente:
- expressão de atribuição
- incremento/decremento
- operador +=
- operador condicional ?:
- do-while
- for
- break e continue
- struct
- arrays
- struct com array

### 3. verificar se o código gerado faz sentido

compare o código gerado com os exemplos nos arquivos `.txt` de teste.

## problemas comuns

### erro: "variável não encontrada"

certifique-se de declarar a variável antes de usá-la:

```python
gc.declarar_variavel("x", "integer", 4)  # declara antes
gc.carregar_variavel("x")  # agora pode usar
```

### erro: "break/continue fora de loop"

certifique-se de usar break/continue apenas dentro de loops:

```python
rotulo_inicio, rotulo_fim = gc.inicio_while()  # inicia loop
# ... código do loop ...
gc.break_cmd()  # agora pode usar break
gc.fim_while()  # finaliza loop
```

### código gerado não está correto

verifique a ordem das instruções:
1. início do programa
2. declarações de variáveis
3. código do programa
4. fim do programa

## saída esperada

quando executar `python testar.py`, você deve ver algo como:

```
============================================================
executando testes do gerador de código
============================================================

testando: expressão de atribuição
  ✓ expressão de atribuição: ok

testando: incremento e decremento
  ✓ incremento/decremento: ok

...

============================================================
resumo dos testes
============================================================
testes passaram: 10/10
testes falharam: 0/10

✓ todos os testes passaram!
```

## dicas

1. execute `python testar.py` primeiro para verificar se tudo está funcionando
2. depois execute `python main.py` para ver exemplos completos de código gerado
3. consulte os arquivos `teste_*.txt` para ver exemplos documentados
4. crie seus próprios testes para casos específicos que você precisa

