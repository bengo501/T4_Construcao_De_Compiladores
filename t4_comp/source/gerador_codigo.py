#gerador de código 
# máquina de pilha
#implementa todas as funcionalidades 

# ============================== tabela de simbolos ==============================
class TabelaSimbolos:#tabela de símbolos para armazenar variáveis, structs e funções
    def __init__(self): #inicializa a tabela de simbolos
        self.simbolos = {} #dict para armazenar os simbolos
        self.contador_var = 0 #count para gerar novos rotulos para variaveis
        self.contador_rot = 0 #count para gerar novos rotulos para codigos

    def novo_rotulo_var(self):#gera novo rotulo para variaveis (V001, V002, ...)
        self.contador_var += 1
        return f"V{self.contador_var:03d}"

    def novo_rotulo_cod(self): #gera novo rotulo para codigos (R001, R002, ...)
        self.contador_rot += 1
        return f"R{self.contador_rot:03d}"

    def inserir(self, nome, tipo, rotulo=None, tamanho=4, offset=0, campos=None): #insere simbolo na tabela
        #campos: dict com campos de struct {nome_campo: (tipo, offset)}
        if rotulo is None:
            rotulo = self.novo_rotulo_var()
        
        self.simbolos[nome] = {
            'tipo': tipo, #tipo do simbolo
            'rotulo': rotulo, #rotulo do simbolo
            'tamanho': tamanho, #tamanho do simbolo
            'offset': offset, #offset do simbolo
            'campos': campos if campos else {} #campos do simbolo
        }
        return rotulo
        
    def buscar(self, nome): #busca simbolo na tabela
        return self.simbolos.get(nome)
 
    def buscar_campo(self, nome_struct, nome_campo): #busca campo de struct
        simbolo = self.buscar(nome_struct)
        if simbolo and simbolo['campos']:
            return simbolo['campos'].get(nome_campo)
        return None

#---------------------------------------------------------------------------------------------
# ============================== gerador de código ==============================
class GeradorCodigo: #gerador de código para máquina de pilha
    def __init__(self): #inicializa o gerador de código
        self.ts = TabelaSimbolos()
        self.codigo = []
        self.pilha_rotulos = []  # para controle de fluxo (if, while, for, etc)
        self.pilha_loops = []  # para break e continue
        self.contador_temp = 0

    def novo_temp(self): #gera novo rótulo temporário
        self.contador_temp += 1
        return f"_tmp{self.contador_temp}"

    def emitir(self, instrucao):#emite uma instrução de código
        self.codigo.append(instrucao)

    def emitir_rotulo(self, rotulo): #emite um rótulo
        self.codigo.append(f"{rotulo}: NOP")

    def get_codigo(self): #retorna o código gerado
        return "\n".join(self.codigo)

