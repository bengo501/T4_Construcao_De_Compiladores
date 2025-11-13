# estrutura do projeto

## organização atual

```
t4_construcaoDeCompiladores/
├── src/                    # código fonte
│   └── gerador_codigo.py  # implementação principal
├── testes/                # testes automatizados
│   ├── testar.py          # testes automatizados completos
│   ├── executar_todos_testes.py  # executa todos os testes
│   └── teste_XX_*.py     # testes individuais (10 arquivos)
├── exemplos/              # exemplos de uso
│   ├── exemplo_uso.py     # exemplos detalhados
│   ├── exemplos_teste.py  # funções de teste
│   └── main.py            # demonstração completa
├── docs/                  # documentação
│   ├── COMO_TESTAR.md     # guia de testes
│   ├── TESTE_RAPIDO.md    # guia rápido
│   ├── README_TESTES.md   # documentação dos testes
│   └── teste_XX_*.txt     # exemplos documentados (10 arquivos)
├── output/                # saída gerada (opcional)
├── README.md              # documentação principal
├── COMANDOS.md            # todos os comandos para executar
└── enunciadoT4.txt        # enunciado da tarefa
```

## comandos principais

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

### executar todos os testes individuais

```bash
python testes/executar_todos_testes.py
```

## como usar os módulos

### importar o gerador

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from gerador_codigo import GeradorCodigo
```

### importar testes individuais

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'testes'))
from teste_01_expressao_atribuicao import gerar_teste
```

## notas

- todos os arquivos de teste já têm os imports configurados corretamente
- os arquivos estão organizados em pastas por tipo
- a documentação está na pasta `docs/`
- os exemplos estão na pasta `exemplos/`
- os testes estão na pasta `testes/`
- o código fonte está na pasta `src/`

