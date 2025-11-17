%{
  import java.io.*;
  import java.util.ArrayList;
  import java.util.Stack;
  import java.util.Map;
  import java.util.HashMap;
%}
 

%token ID, INT, FLOAT, BOOL, NUM, LIT, VOID, MAIN, READ, WRITE, IF, ELSE
%token WHILE,TRUE, FALSE, IF, ELSE
%token EQ, LEQ, GEQ, NEQ 
%token AND, OR

%token INC, DEC, MAIS_IGUAL, INTERROGACAO, DOIS_PONTOS
%token DO, FOR, BREAK, CONTINUE, STRUCT

%right '=' MAIS_IGUAL
%right '?' ':'  
%left OR
%left AND
%left  '>' '<' EQ LEQ GEQ NEQ
%left '+' '-'
%left '*' '/' '%'
%right '!' INC DEC

%type <sval> ID
%type <sval> LIT
%type <sval> NUM
%type <ival> type

/* Tipos para as novas regras de struct */
%type <obj> l_campos
%type <obj> campo


%%

prog : { geraInicio(); } dList mainF { geraAreaDados(); geraAreaLiterais(); } ;

mainF : VOID MAIN '(' ')'   { System.out.println("_start:"); }
        '{' lcmd  { geraFinal(); } '}'
         ; 

dList : decl dList | ;

type : INT    { $$ = INT; }
     | FLOAT  { $$ = FLOAT; }
     | BOOL   { $$ = BOOL; }
     ;

campo : type ID ';' {
            /* campo simples (int x) */
            $$ = new TS_entry($2, $1, 0); 
        }
      | type ID '[' NUM ']' ';' {
            /* campo array - (int notas[4]) */
            int n_elem = Integer.parseInt($4);
            $$ = new TS_entry($2, $1, 0, n_elem);
        }
      ;

l_campos : l_campos campo
           {
               Map<String, TS_entry> campos = (Map<String, TS_entry>)$1;
               TS_entry novo_campo = (TS_entry)$2;

               if (campos.containsKey(novo_campo.id)) {
                   yyerror("(sem) campo >" + novo_campo.id + "< duplicado no struct");
               } else {
                   int offset = 0;
                   for (TS_entry c : campos.values()) {
                       offset += c.getTamanho();
                   }
                   novo_campo.offset = offset;
                   campos.put(novo_campo.id, novo_campo);
               }
               $$ = $1; /* Retorna o HashMap atualizado */
           }
         | { 
               $$ = new HashMap<String, TS_entry>(); 
           }
         ;
decl : 
      type ID ';' {
           if (ts.pesquisa($2) != null) {
               yyerror("(sem) variavel >" + $2 + "< jah declarada");
           } else {
               ts.insert(new TS_entry($2, $1));
           }
      }
/* Declaração de Array (ex: int v[10];) */
      | type ID '[' NUM ']' ';' {
           String id_var = $2;
           int tipo_base = $1;
           int n_elem = Integer.parseInt($4);
           
           if (ts.pesquisa(id_var) != null) {
               yyerror("(sem) variavel >" + id_var + "< jah declarada");
           } else {
               /* Construtor de array simples: (id, nElem, tipoBase, tipoStruct, tamanhoElem) */
               ts.insert(new TS_entry(id_var, n_elem, tipo_base, null, 4));
           }
       }
     /* * BÔNUS (Req 10): Declaração de Array de Struct (ex: Ponto p[10];) */
      | ID ID '[' NUM ']' ';' {
           String id_tipo = $1;
           String id_var = $2;
           int n_elem = Integer.parseInt($4);
           
           TS_entry nodo_tipo = ts.pesquisaTipo(id_tipo);
           if (nodo_tipo == null) yyerror("(sem) tipo >" + id_tipo + "< nao conhecido");
           
           if (ts.pesquisa(id_var) != null) {
               yyerror("(sem) variavel >" + id_var + "< jah declarada");
           } else {
               /* Construtor de array de struct: (id, nElem, tipoBase, tipoStruct, tamanhoElem) */
               ts.insert(new TS_entry(id_var, n_elem, Parser.STRUCT, id_tipo, nodo_tipo.getTamanho()));
             }
         }
      ;
      | STRUCT ID '{' l_campos '}' ';' {
           /* Caso 2: Definição de tipo struct (struct Ponto { ... };) */
           Map<String, TS_entry> campos = (Map<String, TS_entry>)$4;
           int tamanho_total = 0;
           for (TS_entry campo : campos.values()) {
               tamanho_total += campo.getTamanho();
           }
           
           if (ts.pesquisaTipo($2) != null) {
               yyerror("(sem) tipo struct >" + $2 + "< jah declarado");
           } else {
               ts.insert_tipo(new TS_entry($2, tamanho_total, campos));
           }
       }
      | ID ID ';' {
            /* Variável struct (Ponto p1;) */
            String id_tipo = $1;
            String id_var = $2;
            
            TS_entry nodo_tipo = ts.pesquisaTipo(id_tipo);
            TS_entry nodo_var = ts.pesquisa(id_var);
            
            if (nodo_var != null) {
                yyerror("(sem) variavel >" + id_var + "< jah declarada");
            } else if (nodo_tipo == null) {
                yyerror("(sem) tipo >" + id_tipo + "< nao conhecido");
            } else {
              ts.insert(new TS_entry(id_var, nodo_tipo));          }
       }
     ;