#---------------------------------------------------------------------------------------------
    # ============================== instruções básicas ==============================
    def ldc(self, valor):#empilha constante
        self.emitir(f"LDC {valor}")

    def lda(self, rotulo): #empilha conteúdo do endereço
        self.emitir(f"LDA {rotulo}")

    def sta(self, rotulo): #desempilha e armazena no endereço
        self.emitir(f"STA {rotulo}")

    def add(self): #desempilha RT1 e RT2, empilha RT2 + RT1
        self.emitir("ADD")

    def sub(self):#desempilha RT1 e RT2, empilha RT2 - RT1
        self.emitir("SUB")

    def mul(self):#desempilha RT1 e RT2, empilha RT2 * RT1
        self.emitir("MUL")

    def div(self): #desempilha RT1 e RT2, empilha RT2 / RT1
        self.emitir("DIV")

    def mod(self):#desempilha RT1 e RT2, empilha RT2 % RT1
        self.emitir("MOD")

    def neg(self):#desempilha RT1, empilha -RT1
        self.emitir("NEG")

    def dup(self): #duplica topo da pilha
        self.emitir("DUP")

    def drop(self):#desempilha uma palavra (descarta topo da pilha)
        self.emitir("DROP")

    def eq(self):  #desempilha RT1 e RT2, empilha 1 se RT2 == RT1, senão 0
        self.emitir("EQ")

    def ne(self): #desempilha RT1 e RT2, empilha 1 se RT2 != RT1, senão 0
        self.emitir("NE")

    def grt(self): #desempilha RT1 e RT2, empilha 1 se RT2 > RT1, senão 0
        self.emitir("GRT")  

    def les(self):  #desempilha RT1 e RT2, empilha 1 se RT2 < RT1, senão 0
        self.emitir("LES") 

    def geq(self):   #desempilha RT1 e RT2, empilha 1 se RT2 >= RT1, senão 0
        self.emitir("GEQ")

    def leq(self): #desempilha RT1 e RT2, empilha 1 se RT2 <= RT1, senão 0
        self.emitir("LEQ")

    def operador_ou_logico(self): #operador || (ou lógico)
        # espera na pilha: [exp1, exp2] com exp2 no topo
        # comportamento: se exp1 é verdadeiro, resultado é 1; senão, resultado é exp2
        # estratégia: salvar exp2, verificar exp1, decidir
        rotulo_ou_verdadeiro = self.ts.novo_rotulo_cod()
        rotulo_ou_fim = self.ts.novo_rotulo_cod()
        
        # na pilha: [exp1, exp2] com exp2 no topo
        # salva exp2 temporariamente
        temp_exp2 = self.novo_temp()
        self.sta(temp_exp2)  # salva exp2, agora pilha: [exp1]
        # verifica exp1
        self.dup()  # duplica exp1 para não perder
        # se exp1 é verdadeiro (não zero), resultado é 1
        self.jnz(rotulo_ou_verdadeiro)
        # exp1 é falso (zero), descarta exp1 e usa exp2
        self.drop()  # remove exp1
        self.lda(temp_exp2)  # carrega exp2
        self.jmp(rotulo_ou_fim)
        self.emitir_rotulo(rotulo_ou_verdadeiro)
        # exp1 é verdadeiro, descarta exp1 e empilha 1
        self.drop()  # remove exp1
        self.ldc(1)
        self.emitir_rotulo(rotulo_ou_fim)
    
    def operador_e_logico(self): #operador && (e lógico)
        # espera na pilha: [exp1, exp2] com exp2 no topo
        # comportamento: se exp1 é falso, resultado é 0; senão, resultado é exp2
        # estratégia: salvar exp2, verificar exp1, decidir
        rotulo_e_falso = self.ts.novo_rotulo_cod()
        rotulo_e_fim = self.ts.novo_rotulo_cod()
        
        # na pilha: [exp1, exp2] com exp2 no topo
        # salva exp2 temporariamente
        temp_exp2 = self.novo_temp()
        self.sta(temp_exp2)  # salva exp2, agora pilha: [exp1]
        # verifica exp1
        self.dup()  # duplica exp1 para não perder
        # se exp1 é falso (zero), resultado é 0
        self.jzer(rotulo_e_falso)
        # exp1 é verdadeiro (não zero), descarta exp1 e usa exp2
        self.drop()  # remove exp1
        self.lda(temp_exp2)  # carrega exp2
        self.jmp(rotulo_e_fim)
        self.emitir_rotulo(rotulo_e_falso)
        # exp1 é falso, descarta exp1 e empilha 0
        self.drop()  # remove exp1
        self.ldc(0)
        self.emitir_rotulo(rotulo_e_fim)

    def jmp(self, rotulo): #desvia para rótulo
        self.emitir(f"JMP {rotulo}") 

    def jzer(self, rotulo): #desempilha e, se zero, desvia para rótulo
        self.emitir(f"JZER {rotulo}") 

    def jnz(self, rotulo): #desempilha e, se não zero, desvia para rótulo
        self.emitir(f"JNZ {rotulo}")
