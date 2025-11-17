# arquivos de teste individuais

cada funcionalidade agora tem um arquivo Python executável que gera código de teste.

## arquivos de teste

- `teste_01_expressao_atribuicao.py` - expressão de atribuição
- `teste_02_incremento_decremento.py` - incremento e decremento
- `teste_03_operador_mais_igual.py` - operador +=
- `teste_04_operador_condicional.py` - operador condicional ?:
- `teste_05_do_while.py` - comando do-while
- `teste_06_for.py` - comando for
- `teste_07_break_continue.py` - break e continue
- `teste_08_struct.py` - variáveis do tipo struct
- `teste_09_array_inteiros.py` - arrays de inteiros (bonus)
- `teste_10_struct_com_array.py` - struct com array (bonus)

## como usar

### executar um teste individual

```bash
python teste_01_expressao_atribuicao.py
```

cada arquivo exibe:
- descrição do teste
- exemplo de programa fonte
- código gerado

### executar todos os testes

```bash
python executar_todos_testes.py
```

este script executa todos os testes individuais em sequência.

### usar em seu próprio código

cada arquivo de teste exporta uma função `gerar_teste()` que retorna o código gerado:

```python
from teste_01_expressao_atribuicao import gerar_teste

codigo = gerar_teste()
print(codigo)
```

## estrutura de cada arquivo

cada arquivo de teste segue esta estrutura:

```python
from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para funcionalidade"""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # código de teste aqui
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("descrição do teste")
    print("programa fonte:")
    print("...")
    print("codigo gerado:")
    print(gerar_teste())
```

## diferença dos arquivos .txt

- arquivos `.txt`: documentação estática com exemplos
- arquivos `.py`: código executável que gera os testes dinamicamente

os arquivos `.py` são mais úteis porque:
- podem ser executados diretamente
- podem ser importados em outros scripts
- geram código atualizado automaticamente
- podem ser modificados facilmente

## vantagens

1. **executáveis**: podem ser executados diretamente
2. **reutilizáveis**: podem ser importados em outros scripts
3. **atualizáveis**: geram código atualizado automaticamente
4. **modificáveis**: fáceis de modificar para novos casos de teste

## exemplo de uso em script

```python
from teste_01_expressao_atribuicao import gerar_teste
from teste_02_incremento_decremento import gerar_teste as gerar_teste2

# gera código para expressão de atribuição
codigo1 = gerar_teste()
print("expressão de atribuição:")
print(codigo1)

# gera código para incremento/decremento
codigo2 = gerar_teste2()
print("incremento/decremento:")
print(codigo2)
```

