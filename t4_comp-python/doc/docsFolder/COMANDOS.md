# comandos para executar o projeto

este documento contém todos os comandos necessários para executar o gerador de código e seus testes.

## estrutura do projeto

```
t4_construcaoDeCompiladores/
├── src/                    # código fonte
│   └── gerador_codigo.py  # implementação principal
├── testes/                # testes automatizados
│   ├── testar.py          # testes automatizados completos
│   ├── executar_todos_testes.py  # executa todos os testes
│   └── teste_XX_*.py      # testes individuais (10 arquivos)
├── exemplos/              # exemplos de uso
│   ├── exemplo_uso.py     # exemplos detalhados
│   ├── exemplos_teste.py  # funções de teste
│   └── main.py            # demonstração completa
├── docs/                  # documentação
│   ├── COMO_TESTAR.md     # guia de testes
│   ├── TESTE_RAPIDO.md    # guia rápido
│   ├── README_TESTES.md    # documentação dos testes
│   └── teste_XX_*.txt     # exemplos documentados (10 arquivos)
├── output/                # saída gerada (opcional)
├── README.md              # documentação principal
├── COMANDOS.md            # este arquivo
├── ESTRUTURA.md           # estrutura do projeto
└── enunciadoT4.txt        # enunciado da tarefa
```

**nota:** alguns arquivos podem estar tanto nas pastas quanto na raiz. os comandos abaixo funcionam em ambos os casos.

## comandos básicos

### executar testes automatizados

se o arquivo estiver em `testes/`:
```bash
python testes/testar.py
```

se o arquivo estiver na raiz:
```bash
python testar.py
```

ou use:
```bash
python -c "import sys; sys.path.insert(0, 'src' if __import__('os').path.exists('src/gerador_codigo.py') else '.'); exec(open('testes/testar.py' if __import__('os').path.exists('testes/testar.py') else 'testar.py').read())"
```

### ver demonstração completa

se o arquivo estiver em `exemplos/`:
```bash
python exemplos/main.py
```

se o arquivo estiver na raiz:
```bash
python main.py
```

### executar um teste específico

se o arquivo estiver em `testes/`:
```bash
python testes/teste_01_expressao_atribuicao.py
```

se o arquivo estiver na raiz:
```bash
python teste_01_expressao_atribuicao.py
```

## comandos para testes individuais

### teste 1: expressão de atribuição

```bash
python testes/teste_01_expressao_atribuicao.py
# ou
python teste_01_expressao_atribuicao.py
```

### teste 2: incremento e decremento

```bash
python testes/teste_02_incremento_decremento.py
# ou
python teste_02_incremento_decremento.py
```

### teste 3: operador +=

```bash
python testes/teste_03_operador_mais_igual.py
# ou
python teste_03_operador_mais_igual.py
```

### teste 4: operador condicional ?:

```bash
python testes/teste_04_operador_condicional.py
# ou
python teste_04_operador_condicional.py
```

### teste 5: comando do-while

```bash
python testes/teste_05_do_while.py
# ou
python teste_05_do_while.py
```

### teste 6: comando for

```bash
python testes/teste_06_for.py
# ou
python teste_06_for.py
```

### teste 7: break e continue

```bash
python testes/teste_07_break_continue.py
# ou
python teste_07_break_continue.py
```

### teste 8: variáveis do tipo struct

```bash
python testes/teste_08_struct.py
# ou
python teste_08_struct.py
```

### teste 9: arrays de inteiros (bonus)

```bash
python testes/teste_09_array_inteiros.py
# ou
python teste_09_array_inteiros.py
```

### teste 10: struct com array (bonus)

```bash
python testes/teste_10_struct_com_array.py
# ou
python teste_10_struct_com_array.py
```

## comandos para usar em seu próprio código

### importar o gerador

```python
import sys
import os

# ajusta o path dependendo de onde está o arquivo
if os.path.exists('src/gerador_codigo.py'):
    sys.path.insert(0, 'src')
elif os.path.exists('../src/gerador_codigo.py'):
    sys.path.insert(0, '../src')
else:
    sys.path.insert(0, '.')

from gerador_codigo import GeradorCodigo

gc = GeradorCodigo()
gc.inicio_programa()

# seu código aqui

gc.fim_programa()
print(gc.get_codigo())
```

### importar testes individuais

```python
import sys
import os

# ajusta o path dependendo de onde está o arquivo
if os.path.exists('testes/teste_01_expressao_atribuicao.py'):
    sys.path.insert(0, 'testes')
elif os.path.exists('../testes/teste_01_expressao_atribuicao.py'):
    sys.path.insert(0, '../testes')
else:
    sys.path.insert(0, '.')

from teste_01_expressao_atribuicao import gerar_teste

codigo = gerar_teste()
print(codigo)
```

## comandos úteis

### executar todos os testes individuais

```bash
python testes/executar_todos_testes.py
# ou
python executar_todos_testes.py
```

### salvar código gerado em arquivo

```bash
python exemplos/main.py > output/codigo_gerado.txt
# ou
python main.py > output/codigo_gerado.txt
```

### verificar estrutura de pastas

**windows (powershell):**
```powershell
tree /F
```

**linux/mac:**
```bash
tree
```

## comandos por categoria

### verificação rápida

```bash
# executar testes automatizados
python testes/testar.py  # ou python testar.py

# ver demonstração completa
python exemplos/main.py  # ou python main.py
```

### desenvolvimento

```bash
# executar um teste específico
python testes/teste_01_expressao_atribuicao.py  # ou python teste_01_expressao_atribuicao.py

# executar todos os testes individuais
python testes/executar_todos_testes.py  # ou python executar_todos_testes.py
```

### documentação

```bash
# ver documentação principal
cat README.md  # ou type README.md (windows)

# ver guia de testes
cat docs/COMO_TESTAR.md  # ou type docs\COMO_TESTAR.md (windows)

# ver guia rápido
cat docs/TESTE_RAPIDO.md  # ou type docs\TESTE_RAPIDO.md (windows)
```

## resumo de comandos principais

| comando | descrição |
|---------|-----------|
| `python testes/testar.py` ou `python testar.py` | executa todos os testes automatizados |
| `python exemplos/main.py` ou `python main.py` | demonstração completa de todas as funcionalidades |
| `python testes/teste_XX_*.py` ou `python teste_XX_*.py` | executa um teste específico |
| `python exemplos/exemplo_uso.py` ou `python exemplo_uso.py` | exemplos detalhados de uso |

## dicas

1. **comece sempre com**: `python testes/testar.py` ou `python testar.py` para verificar se tudo está funcionando
2. **use exemplos**: `python exemplos/main.py` ou `python main.py` para ver exemplos completos
3. **teste individualmente**: use `python testes/teste_XX_*.py` ou `python teste_XX_*.py` para testar funcionalidades específicas
4. **consulte documentação**: veja os arquivos em `docs/` ou na raiz para mais informações

## troubleshooting

### erro: "módulo não encontrado"

certifique-se de ajustar o path corretamente:

```python
import sys
import os

# verifica onde está o arquivo
if os.path.exists('src/gerador_codigo.py'):
    sys.path.insert(0, 'src')
elif os.path.exists('../src/gerador_codigo.py'):
    sys.path.insert(0, '../src')
else:
    sys.path.insert(0, '.')
```

### erro: "arquivo não encontrado"

certifique-se de estar executando o comando do diretório raiz do projeto.

### erro de encoding

os arquivos estão configurados para utf-8. se houver problemas, use:

```bash
python -X utf8 testes/testar.py
```