#--------------------------------------------------------------------------
    # ========== declarações ==========
    def declarar_variavel(self, nome, tipo="integer", tamanho=4):#declara variável global
        rotulo = self.ts.inserir(nome, tipo, rotulo=f"_{nome}", tamanho=tamanho) #insere var na tabela de simbolos
        self.emitir(f"{rotulo} DS {tamanho}")        #aloca espaço na memória
        return rotulo 

    def declarar_struct(self, nome, campos):#declara struct
        #campos: lista de tuplas (nome_campo, tipo, tamanho)
        offset = 0
        campos_dict = {}
        tamanho_total = 0
        
        for nome_campo, tipo, tamanho in campos: # para cada campo
            campos_dict[nome_campo] = (tipo, offset) #adiciona campo à tabela de símbolos
            offset += tamanho #incrementa offset
            tamanho_total += tamanho #incrementa tamanho total
        
        rotulo = self.ts.inserir(nome, "struct", rotulo=f"_{nome}", #declara struct
                                 tamanho=tamanho_total, campos=campos_dict)
        return rotulo

    def declarar_variavel_struct(self, nome, tipo_struct):#declara variável do tipo struct
        struct_info = self.ts.buscar(tipo_struct) #busca info da struct
        if not struct_info:
            raise ValueError(f"struct {tipo_struct} não encontrada")
        
        tamanho = struct_info['tamanho']
        rotulo = self.ts.inserir(nome, tipo_struct, rotulo=f"_{nome}", tamanho=tamanho)
        self.emitir(f"{rotulo} DS {tamanho}")
        return rotulo

    def declarar_array(self, nome, tipo="integer", tamanho_elemento=4, tamanho_array=1):#declara array
        tamanho_total = tamanho_elemento * tamanho_array #calcula tamanho total do array
        rotulo = self.ts.inserir(nome, f"array[{tamanho_array}]", 
                                rotulo=f"_{nome}", tamanho=tamanho_total)
        self.emitir(f"{rotulo} DS {tamanho_total}")
        return rotulo