lcmd : lcmd cmd
	   |
	   ;
	   
cmd :  
	exp ';'

		| '{' lcmd '}' { System.out.println("\t\t# terminou o bloco..."); }
					     
					       
      	| WRITE '(' LIT ')' ';' { strTab.add($3);
                                System.out.println("\tMOVL $_str_"+strCount+"Len, %EDX"); 
				System.out.println("\tMOVL $_str_"+strCount+", %ECX"); 
                                System.out.println("\tCALL _writeLit"); 
				System.out.println("\tCALL _writeln"); 
                                strCount++;
				}
      
	  	| WRITE '(' LIT 
                              { strTab.add($3);
                                System.out.println("\tMOVL $_str_"+strCount+"Len, %EDX"); 
				System.out.println("\tMOVL $_str_"+strCount+", %ECX"); 
                                System.out.println("\tCALL _writeLit"); 
				strCount++;
				}

                    ',' exp ')' ';' 
			{ 
			 System.out.println("\tPOPL %EAX"); 
			 System.out.println("\tCALL _write");	
			 System.out.println("\tCALL _writeln"); 
                        }
         
     	| READ '(' ref ')' ';' {
           /* 'ref' ($3) já empilhou o endereço correto */
           System.out.println("\tCALL _read");
           System.out.println("\tPOPL %EDX");
           System.out.println("\tMOVL %EAX, (%EDX)");
       }
         
    | WHILE {
				pRot.push(proxRot);  proxRot += 2;
				int rot_inicio = pRot.peek();
				int rot_fim = rot_inicio + 1;
				
				pLoopBreak.push(rot_fim);
				pLoopContinue.push(rot_inicio);
				
				System.out.printf("rot_%02d:\n", rot_inicio);
			} 

			'(' exp ')' {
					System.out.println("\tPOPL %EAX   # desvia se falso...");
					System.out.println("\tCMPL $0, %EAX");
					System.out.printf("\tJE rot_%02d\n", (int)pRot.peek()+1); // Pula para rot_fim
			} 
			cmd	{
				/* Fim do corpo */
				System.out.printf("\tJMP rot_%02d\n", pRot.peek()); // Pula para rot_inicio
				System.out.printf("rot_%02d:\n",(int)pRot.peek()+1); // Define rot_fim
				
				/* Limpa pilhas */
				pRot.pop();
				pLoopBreak.pop();
				pLoopContinue.pop();
			}

    | DO {
				/* Prepara rótulos de início (continue) e fim (break) */
				int rot_inicio = proxRot;
				int rot_fim = proxRot + 1;
				proxRot += 2;
				
				pRot.push(rot_inicio); // Salva rótulo de início para o JNE
				
				/* Salva rótulos para break/continue */
				pLoopBreak.push(rot_fim);
				pLoopContinue.push(rot_inicio);
				
				System.out.printf("rot_%02d:\n", rot_inicio);
			}

			cmd WHILE '(' exp ')' ';' {
				/* Teste da condição */
				System.out.println("\tPOPL %EAX");
				System.out.println("\tCMPL $0, %EAX");
				System.out.printf("\tJNE rot_%02d\n", pRot.pop()); // Pula para rot_inicio se V
				
				/* Define rótulo de fim (break) e limpa pilhas */
				System.out.printf("rot_%02d:\n", pLoopBreak.pop());
				pLoopContinue.pop();
			}

    | BREAK ';' {
				if (pLoopBreak.empty())
					yyerror("(sem) comando break fora de loop");
				else
					System.out.printf("\tJMP rot_%02d\n", pLoopBreak.peek());
			}

    | CONTINUE ';' {
				if (pLoopContinue.empty())
					yyerror("(sem) comando continue fora de loop");
				else
					System.out.printf("\tJMP rot_%02d\n", pLoopContinue.peek());
			}

    | FOR '(' opt_exp ';' {
            /* Ação 1: exp1 (init) - Define rótulos */
            int rot_teste = proxRot;
            int rot_corpo = proxRot + 1; // Rótulo do corpo
            int rot_continue = proxRot + 2; 
            int rot_fim = proxRot + 3;
            proxRot += 4; 
            
            pLoopBreak.push(rot_fim);
            pLoopContinue.push(rot_continue); 
            
            pRot.push(rot_teste);    
            pRot.push(rot_corpo);    
            pRot.push(rot_continue); 
            pRot.push(rot_fim);      
            
            System.out.printf("\tJMP rot_%02d\n", rot_teste); // 1. Vai para o teste inicial
        }
          for_cond_opt ';' {
            /* Ação 2: Após exp2 (test) - Testa a condição */
            
            int rot_teste = (int)pRot.get(pRot.size()-4);
            int rot_corpo = (int)pRot.get(pRot.size()-3);
            int rot_fim = (int)pRot.get(pRot.size()-1); 
            
            System.out.printf("rot_%02d:\n", rot_teste); // 2. Define rot_teste
            System.out.println("\tPOPL %EAX");
            System.out.println("\tCMPL $0, %EAX");
            
            // **CORREÇÃO CRÍTICA**: Inverte a lógica. Pula para o FIM se FALSO.
            System.out.printf("\tJE rot_%02d\n", rot_fim); // 3. JMP para rot_fim (se FALSO)
            
            System.out.printf("rot_%02d:\n", rot_corpo); // 4. Define rot_corpo (se verdadeiro, cai aqui)
            // REMOVIDO: JMP para rot_corpo, pois o fluxo já cai naturalmente.
          }
          opt_exp ')' {
            /* Ação 3: Após exp3 (incremento) */
            int rot_teste = (int)pRot.get(pRot.size()-4);
            int rot_continue = (int)pRot.get(pRot.size()-2);

            System.out.printf("rot_%02d:\n", rot_continue); // 5. Define rot_continue (Incremento)
            System.out.printf("\tJMP rot_%02d\n", rot_teste); // 6. Pula para rot_teste
          }
          cmd {
            /* Ação 4: Após o corpo (cmd) - Loop e Finalização */
            int rot_teste = pRot.pop();  
            int rot_corpo = pRot.pop();  
            int rot_continue = pRot.pop(); 
            int rot_fim = pRot.pop();    
            
            pLoopBreak.pop();
            pLoopContinue.pop();
            
            // Note que rot_corpo já foi definido na Ação 2
            System.out.printf("\tJMP rot_%02d\n", rot_continue); // 7. Volta para o incremento
            System.out.printf("rot_%02d:\n", rot_fim); // 8. Define rótulo do fim (saída do loop)
          }
							
    | IF '(' exp {	
				pRot.push(proxRot);  proxRot += 2;
								
				System.out.println("\tPOPL %EAX");
				System.out.println("\tCMPL $0, %EAX");
				System.out.printf("\tJE rot_%02d\n", pRot.peek());
			}
			')' cmd 

            restoIf {
				System.out.printf("rot_%02d:\n",pRot.peek()+1);
				pRot.pop();
			}
     
     
     
