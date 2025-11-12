# visão geral

este projeto implementa a geração de código para uma máquina de pilha, cobrindo todas as funcionalidades obrigatórias e bônus listadas no enunciado da tarefa 4. abaixo estão os comandos recomendados para validar o trabalho, a função de cada script core e uma justificativa de conformidade com cada requisito.

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

assim, os scripts acima e a cobertura de funcionalidades demonstram que o projeto está alinhado ao enunciado da tarefa 4.***