#--------------------------------------------------------------------------------
    # ============================== expressões ==============================
    def carregar_variavel(self, nome):#carrega variável na pilha
        simbolo = self.ts.buscar(nome)
        if not simbolo:
            raise ValueError(f"variável {nome} não encontrada")
        self.lda(simbolo['rotulo'])

    def carregar_campo_struct(self, nome_var, nome_campo):#carrega campo de struct na pilha
        simbolo = self.ts.buscar(nome_var)
        if not simbolo:
            raise ValueError(f"variável {nome_var} não encontrada")
        
        # busca a definição da struct para obter os campos
        tipo_struct = simbolo['tipo']
        struct_info = self.ts.buscar(tipo_struct)
        if not struct_info or not struct_info.get('campos'):
            raise ValueError(f"struct {tipo_struct} não encontrada ou sem campos")
        
        campo_info = struct_info['campos'].get(nome_campo)
        if not campo_info:
            raise ValueError(f"campo {nome_campo} não encontrado em {tipo_struct}")
        
        tipo_campo, offset = campo_info
        # carrega endereço base
        self.lda(simbolo['rotulo'])
        # adiciona offset (sempre, mesmo que seja 0 para consistência)
        self.ldc(offset)
        self.add()
        # carrega valor do campo via acesso indireto (LDI)
        # na pilha: [endereço] -> LDI -> [valor]
        self.emitir("LDI")

    def atribuir_variavel(self, nome):#atribui valor do topo da pilha à variável
        simbolo = self.ts.buscar(nome)
        if not simbolo:
            raise ValueError(f"variável {nome} não encontrada")
        self.sta(simbolo['rotulo'])

    def atribuir_campo_struct(self, nome_var, nome_campo):#atribui valor do topo da pilha ao campo de struct
        # espera na pilha: [valor]
        simbolo = self.ts.buscar(nome_var)
        if not simbolo:
            raise ValueError(f"variável {nome_var} não encontrada")
        
        # busca a definição da struct para obter os campos
        tipo_struct = simbolo['tipo']
        struct_info = self.ts.buscar(tipo_struct)
        if not struct_info or not struct_info.get('campos'):
            raise ValueError(f"struct {tipo_struct} não encontrada ou sem campos")
        
        campo_info = struct_info['campos'].get(nome_campo)
        if not campo_info:
            raise ValueError(f"campo {nome_campo} não encontrado em {tipo_struct}")
        
        tipo_campo, offset = campo_info
        # carrega endereço base
        self.lda(simbolo['rotulo'])
        # adiciona offset (sempre, mesmo que seja 0 para consistência)
        self.ldc(offset)
        self.add()
        # armazena valor no campo via acesso indireto (STI)
        # na pilha: [valor, endereço] -> STI -> []
        # STI desempilha RT1 (valor) e RT2 (endereço) e armazena RT1 no endereço RT2
        self.emitir("STI")

    def atribuir_array_elemento(self, nome_array):#atribui valor do topo da pilha ao elemento do array
        simbolo = self.ts.buscar(nome_array) #espera na pilha: [valor, índice]
        if not simbolo:
            raise ValueError(f"array {nome_array} não encontrado")
        temp_indice = self.novo_temp() # salva índice temporariamente
        self.sta(temp_indice) # salva índice
        temp_valor = self.novo_temp() # salva valor temporariamente
        self.sta(temp_valor) # salva valor
        self.lda(simbolo['rotulo']) # endereço base
        self.lda(temp_indice) # índice
        self.ldc(4) # assume inteiros de 4 bytes
        self.mul()
        self.add() # endereço calculado no topo
        self.lda(temp_valor) # valor
        self.emitir("STI") # armazena indiretamente

    def carregar_array_elemento(self, nome_array):#carrega elemento do array na pilha
        simbolo = self.ts.buscar(nome_array)#espera na pilha: [índice]
        if not simbolo:
            raise ValueError(f"array {nome_array} não encontrado")
        
        temp_indice = self.novo_temp() # salva índice temporariamente
        self.sta(temp_indice) # salva índice
        self.lda(simbolo['rotulo'])  # endereço base
        self.lda(temp_indice)  # índice
        self.ldc(4)  # assume inteiros de 4 bytes
        self.mul()
        self.add() # endereço calculado no topo
        self.emitir("LDI")  # carrega do endereço calculado