restoIf : ELSE  {
					System.out.printf("\tJMP rot_%02d\n", pRot.peek()+1);
					System.out.printf("rot_%02d:\n",pRot.peek());
		} 	
		cmd  
							
							
		| {
		    System.out.printf("\tJMP rot_%02d\n", pRot.peek()+1);
				System.out.printf("rot_%02d:\n",pRot.peek());
				} 
		;										


exp :  NUM  { System.out.println("\tPUSHL $"+$1); } 
    |  TRUE  { System.out.println("\tPUSHL $1"); } 
    |  FALSE  { System.out.println("\tPUSHL $0"); }      
 		| ref  { 
           System.out.println("\tPOPL %EAX");     // Pega o endereço
           System.out.println("\tMOVL (%EAX), %EAX"); // Carrega o valor do endereço
           System.out.println("\tPUSHL %EAX");    // Empilha o valor
       }
    | '(' exp	')' 
    | '!' exp       { gcExpNot(); }

    /* ** CORREÇÃO: Usa 'ref' para endereço e implementa += ** */
    | ref MAIS_IGUAL exp { /* ref empilhou endereço; exp empilhou valor */
          System.out.println("\tPOPL %EAX");     /* EAX = Valor da exp (direita) */
          System.out.println("\tPOPL %EDX");     /* EDX = Endereço da ref (esquerda) */
          
          System.out.println("\tMOVL (%EDX), %EBX"); /* EBX = Valor da ref (lê o valor no endereço) */
          System.out.println("\tADDL %EAX, %EBX");   /* EBX = Valor da ref + Valor da exp */
          
          System.out.println("\tMOVL %EBX, (%EDX)"); /* Salva o novo valor no endereço */
          System.out.println("\tPUSHL %EBX");    /* PUSH O NOVO VALOR para encadear */
        }

    | ref '=' exp %prec AND {
         System.out.println("\tPOPL %EAX");     // Valor (da exp)
         System.out.println("\tPOPL %EDX");     // Endereço (da ref)
         System.out.println("\tMOVL %EAX, (%EDX)"); // Salva Valor no Endereço
         System.out.println("\tPUSHL %EAX");    // Empurra o valor de volta
     }
 
    /* ** CORREÇÃO: Pré-Incremento (++ref) ** */
    | INC ref {
        System.out.println("\tPOPL %EAX");      /* EAX = Endereço da ref */
        System.out.println("\tMOVL (%EAX), %EBX"); /* EBX = Valor atual */
        System.out.println("\tADDL $1, %EBX");     /* EBX = Valor + 1 (Incrementa) */
        System.out.println("\tMOVL %EBX, (%EAX)"); /* Salva o novo valor no endereço */
        System.out.println("\tPUSHL %EBX");     /* PUSHL o NOVO valor */
    }
 
    /* ** CORREÇÃO: Pós-Incremento (ref++) ** */
    | ref INC {
        System.out.println("\tPOPL %EAX");      /* EAX = Endereço da ref */
        System.out.println("\tMOVL (%EAX), %EBX"); /* EBX = Valor atual */
        System.out.println("\tPUSHL %EBX");     /* PUSHL o VALOR ANTIGO */
        System.out.println("\tADDL $1, %EBX");     /* EBX = Valor + 1 (Incrementa) */
        System.out.println("\tMOVL %EBX, (%EAX)"); /* Salva o novo valor no endereço */
    }
 
    /* ** CORREÇÃO: Pré-Decremento (--ref) ** */
    | DEC ref {
        System.out.println("\tPOPL %EAX");      /* EAX = Endereço da ref */
        System.out.println("\tMOVL (%EAX), %EBX"); /* EBX = Valor atual */
        System.out.println("\tSUBL $1, %EBX");     /* EBX = Valor - 1 (Decrementa) */
        System.out.println("\tMOVL %EBX, (%EAX)"); /* Salva o novo valor no endereço */
        System.out.println("\tPUSHL %EBX");     /* PUSHL o NOVO valor */
    }
 
    /* ** CORREÇÃO: Pós-Decremento (ref--) ** */
    | ref DEC {
        System.out.println("\tPOPL %EAX");      /* EAX = Endereço da ref */
        System.out.println("\tMOVL (%EAX), %EBX"); /* EBX = Valor atual */
        System.out.println("\tPUSHL %EBX");     /* PUSHL o VALOR ANTIGO */
        System.out.println("\tSUBL $1, %EBX");     /* EBX = Valor - 1 (Decrementa) */
        System.out.println("\tMOVL %EBX, (%EAX)"); /* Salva o novo valor no endereço */
    }

		| exp '+' exp		{ gcExpArit('+'); }
		| exp '-' exp		{ gcExpArit('-'); }
		| exp '*' exp		{ gcExpArit('*'); }
		| exp '/' exp		{ gcExpArit('/'); }
		| exp '%' exp		{ gcExpArit('%'); }
																			
		| exp '>' exp		{ gcExpRel('>'); }
		| exp '<' exp		{ gcExpRel('<'); }											
		| exp EQ exp		{ gcExpRel(EQ); }											
		| exp LEQ exp		{ gcExpRel(LEQ); }											
		| exp GEQ exp		{ gcExpRel(GEQ); }											
		| exp NEQ exp		{ gcExpRel(NEQ); }											
												
		| exp OR exp		{ gcExpLog(OR); }											
		| exp AND exp		{ gcExpLog(AND); }											

	/* ** CORREÇÃO: Usa tokens e lógica correta ** */
	| exp INTERROGACAO { 
      pRot.push(proxRot); proxRot += 2; 
      System.out.println("\tPOPL %EAX");
      System.out.println("\tCMPL $0, %EAX");
      System.out.printf("\tJE rot_%02d\n", pRot.peek()); 
    }
    exp DOIS_PONTOS {
        /* Ação 2: Após bloco verdadeiro (exp_2) */
        
        // Empurra o resultado de exp_2 (já está na pilha, mas garante que EAX/EBX não contaminem)
        System.out.println("\tPOPL %EAX"); // Pega o resultado de exp_2
        System.out.println("\tPUSHL %EAX"); // Empilha de volta
        
        System.out.printf("\tJMP rot_%02d\n", pRot.peek()+1); // Pula para R_fim
        System.out.printf("rot_%02d:\n", pRot.peek()); // Define R_else
    }
    exp           { /* Ação FINAL (exp_3) */
        /* Note: exp_3 está na pilha */
        System.out.printf("rot_%02d:\n", pRot.peek()+1); // Define R_fim
        pRot.pop(); 
    }
	;