#----------------------------------------------------------------------------------------------   
    # ============================== arrays de structs ==============================
    def declarar_array_struct(self, nome, tipo_struct, tamanho_array):#declara array de structs
        struct_info = self.ts.buscar(tipo_struct)
        if not struct_info:
            raise ValueError(f"struct {tipo_struct} não encontrada")
        
        tamanho_struct = struct_info['tamanho']
        tamanho_total = tamanho_struct * tamanho_array
        rotulo = self.ts.inserir(nome, f"array[{tamanho_array}] of {tipo_struct}", 
                                rotulo=f"_{nome}", tamanho=tamanho_total)
        self.emitir(f"{rotulo} DS {tamanho_total}")
        return rotulo

    def atribuir_campo_struct_array(self, nome_array, nome_campo):#atribui valor do topo da pilha ao campo de struct no array
        simbolo = self.ts.buscar(nome_array)# espera na pilha: [valor, índice]
        if not simbolo:
            raise ValueError(f"array {nome_array} não encontrado")
        
        # obtém informações do tipo struct
        tipo_array = simbolo['tipo']
        if not tipo_array.startswith('array[') or ' of ' not in tipo_array:
            raise ValueError(f"{nome_array} não é um array de structs")
        
        tipo_struct = tipo_array.split(' of ')[1]
        struct_info = self.ts.buscar(tipo_struct)
        if not struct_info:
            raise ValueError(f"struct {tipo_struct} não encontrada")
        
        # obtém offset do campo
        campos = struct_info.get('campos', {})
        campo_info = campos.get(nome_campo)
        if not campo_info:
            raise ValueError(f"campo {nome_campo} não encontrado em {tipo_struct}")
        
        tipo_campo, offset_campo = campo_info
        tamanho_struct = struct_info['tamanho']
        
        temp_indice = self.novo_temp() # salva índice temporariamente
        self.sta(temp_indice) # salva índice
        temp_valor = self.novo_temp() # salva valor temporariamente
        self.sta(temp_valor) # salva valor
        # calcula endereço: base + indice * tamanho_struct + offset_campo
        self.lda(simbolo['rotulo'])  # endereço base do array
        self.lda(temp_indice)  # índice
        self.ldc(tamanho_struct)  # tamanho da struct
        self.mul()
        self.add()  # base + indice * tamanho_struct
        self.ldc(offset_campo)  # offset do campo
        self.add() # endereço calculado no topo
        self.lda(temp_valor)  # valor
        self.emitir("STI")  # armazena indiretamente
    
    def carregar_campo_struct_array(self, nome_array, nome_campo):   #carrega campo de struct no array na pilha
        #espera na pilha: [índice]
        simbolo = self.ts.buscar(nome_array)
        if not simbolo:
            raise ValueError(f"array {nome_array} não encontrado")
        
        # obtém informações do tipo struct
        tipo_array = simbolo['tipo']
        if not tipo_array.startswith('array[') or ' of ' not in tipo_array:
            raise ValueError(f"{nome_array} não é um array de structs")
        
        tipo_struct = tipo_array.split(' of ')[1]
        struct_info = self.ts.buscar(tipo_struct)
        if not struct_info:
            raise ValueError(f"struct {tipo_struct} não encontrada")
        
        # obtém offset do campo
        campos = struct_info.get('campos', {})
        campo_info = campos.get(nome_campo)
        if not campo_info:
            raise ValueError(f"campo {nome_campo} não encontrado em {tipo_struct}")
        
        tipo_campo, offset_campo = campo_info
        tamanho_struct = struct_info['tamanho']
        
        temp_indice = self.novo_temp() # salva índice temporariamente
        self.sta(temp_indice) # salva índice
        self.lda(simbolo['rotulo'])  # endereço base do array
        self.lda(temp_indice)  # índice
        self.ldc(tamanho_struct)  # tamanho da struct
        self.mul()
        self.add()  # base + indice * tamanho_struct
        self.ldc(offset_campo)  # offset do campo
        self.add()  # endereço calculado no topo
        
        # carrega valor indiretamente
        self.emitir("LDI")  # carrega do endereço calculado

#---------------------------------------------------------------------------------------------    
    # ============================== expressão de atribuição ==============================
    def expressao_atribuicao(self, nome):#transforma comando de atribuição em expressão de atribuição
        #atribui valor e mantém o valor no topo da pilha
        #valor já está no topo da pilha
        simbolo = self.ts.buscar(nome)
        if not simbolo:
            raise ValueError(f"variável {nome} não encontrada")
        
        self.emitir("DUP")  # duplica topo da pilha
        self.sta(simbolo['rotulo'])

#---------------------------------------------------------------------------------------------   
    # ============================== incremento/decremento ==============================
    def pre_incremento(self, nome): #pré-incremento: ++var
        self.carregar_variavel(nome)
        self.ldc(1)
        self.add()
        self.emitir("DUP")  # duplica para retornar valor
        self.atribuir_variavel(nome)
    
    def pos_incremento(self, nome):#pós-incremento: var++
        self.carregar_variavel(nome)
        self.emitir("DUP")  # duplica valor original
        self.ldc(1)
        self.add()
        self.atribuir_variavel(nome)
    
    def pre_decremento(self, nome):#pré-decremento: --var
        self.carregar_variavel(nome)
        self.ldc(1)
        self.sub()
        self.emitir("DUP")  # duplica para retornar valor
        self.atribuir_variavel(nome)
    
    def pos_decremento(self, nome):#pós-decremento: var--
        self.carregar_variavel(nome)
        self.emitir("DUP")  # duplica valor original
        self.ldc(1)
        self.sub()
        self.atribuir_variavel(nome) 