opt_exp : exp
        | /* Vazio */
        ;	

/* * NOVA REGRA (Req 8 & 9): 'ref' (Referência)
 * Trata acesso a ID simples, ID.ID (struct) e ID[exp] (array)
 * Esta regra deixa o ENDEREÇO do dado na pilha.
 */
ref : ID {
          /* Var simples. Empilha o endereço. */
          TS_entry nodo = ts.pesquisa($1);
          if (nodo == null) yyerror("(sem) variavel >" + $1 + "< nao declarada");
          System.out.println("\tPUSHL $_" + $1);
      }
    | ID '.' ID {
          /* Campo de struct (ex: p1.x) */
          String id_var = $1;
          String id_campo = $3;
          
          TS_entry nodo_var = ts.pesquisa(id_var);
          if (nodo_var == null) yyerror("(sem) variavel >" + id_var + "< nao declarada");
          
          TS_entry nodo_tipo = ts.pesquisaTipo(nodo_var.getTipoStruct());
          if (nodo_tipo == null) yyerror("(sem) tipo >" + nodo_var.getTipoStruct() + "< nao eh um struct");
          
          TS_entry nodo_campo = nodo_tipo.getCampo(id_campo);
          if (nodo_campo == null) yyerror("(sem) campo >" + id_campo + "< nao existe no struct " + nodo_tipo.id);
          
          /* GERA CÓDIGO: (base + offset) */
          System.out.println("\tMOVL $_" + id_var + ", %EAX");
          System.out.println("\tADDL $" + nodo_campo.getOffset() + ", %EAX");
          System.out.println("\tPUSHL %EAX");
      }
    /* * array (ex: v[i]) */
    | ID '[' exp ']' {
          String id_var = $1;
          
          TS_entry nodo_var = ts.pesquisa(id_var);
          if (nodo_var == null) yyerror("(sem) array >" + id_var + "< nao declarado");
          if (nodo_var.getTipo() != Parser.ARRAY) yyerror("(sem) >" + id_var + "< nao eh um array");

          /* GERA CÓDIGO: (base + (indice * 4)) */
          System.out.println("\tPOPL %EAX");     // EAX = indice (da 'exp')
          System.out.println("\tIMULL $4, %EAX");  // EAX = indice * 4
          System.out.println("\tADDL $_" + id_var + ", %EAX"); // EAX = _v + (indice * 4)
          System.out.println("\tPUSHL %EAX");    // Empilha o endereço final
      }
	  /* * acesso a array DENTRO de struct (ex: p1.notas[i]) */
    | ID '.' ID '[' exp ']' {
          TS_entry nodo_var = ts.pesquisa($1); // p1
          if (nodo_var == null) yyerror("(sem) variavel >" + $1 + "< nao declarada");
          TS_entry nodo_tipo = ts.pesquisaTipo(nodo_var.getTipoStruct()); // tipo de p1
          if (nodo_tipo == null) yyerror("(sem) tipo >" + nodo_var.getTipoStruct() + "< nao eh um struct");
          TS_entry nodo_campo = nodo_tipo.getCampo($3); // notas
          if (nodo_campo == null) yyerror("(sem) campo >" + $3 + "< nao existe");
          if (nodo_campo.getTipo() != Parser.ARRAY) yyerror("(sem) campo >" + $3 + "< nao eh um array");

          System.out.println("\tPOPL %EAX"); // EAX = indice (da exp)
          System.out.println("\tIMULL $" + nodo_campo.getTamanhoElemento() + ", %EAX"); // EAX = indice * 4
          
          System.out.println("\tMOVL $_" + $1 + ", %EDX"); // EDX = end base (p1)
          System.out.println("\tADDL $" + nodo_campo.getOffset() + ", %EDX"); // EDX = end base + offset 
          
          System.out.println("\tADDL %EDX, %EAX"); // EAX = (p1+offset_notas) + (indice*4)
          System.out.println("\tPUSHL %EAX");
      }
    /* * acesso a struct entro de array (ex: lista[i].x) */
    | ID '[' exp ']' '.' ID {
          TS_entry nodo_var = ts.pesquisa($1); // lista
          if (nodo_var == null) yyerror("(sem) array >" + $1 + "< nao declarado");
          if (nodo_var.getTipo() != Parser.ARRAY) yyerror("(sem) >" + $1 + "< nao eh um array");
          
          TS_entry nodo_tipo = ts.pesquisaTipo(nodo_var.getTipoStruct()); // Ponto
          if (nodo_tipo == null) yyerror("(sem) tipo base >" + nodo_var.getTipoStruct() + "< nao eh struct");
          
          TS_entry nodo_campo = nodo_tipo.getCampo($6); // x
          if (nodo_campo == null) yyerror("(sem) campo >" + $6 + "< nao existe");
          
          int tamanho_struct = nodo_var.getTamanhoElemento();
          int offset_campo = nodo_campo.getOffset();

          System.out.println("\tPOPL %EAX"); // EAX = indice (da exp)
          System.out.println("\tIMULL $" + tamanho_struct + ", %EAX"); // EAX = indice * tam_struct
          
          System.out.println("\tADDL $_" + $1 + ", %EAX"); // EAX = _lista + (indice * tam_struct)
          
          System.out.println("\tADDL $" + offset_campo + ", %EAX"); // EAX = (base + ... ) + offset_x
          System.out.println("\tPUSHL %EAX");
      	}