#--------------------------------------------------------------------------------------------- 
    # ============================== operador += ==============================
    def atribuicao_adicao(self, nome):#operador +=: var += exp
        self.carregar_variavel(nome)  # valor atual de var
        # expressão já está na pilha
        self.add()  # soma
        self.emitir("DUP")  # duplica para retornar valor
        self.atribuir_variavel(nome)

#--------------------------------------------------------------------------------------------- 
    # ============================== operador condicional ?: ==============================
    def operador_condicional(self, rotulo_else, rotulo_fim):#transforma operador condicional em expressão condicional
        #operador condicional: exp1 ? exp2 : exp3
        #exp1 (condição) já está na pilha
        # se condição for falsa, pula para exp3
        self.jzer(rotulo_else)
        # se verdadeira, executa exp2 e pula para fim
        # exp2 será gerada pelo chamador
        # depois de gerar exp2:
        self.jmp(rotulo_fim)
        self.emitir_rotulo(rotulo_else)
        # exp3 será gerada pelo chamador
        # depois de gerar exp3:
        # valor de exp2 ou exp3 fica no topo da pilha
        self.emitir_rotulo(rotulo_fim)

 #---------------------------------------------------------------------------------------------   
    # ============================== estruturas de controle ==============================
    def inicio_if(self):#início de if: cria rótulos
        rotulo_else = self.ts.novo_rotulo_cod() #gera novo rótulo para else
        rotulo_fim = self.ts.novo_rotulo_cod() #gera novo rótulo para fim
        self.pilha_rotulos.append((rotulo_else, rotulo_fim)) #add o rotulo de else e fim do loop na pilha de rotulos
        return rotulo_else, rotulo_fim
    
    def fim_if_then(self): #fim do bloco then
        rotulo_else, rotulo_fim = self.pilha_rotulos[-1]
        self.jmp(rotulo_fim)
        self.emitir_rotulo(rotulo_else)
    
    def fim_if(self): #fim de if
        rotulo_else, rotulo_fim = self.pilha_rotulos.pop()    #obtem o rotulo de else e fim do loop
        self.emitir_rotulo(rotulo_fim)
    
    def inicio_while(self):#início de while
        rotulo_inicio = self.ts.novo_rotulo_cod() #gera novo rótulo para início do loop
        rotulo_fim = self.ts.novo_rotulo_cod() #gera novo rótulo para fim do loop
        self.pilha_rotulos.append((rotulo_inicio, rotulo_fim)) #add o rotulo de início e fim do loop na pilha de rotulos
        self.pilha_loops.append((rotulo_inicio, rotulo_fim)) #add o rotulo de início e fim do loop na pilha de loops
        self.emitir_rotulo(rotulo_inicio)
        return rotulo_inicio, rotulo_fim
    
    def fim_while(self):        #fim de while
        rotulo_inicio, rotulo_fim = self.pilha_rotulos.pop()    #obtem o rotulo de início e fim do loop
        self.pilha_loops.pop()    #remove o rotulo de início e fim do loop da pilha de loops
        self.jmp(rotulo_inicio)    #pula para o rótulo de início
        self.emitir_rotulo(rotulo_fim)
    
    def inicio_do_while(self):    #inicio de do-while
        rotulo_inicio = self.ts.novo_rotulo_cod()    #gera novo rótulo para início do loop
        rotulo_fim = self.ts.novo_rotulo_cod()    #gera novo rótulo para fim do loop
        self.pilha_rotulos.append((rotulo_inicio, rotulo_fim))    #add o rotulo de início e fim do loop na pilha de rotulos
        self.pilha_loops.append((rotulo_inicio, rotulo_fim))    #add o rotulo de início e fim do loop na pilha de loops
        self.emitir_rotulo(rotulo_inicio) 
        return rotulo_inicio, rotulo_fim 
    
    def fim_do_while(self):#fim de do-while
        rotulo_inicio, rotulo_fim = self.pilha_rotulos.pop()#obtem o rotulo de início e fim do loop
        self.pilha_loops.pop()
        # condição já está na pilha
        self.jnz(rotulo_inicio)  # se verdadeira, volta ao início
        self.emitir_rotulo(rotulo_fim)
    
    def inicio_for(self, exp_inicial=None):#inicio de for
        rotulo_teste = self.ts.novo_rotulo_cod() #gera novo rotulo para teste
        rotulo_incremento = self.ts.novo_rotulo_cod() #gera novo rotulo para incremento
        rotulo_fim = self.ts.novo_rotulo_cod() #gera novo rotulo para fim
        self.pilha_rotulos.append((rotulo_teste, rotulo_incremento, rotulo_fim)) #add o rotulo de teste, incremento e fim do loop na pilha de rotulos
        self.pilha_loops.append((rotulo_teste, rotulo_fim)) #add o rotulo de teste e fim do loop na pilha de loops
        
        if exp_inicial:  # gera expressão inicial se houver
            pass
        
        self.jmp(rotulo_teste)  # pula para teste
        self.emitir_rotulo(rotulo_incremento)
        return rotulo_teste, rotulo_incremento, rotulo_fim
    
    def teste_for(self):#teste de for: expressão de teste já está na pilha
        rotulo_teste, rotulo_incremento, rotulo_fim = self.pilha_rotulos[-1]#obtem o rotulo de teste, incremento e fim do loop
        self.emitir_rotulo(rotulo_teste)
        self.jzer(rotulo_fim)  # se falso, sai do loop
    
    def incremento_for(self):#incremento de for: expressão de incremento já foi gerada
        rotulo_teste, rotulo_incremento, rotulo_fim = self.pilha_rotulos[-1]#obtem o rotulo de teste, incremento e fim do loop
        self.jmp(rotulo_incremento)  # volta para incremento
    
    def fim_for(self):#fim de for
        rotulo_teste, rotulo_incremento, rotulo_fim = self.pilha_rotulos.pop()#obtem o rotulo de teste, incremento e fim do loop
        self.pilha_loops.pop()#remove o rotulo de teste, incremento e fim do loop da pilha de loops
        self.jmp(rotulo_incremento)  # volta para incremento
        self.emitir_rotulo(rotulo_fim)
    
    def break_cmd(self):#comando break
        if not self.pilha_loops:
            raise ValueError("break fora de loop")
        rotulo_inicio, rotulo_fim = self.pilha_loops[-1]    #obtém o rótulo de início e fim do loop
        self.jmp(rotulo_fim)    #pula para o rótulo de fim
    
    def continue_cmd(self):#comando continue
        if not self.pilha_loops:    #verifica se está fora de loop
            raise ValueError("continue fora de loop")
        rotulo_inicio, rotulo_fim = self.pilha_loops[-1]
        
        # para for, precisa voltar para incremento
        if len(self.pilha_rotulos) > 0 and len(self.pilha_rotulos[-1]) == 3:
            rotulo_teste, rotulo_incremento, rotulo_fim = self.pilha_rotulos[-1]
            self.jmp(rotulo_incremento)
        else:
            # para while/do-while, volta para início
            rotulo_inicio, rotulo_fim = self.pilha_loops[-1]
            self.jmp(rotulo_inicio)
#---------------------------------------------------------------------------------------------   
    # ============================== início do programa ==============================
    def inicio_programa(self): #início do programa
        self.emitir("JMP _start")
    
    def fim_programa(self):#fim do programa
        self.emitir_rotulo("_start")
        self.emitir("HALT")