;


/* Se a expressão for vazia, empilha 'true' (1) para criar um loop infinito.*/
for_cond_opt : exp
             | /* Vazio */ { System.out.println("\tPUSHL $1"); }
             ;				

%%

  private Yylex lexer;

  private TabSimb ts = new TabSimb();

  private int strCount = 0;
  private ArrayList<String> strTab = new ArrayList<String>();

  private Stack<Integer> pRot = new Stack<Integer>();
  private int proxRot = 1;
  private Stack<Integer> pLoopBreak = new Stack<Integer>();
  private Stack<Integer> pLoopContinue = new Stack<Integer>();


  public static int ARRAY = 100;


  private int yylex () {
    int yyl_return = -1;
    try {
      yylval = new ParserVal(0);
      yyl_return = lexer.yylex();
    }
    catch (IOException e) {
      System.err.println("IO error :"+e);
    }
    return yyl_return;
  }


  public void yyerror (String error) {
    System.err.println ("Error: " + error + "  linha: " + lexer.getLine());
  }


  public Parser(Reader r) {
    lexer = new Yylex(r, this);
  }  

  public void setDebug(boolean debug) {
    yydebug = debug;
  }

  public void listarTS() { ts.listar();}

  public static void main(String args[]) throws IOException {

    Parser yyparser;
    if ( args.length > 0 ) {
      // parse a file
      yyparser = new Parser(new FileReader(args[0]));
      yyparser.yyparse();
      // yyparser.listarTS();

    }
    else {
      // interactive mode
      System.out.println("\n\tFormato: java Parser entrada.cmm >entrada.s\n");
    }

  }

							
		void gcExpArit(int oparit) {
 				System.out.println("\tPOPL %EBX");
   			System.out.println("\tPOPL %EAX");

   		switch (oparit) {
     		case '+' : System.out.println("\tADDL %EBX, %EAX" ); break;
     		case '-' : System.out.println("\tSUBL %EBX, %EAX" ); break;
     		case '*' : System.out.println("\tIMULL %EBX, %EAX" ); break;

    		case '/': 
           		     System.out.println("\tMOVL $0, %EDX");
           		     System.out.println("\tIDIVL %EBX");
           		     break;
     		case '%': 
           		     System.out.println("\tMOVL $0, %EDX");
           		     System.out.println("\tIDIVL %EBX");
           		     System.out.println("\tMOVL %EDX, %EAX");
           		     break;
    		}
   		System.out.println("\tPUSHL %EAX");
		}

	public void gcExpRel(int oprel) {

    System.out.println("\tPOPL %EAX");
    System.out.println("\tPOPL %EDX");
    System.out.println("\tCMPL %EAX, %EDX");
    System.out.println("\tMOVL $0, %EAX");

    System.out.println("\tXORL %EAX, %EAX"); // Limpa EAX (MOVL $0, %EAX é menos eficiente/verboso)
    
    switch (oprel) {
       case '<':  			System.out.println("\tSETL  %AL"); break;
       case '>':  			System.out.println("\tSETG  %AL"); break;
       case Parser.EQ:  System.out.println("\tSETE  %AL"); break;
       case Parser.GEQ: System.out.println("\tSETGE %AL"); break;
       case Parser.LEQ: System.out.println("\tSETLE %AL"); break;
       case Parser.NEQ: System.out.println("\tSETNE %AL"); break;
       }
    
    System.out.println("\tPUSHL %EAX");

	}


	public void gcExpLog(int oplog) {

	   	System.out.println("\tPOPL %EDX");
 		 	System.out.println("\tPOPL %EAX");

  	 	System.out.println("\tCMPL $0, %EAX");
 		  System.out.println("\tMOVL $0, %EAX");
   		System.out.println("\tSETNE %AL");
   		System.out.println("\tCMPL $0, %EDX");
   		System.out.println("\tMOVL $0, %EDX");
   		System.out.println("\tSETNE %DL");

   		switch (oplog) {
    			case Parser.OR:  System.out.println("\tORL  %EDX, %EAX");  break;
    			case Parser.AND: System.out.println("\tANDL  %EDX, %EAX"); break;
       }

    	System.out.println("\tPUSHL %EAX");
	}

	public void gcExpNot(){

  	 System.out.println("\tPOPL %EAX" );
 	   System.out.println("	\tNEGL %EAX" );
  	 System.out.println("	\tPUSHL %EAX");
	}

   private void geraInicio() {
			System.out.println(".text\n\n#\t Bernardo Klein Heitz, João Pedro Aiolfi de Figueiredo, Lucas Teixeira Brenner e Lucas Langer Lantmann \n#\n"); 
			System.out.println(".GLOBL _start\n\n");  
   }

   private void geraFinal(){
	
			System.out.println("\n\n");
			System.out.println("#");
			System.out.println("# devolve o controle para o SO (final da main)");
			System.out.println("#");
			System.out.println("\tmov $0, %ebx");
			System.out.println("\tmov $1, %eax");
			System.out.println("\tint $0x80");
	
			System.out.println("\n");
			System.out.println("#");
			System.out.println("# Funcoes da biblioteca (IO)");
			System.out.println("#");
			System.out.println("\n");
			System.out.println("_writeln:");
			System.out.println("\tMOVL $__fim_msg, %ECX");
			System.out.println("\tDECL %ECX");
			System.out.println("\tMOVB $10, (%ECX)");
			System.out.println("\tMOVL $1, %EDX");
			System.out.println("\tJMP _writeLit");
			System.out.println("_write:");
			System.out.println("\tMOVL $__fim_msg, %ECX");
			System.out.println("\tMOVL $0, %EBX");
			System.out.println("\tCMPL $0, %EAX");
			System.out.println("\tJGE _write3");
			System.out.println("\tNEGL %EAX");
			System.out.println("\tMOVL $1, %EBX");
			System.out.println("_write3:");
			System.out.println("\tPUSHL %EBX");
			System.out.println("\tMOVL $10, %EBX");
			System.out.println("_divide:");
			System.out.println("\tMOVL $0, %EDX");
			System.out.println("\tIDIVL %EBX");
			System.out.println("\tDECL %ECX");
			System.out.println("\tADD $48, %DL");
			System.out.println("\tMOVB %DL, (%ECX)");
			System.out.println("\tCMPL $0, %EAX");
			System.out.println("\tJNE _divide");
			System.out.println("\tPOPL %EBX");
			System.out.println("\tCMPL $0, %EBX");
			System.out.println("\tJE _print");
			System.out.println("\tDECL %ECX");
			System.out.println("\tMOVB $'-', (%ECX)");
			System.out.println("_print:");
			System.out.println("\tMOVL $__fim_msg, %EDX");
			System.out.println("\tSUBL %ECX, %EDX");
			System.out.println("_writeLit:");
			System.out.println("\tMOVL $1, %EBX");
			System.out.println("\tMOVL $4, %EAX");
			System.out.println("\tint $0x80");
			System.out.println("\tRET");
			System.out.println("_read:");
			System.out.println("\tMOVL $15, %EDX");
			System.out.println("\tMOVL $__msg, %ECX");
			System.out.println("\tMOVL $0, %EBX");
			System.out.println("\tMOVL $3, %EAX");
			System.out.println("\tint $0x80");
			System.out.println("\tMOVL $0, %EAX");
			System.out.println("\tMOVL $0, %EBX");
			System.out.println("\tMOVL $0, %EDX");
			System.out.println("\tMOVL $__msg, %ECX");
			System.out.println("\tCMPB $'-', (%ECX)");
			System.out.println("\tJNE _reading");
			System.out.println("\tINCL %ECX");
			System.out.println("\tINC %BL");
			System.out.println("_reading:");
			System.out.println("\tMOVB (%ECX), %DL");
			System.out.println("\tCMP $10, %DL");
			System.out.println("\tJE _fimread");
			System.out.println("\tSUB $48, %DL");
			System.out.println("\tIMULL $10, %EAX");
			System.out.println("\tADDL %EDX, %EAX");
			System.out.println("\tINCL %ECX");
			System.out.println("\tJMP _reading");
			System.out.println("_fimread:");
			System.out.println("\tCMPB $1, %BL");
			System.out.println("\tJNE _fimread2");
			System.out.println("\tNEGL %EAX");
			System.out.println("_fimread2:");
			System.out.println("\tRET");
			System.out.println("\n");
     }

     private void geraAreaDados(){
			System.out.println("");		
			System.out.println("#");
			System.out.println("# area de dados");
			System.out.println("#");
			System.out.println(".data");
			System.out.println("#");
			System.out.println("# variaveis globais");
			System.out.println("#");
			ts.geraGlobais();	
			System.out.println("");
	
    }

     private void geraAreaLiterais() { 

         System.out.println("#\n# area de literais\n#");
         System.out.println("__msg:");
	       System.out.println("\t.zero 30");
	       System.out.println("__fim_msg:");
	       System.out.println("\t.byte 0");
	       System.out.println("\n");

         for (int i = 0; i<strTab.size(); i++ ) {
             System.out.println("_str_"+i+":");
             System.out.println("\t .ascii \""+strTab.get(i)+"\""); 
	           System.out.println("_str_"+i+"Len = . - _str_"+i);  
	      }		
   }