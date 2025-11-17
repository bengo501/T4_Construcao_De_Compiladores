//### This file created by BYACC 1.8(/Java extension  1.15)
//### Java capabilities added 7 Jan 97, Bob Jamison
//### Updated : 27 Nov 97  -- Bob Jamison, Joe Nieten
//###           01 Jan 98  -- Bob Jamison -- fixed generic semantic constructor
//###           01 Jun 99  -- Bob Jamison -- added Runnable support
//###           06 Aug 00  -- Bob Jamison -- made state variables class-global
//###           03 Jan 01  -- Bob Jamison -- improved flags, tracing
//###           16 May 01  -- Bob Jamison -- added custom stack sizing
//###           04 Mar 02  -- Yuval Oren  -- improved java performance, added options
//###           14 Mar 02  -- Tomas Hurka -- -d support, static initializer workaround
//### Please send bug reports to tom@hukatronic.cz
//### static char yysccsid[] = "@(#)yaccpar	1.8 (Berkeley) 01/20/90";






//#line 2 "exemploGC.y"
  import java.io.*;
  import java.util.ArrayList;
  import java.util.Stack;
  import java.util.Map;
  import java.util.HashMap;
//#line 23 "Parser.java"




public class Parser
{

boolean yydebug;        //do I want debug output?
int yynerrs;            //number of errors so far
int yyerrflag;          //was there an error?
int yychar;             //the current working character

//########## MESSAGES ##########
//###############################################################
// method: debug
//###############################################################
void debug(String msg)
{
  if (yydebug)
    System.out.println(msg);
}

//########## STATE STACK ##########
final static int YYSTACKSIZE = 500;  //maximum stack size
int statestk[] = new int[YYSTACKSIZE]; //state stack
int stateptr;
int stateptrmax;                     //highest index of stackptr
int statemax;                        //state when highest index reached
//###############################################################
// methods: state stack push,pop,drop,peek
//###############################################################
final void state_push(int state)
{
  try {
		stateptr++;
		statestk[stateptr]=state;
	 }
	 catch (ArrayIndexOutOfBoundsException e) {
     int oldsize = statestk.length;
     int newsize = oldsize * 2;
     int[] newstack = new int[newsize];
     System.arraycopy(statestk,0,newstack,0,oldsize);
     statestk = newstack;
     statestk[stateptr]=state;
  }
}
final int state_pop()
{
  return statestk[stateptr--];
}
final void state_drop(int cnt)
{
  stateptr -= cnt; 
}
final int state_peek(int relative)
{
  return statestk[stateptr-relative];
}
//###############################################################
// method: init_stacks : allocate and prepare stacks
//###############################################################
final boolean init_stacks()
{
  stateptr = -1;
  val_init();
  return true;
}
//###############################################################
// method: dump_stacks : show n levels of the stacks
//###############################################################
void dump_stacks(int count)
{
int i;
  System.out.println("=index==state====value=     s:"+stateptr+"  v:"+valptr);
  for (i=0;i<count;i++)
    System.out.println(" "+i+"    "+statestk[i]+"      "+valstk[i]);
  System.out.println("======================");
}


//########## SEMANTIC VALUES ##########
//public class ParserVal is defined in ParserVal.java


String   yytext;//user variable to return contextual strings
ParserVal yyval; //used to return semantic vals from action routines
ParserVal yylval;//the 'lval' (result) I got from yylex()
ParserVal valstk[];
int valptr;
//###############################################################
// methods: value stack push,pop,drop,peek.
//###############################################################
void val_init()
{
  valstk=new ParserVal[YYSTACKSIZE];
  yyval=new ParserVal();
  yylval=new ParserVal();
  valptr=-1;
}
void val_push(ParserVal val)
{
  if (valptr>=YYSTACKSIZE)
    return;
  valstk[++valptr]=val;
}
ParserVal val_pop()
{
  if (valptr<0)
    return new ParserVal();
  return valstk[valptr--];
}
void val_drop(int cnt)
{
int ptr;
  ptr=valptr-cnt;
  if (ptr<0)
    return;
  valptr = ptr;
}
ParserVal val_peek(int relative)
{
int ptr;
  ptr=valptr-relative;
  if (ptr<0)
    return new ParserVal();
  return valstk[ptr];
}
final ParserVal dup_yyval(ParserVal val)
{
  ParserVal dup = new ParserVal();
  dup.ival = val.ival;
  dup.dval = val.dval;
  dup.sval = val.sval;
  dup.obj = val.obj;
  return dup;
}
//#### end semantic value section ####
public final static short ID=257;
public final static short INT=258;
public final static short FLOAT=259;
public final static short BOOL=260;
public final static short NUM=261;
public final static short LIT=262;
public final static short VOID=263;
public final static short MAIN=264;
public final static short READ=265;
public final static short WRITE=266;
public final static short IF=267;
public final static short ELSE=268;
public final static short WHILE=269;
public final static short TRUE=270;
public final static short FALSE=271;
public final static short EQ=272;
public final static short LEQ=273;
public final static short GEQ=274;
public final static short NEQ=275;
public final static short AND=276;
public final static short OR=277;
public final static short INC=278;
public final static short DEC=279;
public final static short MAIS_IGUAL=280;
public final static short INTERROGACAO=281;
public final static short DOIS_PONTOS=282;
public final static short DO=283;
public final static short FOR=284;
public final static short BREAK=285;
public final static short CONTINUE=286;
public final static short STRUCT=287;
public final static short YYERRCODE=256;
final static short yylhs[] = {                           -1,
    5,    0,    7,    9,    6,    4,    4,    1,    1,    1,
    3,    3,    2,    2,   10,   10,   10,   10,   10,    8,
    8,   11,   11,   11,   13,   11,   11,   15,   16,   11,
   17,   11,   11,   11,   20,   21,   22,   11,   23,   11,
   25,   24,   24,   12,   12,   12,   12,   12,   12,   12,
   12,   12,   12,   12,   12,   12,   12,   12,   12,   12,
   12,   12,   12,   12,   12,   12,   12,   12,   26,   27,
   12,   18,   18,   14,   14,   14,   14,   14,   19,   19,
};
final static short yylen[] = {                            2,
    0,    3,    0,    0,    9,    2,    0,    1,    1,    1,
    3,    6,    2,    0,    3,    6,    6,    6,    3,    2,
    0,    2,    3,    5,    0,    8,    5,    0,    0,    7,
    0,    8,    2,    2,    0,    0,    0,   12,    0,    7,
    0,    3,    0,    1,    1,    1,    1,    3,    2,    3,
    3,    2,    2,    2,    2,    3,    3,    3,    3,    3,
    3,    3,    3,    3,    3,    3,    3,    3,    0,    0,
    7,    1,    0,    1,    3,    4,    6,    6,    1,    0,
};
final static short yydefred[] = {                         1,
    0,    0,    0,    8,    9,   10,    0,    0,    0,    0,
    0,    0,    0,    0,    2,    6,   19,    0,   14,   15,
    0,    0,    0,    0,    0,    0,    0,    0,    0,   13,
    0,    3,   17,   18,    0,   16,    0,   11,    0,   21,
    0,    0,    0,    0,   44,    0,    0,    0,   28,   45,
   46,    0,    0,   31,    0,    0,    0,    0,    0,   21,
    0,   20,    0,    0,   12,   53,   55,    0,    0,    0,
    0,    0,    0,    0,   52,   54,    0,    0,   33,   34,
   49,    0,    0,    5,    0,    0,    0,    0,    0,    0,
   69,    0,    0,    0,    0,    0,    0,    0,   22,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,   48,   23,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,   58,   59,   60,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   35,    0,    0,    0,
   27,   24,    0,    0,   29,    0,    0,   70,   78,   77,
    0,    0,    0,    0,    0,    0,    0,    0,   41,   40,
   30,    0,   36,    0,   26,    0,   32,    0,   42,    0,
   37,    0,   38,
};
final static short yydgoto[] = {                          1,
    8,   24,   30,    9,    2,   15,   37,   42,   61,   10,
   62,   63,  133,   64,   74,  153,   77,  111,  156,  147,
  168,  172,  134,  160,  166,  120,  157,
};
final static short yysindex[] = {                         0,
    0, -163, -252,    0,    0,    0, -247, -245, -243, -163,
  -51, -107,  -46, -242,    0,    0,    0, -236,    0,    0,
 -235,  -11,  -60, -114,  -39,    8,   -9,   -4, -200,    0,
    3,    0,    0,    0,  -44,    0,  -59,    0, -198,    0,
  -25,   27,   10,  -19,    0,   34,   36,   37,    0,    0,
    0, -179, -176,    0,   48,   23,   32,  -31,  -31,    0,
  -18,    0,  132,   47,    0,    0,    0,  -31,  -31, -159,
 -148, -147,  -31,   77,    0,    0,   27,  -31,    0,    0,
    0,  159,  -33,    0,  -31,  -31,  -31,  -31,  -31,  -31,
    0,  -31,  -31,  -31,  -31,  -31,  -31,  -31,    0,  -31,
  437,  287,   35,  -43,   84,   93,  437,  -31, -133,  437,
   81,    0,    0,   76,   76,   76,   76,   -1,  341,  -31,
   76,   76,   28,   28,    0,    0,    0,   -1,  101,  -31,
   83,   89,  105,  110,  314,  112,    0,  379, -104,  401,
    0,    0,  -31,   27,    0,  -31,  -31,    0,    0,    0,
  408, -105,   27,  415,  437,  102,  -31,  108,    0,    0,
    0,  113,    0,  437,    0,   27,    0,  -31,    0,  130,
    0,   27,    0,
};
final static short yyrindex[] = {                         0,
    0,  -90,    0,    0,    0,    0,    0,    0,    0,  -90,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,   51,    0,   42,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  123,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  119,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
  -40,    0,   69,  139,    0,  140,  146,    0,    0,  -24,
    0,    0,    0,  457,  464,  473,  489,  -35,   -7,    0,
  512,  535,  444,  450,    0,    0,    0,  -20,   96,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   32,    0,    0,    0,
    0,   -3,    0,    0,   23,    0,    0,    0,    0,    0,
    0,    0,    0,  -27,    0,    0,    0,  147,    0,    0,
    0,    0,    0,
};
final static short yygindex[] = {                         0,
  166,    0,    0,  183,    0,    0,    0,  137,    0,    0,
  -73,  745,    0,  127,    0,    0,    0,   31,    0,    0,
    0,    0,    0,    0,    0,    0,    0,
};
final static int YYTABLESIZE=913;
static short yytable[];
static { yytable();}
static void yytable(){
yytable = new short[]{                         58,
   50,   58,   70,  109,   11,   68,   59,   17,   59,   12,
   28,   13,   20,   71,   38,   19,   72,   50,   50,   14,
   51,   22,   68,   68,   23,   25,   70,   68,   26,   43,
   71,   71,   27,   67,   72,   98,   43,   51,   51,   18,
   96,   94,   51,   95,   21,   97,   39,   69,   32,   33,
   67,   67,   50,   31,   34,   67,   35,   68,   93,   58,
   92,   36,   41,   40,   98,   71,   59,   43,   65,   96,
  152,   69,   51,   71,   97,   72,   73,   75,   74,  161,
   76,   79,   74,   74,   74,   67,   74,   78,   74,   60,
   80,  113,  169,    3,    4,    5,    6,  103,  173,   74,
   74,   74,   74,   74,   74,   75,   84,  100,  104,   75,
   75,   75,   98,   75,  106,   75,  108,   96,   94,   43,
   95,   43,   97,    7,  131,  130,   75,   75,   75,   75,
   75,   75,   76,  132,   74,  136,   76,   76,   76,  137,
   76,  141,   76,    4,    5,    6,  139,  142,  143,   60,
  144,  146,  149,   76,   76,   76,   76,   76,   76,   47,
  163,   75,  159,   47,   47,   47,  165,   47,   98,   47,
  171,  167,    7,   96,   94,    4,   95,   73,   97,   74,
   47,   47,   47,   25,   47,   47,   39,   73,   76,   29,
   99,   93,   16,   92,   91,   98,   83,  105,  170,  112,
   96,   94,    0,   95,    0,   97,    0,    0,    0,    0,
    0,    0,    0,    0,    0,   47,    0,    0,   93,    0,
   92,   91,    0,   44,    0,   44,    0,   45,    0,   45,
    0,   46,   47,   48,    0,   49,   50,   51,   50,   51,
   68,   68,    0,    0,   52,   53,   52,   53,    0,   54,
   55,   56,   57,   43,    0,   51,   51,   43,   66,   67,
   68,   43,   43,   43,    0,   43,   43,   43,    0,   67,
   85,   86,   87,   88,   43,   43,    0,    0,    0,   43,
   43,   43,   43,   44,    0,    0,    0,   45,    0,    0,
    0,   46,   47,   48,    0,   49,   50,   51,    0,    0,
    0,    0,    0,    0,   52,   53,    0,    0,    0,   54,
   55,   56,   57,   74,   74,   74,   74,   74,   74,    0,
    0,    0,    0,   98,    0,    0,    0,    0,   96,   94,
    0,   95,    0,   97,    0,    0,    0,    0,    0,    0,
   75,   75,   75,   75,   75,   75,   93,    0,   92,   91,
   98,    0,    0,    0,  145,   96,   94,    0,   95,    0,
   97,    0,    0,    0,    0,    0,    0,   76,   76,   76,
   76,   76,   76,   93,    0,   92,   91,   98,    0,  129,
    0,    0,   96,   94,    0,   95,    0,   97,    0,    0,
    0,    0,    0,    0,   47,   47,   47,   47,   47,   47,
   93,    0,   92,   85,   86,   87,   88,   89,   90,    0,
    0,    0,    0,    0,    0,   98,    0,    0,    0,    0,
   96,   94,    0,   95,    0,   97,    0,    0,    0,    0,
   85,   86,   87,   88,   89,   90,  148,   98,   93,    0,
   92,   91,   96,   94,   98,   95,    0,   97,  158,   96,
   94,   98,   95,    0,   97,  162,   96,   94,    0,   95,
   93,   97,   92,   91,    0,    0,    0,   93,    0,   92,
   91,    0,    0,   98,   93,    0,   92,   91,   96,   94,
    0,   95,    0,   97,   56,    0,   56,    0,   56,    0,
   57,    0,   57,  150,   57,    0,   93,   63,   92,   91,
    0,   56,   56,   56,   64,   56,   56,   57,   57,   57,
    0,   57,   57,   65,   63,   63,   63,    0,   63,   63,
    0,   64,   64,   64,    0,   64,   64,    0,    0,   66,
   65,   65,   65,    0,   65,   65,   56,    0,    0,    0,
    0,    0,   57,    0,    0,    0,   66,   66,   66,   63,
   66,   66,   61,    0,    0,    0,   64,    0,   85,   86,
   87,   88,   89,   90,    0,   65,    0,    0,    0,   61,
   61,   61,    0,   61,   61,   62,    0,    0,    0,    0,
    0,   66,    0,    0,    0,   85,   86,   87,   88,   89,
   90,    0,   62,   62,   62,    0,   62,   62,    0,    0,
    0,    0,    0,    0,   61,    0,    0,    0,    0,    0,
    0,    0,   85,   86,   87,   88,   89,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   62,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   85,   86,   87,   88,   89,   90,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   85,   86,   87,   88,   89,   90,    0,   85,
   86,   87,   88,   89,   90,    0,   85,   86,   87,   88,
   89,   90,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,   85,   86,
   87,   88,   89,   90,    0,   56,   56,   56,   56,   56,
   56,   57,   57,   57,   57,   57,   57,    0,   63,   63,
   63,   63,   63,   63,    0,   64,   64,   64,   64,   64,
   64,    0,    0,    0,   65,   65,   65,   65,   65,   65,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   66,   66,   66,   66,   66,   66,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   61,   61,   61,   61,   61,   61,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   81,   82,    0,    0,   62,   62,   62,   62,
   62,   62,  101,  102,    0,    0,    0,  107,    0,    0,
    0,    0,  110,    0,    0,    0,    0,    0,    0,  114,
  115,  116,  117,  118,  119,    0,  121,  122,  123,  124,
  125,  126,  127,    0,  128,    0,    0,    0,    0,    0,
    0,    0,  135,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  138,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  140,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  151,    0,    0,
  154,  155,    0,    0,    0,    0,    0,    0,    0,    0,
    0,  164,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,  110,
};
}
static short yycheck[];
static { yycheck(); }
static void yycheck() {
yycheck = new short[] {                         33,
   41,   33,   46,   77,  257,   41,   40,   59,   40,  257,
  125,  257,   59,   41,   59,  123,   41,   58,   59,  263,
   41,  264,   58,   59,  261,  261,   46,   63,   40,   33,
   58,   59,   93,   41,   59,   37,   40,   58,   59,   91,
   42,   43,   63,   45,   91,   47,   91,   91,   41,   59,
   58,   59,   93,   93,   59,   63,  257,   93,   60,   33,
   62,   59,  261,  123,   37,   93,   40,   93,   59,   42,
  144,   91,   93,   40,   47,   40,   40,  257,   37,  153,
  257,   59,   41,   42,   43,   93,   45,   40,   47,  123,
   59,  125,  166,  257,  258,  259,  260,  257,  172,   58,
   59,   60,   61,   62,   63,   37,  125,   61,  257,   41,
   42,   43,   37,   45,  262,   47,   40,   42,   43,  123,
   45,  125,   47,  287,   41,   91,   58,   59,   60,   61,
   62,   63,   37,   41,   93,  269,   41,   42,   43,   59,
   45,   59,   47,  258,  259,  260,   46,   59,   44,  123,
   41,   40,  257,   58,   59,   60,   61,   62,   63,   37,
   59,   93,  268,   41,   42,   43,   59,   45,   37,   47,
   41,   59,  263,   42,   43,  125,   45,   59,   47,   41,
   58,   59,   60,   44,   62,   63,   41,   41,   93,   24,
   59,   60,   10,   62,   63,   37,   60,   71,  168,   41,
   42,   43,   -1,   45,   -1,   47,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   93,   -1,   -1,   60,   -1,
   62,   63,   -1,  257,   -1,  257,   -1,  261,   -1,  261,
   -1,  265,  266,  267,   -1,  269,  270,  271,  270,  271,
  276,  277,   -1,   -1,  278,  279,  278,  279,   -1,  283,
  284,  285,  286,  257,   -1,  276,  277,  261,  278,  279,
  280,  265,  266,  267,   -1,  269,  270,  271,   -1,  277,
  272,  273,  274,  275,  278,  279,   -1,   -1,   -1,  283,
  284,  285,  286,  257,   -1,   -1,   -1,  261,   -1,   -1,
   -1,  265,  266,  267,   -1,  269,  270,  271,   -1,   -1,
   -1,   -1,   -1,   -1,  278,  279,   -1,   -1,   -1,  283,
  284,  285,  286,  272,  273,  274,  275,  276,  277,   -1,
   -1,   -1,   -1,   37,   -1,   -1,   -1,   -1,   42,   43,
   -1,   45,   -1,   47,   -1,   -1,   -1,   -1,   -1,   -1,
  272,  273,  274,  275,  276,  277,   60,   -1,   62,   63,
   37,   -1,   -1,   -1,   41,   42,   43,   -1,   45,   -1,
   47,   -1,   -1,   -1,   -1,   -1,   -1,  272,  273,  274,
  275,  276,  277,   60,   -1,   62,   63,   37,   -1,   93,
   -1,   -1,   42,   43,   -1,   45,   -1,   47,   -1,   -1,
   -1,   -1,   -1,   -1,  272,  273,  274,  275,  276,  277,
   60,   -1,   62,  272,  273,  274,  275,  276,  277,   -1,
   -1,   -1,   -1,   -1,   -1,   37,   -1,   -1,   -1,   -1,
   42,   43,   -1,   45,   -1,   47,   -1,   -1,   -1,   -1,
  272,  273,  274,  275,  276,  277,   58,   37,   60,   -1,
   62,   63,   42,   43,   37,   45,   -1,   47,   41,   42,
   43,   37,   45,   -1,   47,   41,   42,   43,   -1,   45,
   60,   47,   62,   63,   -1,   -1,   -1,   60,   -1,   62,
   63,   -1,   -1,   37,   60,   -1,   62,   63,   42,   43,
   -1,   45,   -1,   47,   41,   -1,   43,   -1,   45,   -1,
   41,   -1,   43,   93,   45,   -1,   60,   41,   62,   63,
   -1,   58,   59,   60,   41,   62,   63,   58,   59,   60,
   -1,   62,   63,   41,   58,   59,   60,   -1,   62,   63,
   -1,   58,   59,   60,   -1,   62,   63,   -1,   -1,   41,
   58,   59,   60,   -1,   62,   63,   93,   -1,   -1,   -1,
   -1,   -1,   93,   -1,   -1,   -1,   58,   59,   60,   93,
   62,   63,   41,   -1,   -1,   -1,   93,   -1,  272,  273,
  274,  275,  276,  277,   -1,   93,   -1,   -1,   -1,   58,
   59,   60,   -1,   62,   63,   41,   -1,   -1,   -1,   -1,
   -1,   93,   -1,   -1,   -1,  272,  273,  274,  275,  276,
  277,   -1,   58,   59,   60,   -1,   62,   63,   -1,   -1,
   -1,   -1,   -1,   -1,   93,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  272,  273,  274,  275,  276,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   93,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
  272,  273,  274,  275,  276,  277,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  272,  273,  274,  275,  276,  277,   -1,  272,
  273,  274,  275,  276,  277,   -1,  272,  273,  274,  275,
  276,  277,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  272,  273,
  274,  275,  276,  277,   -1,  272,  273,  274,  275,  276,
  277,  272,  273,  274,  275,  276,  277,   -1,  272,  273,
  274,  275,  276,  277,   -1,  272,  273,  274,  275,  276,
  277,   -1,   -1,   -1,  272,  273,  274,  275,  276,  277,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
  272,  273,  274,  275,  276,  277,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,  272,  273,  274,  275,  276,  277,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   58,   59,   -1,   -1,  272,  273,  274,  275,
  276,  277,   68,   69,   -1,   -1,   -1,   73,   -1,   -1,
   -1,   -1,   78,   -1,   -1,   -1,   -1,   -1,   -1,   85,
   86,   87,   88,   89,   90,   -1,   92,   93,   94,   95,
   96,   97,   98,   -1,  100,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  108,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  120,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  130,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,  143,   -1,   -1,
  146,  147,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,  157,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  168,
};
}
final static short YYFINAL=1;
final static short YYMAXTOKEN=287;
final static String yyname[] = {
"end-of-file",null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,"'!'",null,null,null,"'%'",null,null,"'('","')'","'*'","'+'",
"','","'-'","'.'","'/'",null,null,null,null,null,null,null,null,null,null,"':'",
"';'","'<'","'='","'>'","'?'",null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,"'['",null,"']'",null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,"'{'",null,"'}'",null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,"ID","INT","FLOAT","BOOL","NUM",
"LIT","VOID","MAIN","READ","WRITE","IF","ELSE","WHILE","TRUE","FALSE","EQ",
"LEQ","GEQ","NEQ","AND","OR","INC","DEC","MAIS_IGUAL","INTERROGACAO",
"DOIS_PONTOS","DO","FOR","BREAK","CONTINUE","STRUCT",
};
final static String yyrule[] = {
"$accept : prog",
"$$1 :",
"prog : $$1 dList mainF",
"$$2 :",
"$$3 :",
"mainF : VOID MAIN '(' ')' $$2 '{' lcmd $$3 '}'",
"dList : decl dList",
"dList :",
"type : INT",
"type : FLOAT",
"type : BOOL",
"campo : type ID ';'",
"campo : type ID '[' NUM ']' ';'",
"l_campos : l_campos campo",
"l_campos :",
"decl : type ID ';'",
"decl : type ID '[' NUM ']' ';'",
"decl : ID ID '[' NUM ']' ';'",
"decl : STRUCT ID '{' l_campos '}' ';'",
"decl : ID ID ';'",
"lcmd : lcmd cmd",
"lcmd :",
"cmd : exp ';'",
"cmd : '{' lcmd '}'",
"cmd : WRITE '(' LIT ')' ';'",
"$$4 :",
"cmd : WRITE '(' LIT $$4 ',' exp ')' ';'",
"cmd : READ '(' ref ')' ';'",
"$$5 :",
"$$6 :",
"cmd : WHILE $$5 '(' exp ')' $$6 cmd",
"$$7 :",
"cmd : DO $$7 cmd WHILE '(' exp ')' ';'",
"cmd : BREAK ';'",
"cmd : CONTINUE ';'",
"$$8 :",
"$$9 :",
"$$10 :",
"cmd : FOR '(' opt_exp ';' $$8 for_cond_opt ';' $$9 opt_exp ')' $$10 cmd",
"$$11 :",
"cmd : IF '(' exp $$11 ')' cmd restoIf",
"$$12 :",
"restoIf : ELSE $$12 cmd",
"restoIf :",
"exp : NUM",
"exp : TRUE",
"exp : FALSE",
"exp : ref",
"exp : '(' exp ')'",
"exp : '!' exp",
"exp : ID MAIS_IGUAL exp",
"exp : ref '=' exp",
"exp : INC ID",
"exp : ID INC",
"exp : DEC ID",
"exp : ID DEC",
"exp : exp '+' exp",
"exp : exp '-' exp",
"exp : exp '*' exp",
"exp : exp '/' exp",
"exp : exp '%' exp",
"exp : exp '>' exp",
"exp : exp '<' exp",
"exp : exp EQ exp",
"exp : exp LEQ exp",
"exp : exp GEQ exp",
"exp : exp NEQ exp",
"exp : exp OR exp",
"exp : exp AND exp",
"$$13 :",
"$$14 :",
"exp : exp '?' $$13 exp ':' $$14 exp",
"opt_exp : exp",
"opt_exp :",
"ref : ID",
"ref : ID '.' ID",
"ref : ID '[' exp ']'",
"ref : ID '.' ID '[' exp ']'",
"ref : ID '[' exp ']' '.' ID",
"for_cond_opt : exp",
"for_cond_opt :",
};

//#line 524 "exemploGC.y"

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
//#line 771 "Parser.java"
//###############################################################
// method: yylexdebug : check lexer state
//###############################################################
void yylexdebug(int state,int ch)
{
String s=null;
  if (ch < 0) ch=0;
  if (ch <= YYMAXTOKEN) //check index bounds
     s = yyname[ch];    //now get it
  if (s==null)
    s = "illegal-symbol";
  debug("state "+state+", reading "+ch+" ("+s+")");
}





//The following are now global, to aid in error reporting
int yyn;       //next next thing to do
int yym;       //
int yystate;   //current parsing state from state table
String yys;    //current token string


//###############################################################
// method: yyparse : parse input and execute indicated items
//###############################################################
int yyparse()
{
boolean doaction;
  init_stacks();
  yynerrs = 0;
  yyerrflag = 0;
  yychar = -1;          //impossible char forces a read
  yystate=0;            //initial state
  state_push(yystate);  //save it
  val_push(yylval);     //save empty value
  while (true) //until parsing is done, either correctly, or w/error
    {
    doaction=true;
    if (yydebug) debug("loop"); 
    //#### NEXT ACTION (from reduction table)
    for (yyn=yydefred[yystate];yyn==0;yyn=yydefred[yystate])
      {
      if (yydebug) debug("yyn:"+yyn+"  state:"+yystate+"  yychar:"+yychar);
      if (yychar < 0)      //we want a char?
        {
        yychar = yylex();  //get next token
        if (yydebug) debug(" next yychar:"+yychar);
        //#### ERROR CHECK ####
        if (yychar < 0)    //it it didn't work/error
          {
          yychar = 0;      //change it to default string (no -1!)
          if (yydebug)
            yylexdebug(yystate,yychar);
          }
        }//yychar<0
      yyn = yysindex[yystate];  //get amount to shift by (shift index)
      if ((yyn != 0) && (yyn += yychar) >= 0 &&
          yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
        {
        if (yydebug)
          debug("state "+yystate+", shifting to state "+yytable[yyn]);
        //#### NEXT STATE ####
        yystate = yytable[yyn];//we are in a new state
        state_push(yystate);   //save it
        val_push(yylval);      //push our lval as the input for next rule
        yychar = -1;           //since we have 'eaten' a token, say we need another
        if (yyerrflag > 0)     //have we recovered an error?
           --yyerrflag;        //give ourselves credit
        doaction=false;        //but don't process yet
        break;   //quit the yyn=0 loop
        }

    yyn = yyrindex[yystate];  //reduce
    if ((yyn !=0 ) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
      {   //we reduced!
      if (yydebug) debug("reduce");
      yyn = yytable[yyn];
      doaction=true; //get ready to execute
      break;         //drop down to actions
      }
    else //ERROR RECOVERY
      {
      if (yyerrflag==0)
        {
        yyerror("syntax error");
        yynerrs++;
        }
      if (yyerrflag < 3) //low error count?
        {
        yyerrflag = 3;
        while (true)   //do until break
          {
          if (stateptr<0)   //check for under & overflow here
            {
            yyerror("stack underflow. aborting...");  //note lower case 's'
            return 1;
            }
          yyn = yysindex[state_peek(0)];
          if ((yyn != 0) && (yyn += YYERRCODE) >= 0 &&
                    yyn <= YYTABLESIZE && yycheck[yyn] == YYERRCODE)
            {
            if (yydebug)
              debug("state "+state_peek(0)+", error recovery shifting to state "+yytable[yyn]+" ");
            yystate = yytable[yyn];
            state_push(yystate);
            val_push(yylval);
            doaction=false;
            break;
            }
          else
            {
            if (yydebug)
              debug("error recovery discarding state "+state_peek(0)+" ");
            if (stateptr<0)   //check for under & overflow here
              {
              yyerror("Stack underflow. aborting...");  //capital 'S'
              return 1;
              }
            state_pop();
            val_pop();
            }
          }
        }
      else            //discard this token
        {
        if (yychar == 0)
          return 1; //yyabort
        if (yydebug)
          {
          yys = null;
          if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
          if (yys == null) yys = "illegal-symbol";
          debug("state "+yystate+", error recovery discards token "+yychar+" ("+yys+")");
          }
        yychar = -1;  //read another
        }
      }//end error recovery
    }//yyn=0 loop
    if (!doaction)   //any reason not to proceed?
      continue;      //skip action
    yym = yylen[yyn];          //get count of terminals on rhs
    if (yydebug)
      debug("state "+yystate+", reducing "+yym+" by rule "+yyn+" ("+yyrule[yyn]+")");
    if (yym>0)                 //if count of rhs not 'nil'
      yyval = val_peek(yym-1); //get current semantic value
    yyval = dup_yyval(yyval); //duplicate yyval if ParserVal is used as semantic value
    switch(yyn)
      {
//########## USER-SUPPLIED ACTIONS ##########
case 1:
//#line 39 "exemploGC.y"
{ geraInicio(); }
break;
case 2:
//#line 39 "exemploGC.y"
{ geraAreaDados(); geraAreaLiterais(); }
break;
case 3:
//#line 41 "exemploGC.y"
{ System.out.println("_start:"); }
break;
case 4:
//#line 42 "exemploGC.y"
{ geraFinal(); }
break;
case 8:
//#line 47 "exemploGC.y"
{ yyval.ival = INT; }
break;
case 9:
//#line 48 "exemploGC.y"
{ yyval.ival = FLOAT; }
break;
case 10:
//#line 49 "exemploGC.y"
{ yyval.ival = BOOL; }
break;
case 11:
//#line 52 "exemploGC.y"
{
            /* campo simples (int x) */
            yyval.obj = new TS_entry(val_peek(1).sval, val_peek(2).ival, 0); 
        }
break;
case 12:
//#line 56 "exemploGC.y"
{
            /* campo array - (int notas[4]) */
            int n_elem = Integer.parseInt(val_peek(2).sval);
            yyval.obj = new TS_entry(val_peek(4).sval, val_peek(5).ival, 0, n_elem);
        }
break;
case 13:
//#line 64 "exemploGC.y"
{
               Map<String, TS_entry> campos = (Map<String, TS_entry>)val_peek(1).obj;
               TS_entry novo_campo = (TS_entry)val_peek(0).obj;

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
               yyval.obj = val_peek(1).obj; /* Retorna o HashMap atualizado */
           }
break;
case 14:
//#line 80 "exemploGC.y"
{ 
               yyval.obj = new HashMap<String, TS_entry>(); 
           }
break;
case 15:
//#line 85 "exemploGC.y"
{
           if (ts.pesquisa(val_peek(1).sval) != null) {
               yyerror("(sem) variavel >" + val_peek(1).sval + "< jah declarada");
           } else {
               ts.insert(new TS_entry(val_peek(1).sval, val_peek(2).ival));
           }
      }
break;
case 16:
//#line 93 "exemploGC.y"
{
           String id_var = val_peek(4).sval;
           int tipo_base = val_peek(5).ival;
           int n_elem = Integer.parseInt(val_peek(2).sval);
           
           if (ts.pesquisa(id_var) != null) {
               yyerror("(sem) variavel >" + id_var + "< jah declarada");
           } else {
               /* Construtor de array simples: (id, nElem, tipoBase, tipoStruct, tamanhoElem) */
               ts.insert(new TS_entry(id_var, n_elem, tipo_base, null, 4));
           }
       }
break;
case 17:
//#line 106 "exemploGC.y"
{
           String id_tipo = val_peek(5).sval;
           String id_var = val_peek(4).sval;
           int n_elem = Integer.parseInt(val_peek(2).sval);
           
           TS_entry nodo_tipo = ts.pesquisaTipo(id_tipo);
           if (nodo_tipo == null) yyerror("(sem) tipo >" + id_tipo + "< nao conhecido");
           
           if (ts.pesquisa(id_var) != null) {
               yyerror("(sem) variavel >" + id_var + "< jah declarada");
           } else {
               /* Construtor de array de struct: (id, nElem, tipoBase, tipoStruct, tamanhoElem) */
               ts.insert(new TS_entry(id_var, n_elem, Parser.STRUCT, id_tipo, nodo_tipo.getTamanho()));
             }
         }
break;
case 18:
//#line 122 "exemploGC.y"
{
           /* Caso 2: Definição de tipo struct (struct Ponto { ... };) */
           Map<String, TS_entry> campos = (Map<String, TS_entry>)val_peek(2).obj;
           int tamanho_total = 0;
           for (TS_entry campo : campos.values()) {
               tamanho_total += campo.getTamanho();
           }
           
           if (ts.pesquisaTipo(val_peek(4).sval) != null) {
               yyerror("(sem) tipo struct >" + val_peek(4).sval + "< jah declarado");
           } else {
               ts.insert_tipo(new TS_entry(val_peek(4).sval, tamanho_total, campos));
           }
       }
break;
case 19:
//#line 136 "exemploGC.y"
{
            /* Variável struct (Ponto p1;) */
            String id_tipo = val_peek(2).sval;
            String id_var = val_peek(1).sval;
            
            TS_entry nodo_tipo = ts.pesquisaTipo(id_tipo);
            TS_entry nodo_var = ts.pesquisa(id_var);
            
            if (nodo_var != null) {
                yyerror("(sem) variavel >" + id_var + "< jah declarada");
            } else if (nodo_tipo == null) {
                yyerror("(sem) tipo >" + id_tipo + "< nao conhecido");
            } else {
              ts.insert(new TS_entry(id_var, nodo_tipo));          }
       }
break;
case 23:
//#line 161 "exemploGC.y"
{ System.out.println("\t\t# terminou o bloco..."); }
break;
case 24:
//#line 164 "exemploGC.y"
{ strTab.add(val_peek(2).sval);
                                System.out.println("\tMOVL $_str_"+strCount+"Len, %EDX"); 
				System.out.println("\tMOVL $_str_"+strCount+", %ECX"); 
                                System.out.println("\tCALL _writeLit"); 
				System.out.println("\tCALL _writeln"); 
                                strCount++;
				}
break;
case 25:
//#line 173 "exemploGC.y"
{ strTab.add(val_peek(0).sval);
                                System.out.println("\tMOVL $_str_"+strCount+"Len, %EDX"); 
				System.out.println("\tMOVL $_str_"+strCount+", %ECX"); 
                                System.out.println("\tCALL _writeLit"); 
				strCount++;
				}
break;
case 26:
//#line 181 "exemploGC.y"
{ 
			 System.out.println("\tPOPL %EAX"); 
			 System.out.println("\tCALL _write");	
			 System.out.println("\tCALL _writeln"); 
                        }
break;
case 27:
//#line 187 "exemploGC.y"
{
           /* 'ref' ($3) já empilhou o endereço correto */
           System.out.println("\tCALL _read");
           System.out.println("\tPOPL %EDX");
           System.out.println("\tMOVL %EAX, (%EDX)");
       }
break;
case 28:
//#line 194 "exemploGC.y"
{
				pRot.push(proxRot);  proxRot += 2;
				int rot_inicio = pRot.peek();
				int rot_fim = rot_inicio + 1;
				
				pLoopBreak.push(rot_fim);
				pLoopContinue.push(rot_inicio);
				
				System.out.printf("rot_%02d:\n", rot_inicio);
			}
break;
case 29:
//#line 205 "exemploGC.y"
{
					System.out.println("\tPOPL %EAX   # desvia se falso...");
					System.out.println("\tCMPL $0, %EAX");
					System.out.printf("\tJE rot_%02d\n", (int)pRot.peek()+1); /* Pula para rot_fim*/
			}
break;
case 30:
//#line 210 "exemploGC.y"
{
				/* Fim do corpo */
				System.out.printf("\tJMP rot_%02d\n", pRot.peek()); /* Pula para rot_inicio*/
				System.out.printf("rot_%02d:\n",(int)pRot.peek()+1); /* Define rot_fim*/
				
				/* Limpa pilhas */
				pRot.pop();
				pLoopBreak.pop();
				pLoopContinue.pop();
			}
break;
case 31:
//#line 221 "exemploGC.y"
{
				/* Prepara rótulos de início (continue) e fim (break) */
				int rot_inicio = proxRot;
				int rot_fim = proxRot + 1;
				proxRot += 2;
				
				pRot.push(rot_inicio); /* Salva rótulo de início para o JNE*/
				
				/* Salva rótulos para break/continue */
				pLoopBreak.push(rot_fim);
				pLoopContinue.push(rot_inicio);
				
				System.out.printf("rot_%02d:\n", rot_inicio);
			}
break;
case 32:
//#line 236 "exemploGC.y"
{
				/* Teste da condição */
				System.out.println("\tPOPL %EAX");
				System.out.println("\tCMPL $0, %EAX");
				System.out.printf("\tJNE rot_%02d\n", pRot.pop()); /* Pula para rot_inicio se V*/
				
				/* Define rótulo de fim (break) e limpa pilhas */
				System.out.printf("rot_%02d:\n", pLoopBreak.pop());
				pLoopContinue.pop();
			}
break;
case 33:
//#line 247 "exemploGC.y"
{
				if (pLoopBreak.empty())
					yyerror("(sem) comando break fora de loop");
				else
					System.out.printf("\tJMP rot_%02d\n", pLoopBreak.peek());
			}
break;
case 34:
//#line 254 "exemploGC.y"
{
				if (pLoopContinue.empty())
					yyerror("(sem) comando continue fora de loop");
				else
					System.out.printf("\tJMP rot_%02d\n", pLoopContinue.peek());
			}
break;
case 35:
//#line 261 "exemploGC.y"
{
				/* Ação 1: exp1 (init) - Define rótulos */
				int rot_teste = proxRot;
				int rot_continue = proxRot + 1; /* Incremento*/
				int rot_fim = proxRot + 2;
				int rot_corpo = proxRot + 3; 
				proxRot += 4; /* Avança o contador global*/
				
				pLoopBreak.push(rot_fim);
				pLoopContinue.push(rot_continue); 
				
				pRot.push(rot_fim);      /* 3*/
				pRot.push(rot_continue); /* 2*/
				pRot.push(rot_corpo);    /* 1 (Corpo)*/
				pRot.push(rot_teste);    /* 0 (Teste)*/
				
				System.out.printf("\tJMP rot_%02d\n", rot_teste); 
				System.out.printf("rot_%02d:\n", rot_corpo);    
          }
break;
case 36:
//#line 280 "exemploGC.y"
{
			/* Ação 2: Após exp2 (test) */
			System.out.printf("rot_%02d:\n", pRot.get(pRot.size()-2)); /* Define rot_teste*/
            System.out.println("\tPOPL %EAX");
            System.out.println("\tCMPL $0, %EAX");
            System.out.printf("\tJE rot_%02d\n", pRot.get(pRot.size()-4)); /* JMP para rot_fim (se F)*/
			System.out.printf("\tJMP rot_%02d\n", pRot.get(pRot.size()-3)); /* JMP para rot_corpo (se V)*/
          }
break;
case 37:
//#line 288 "exemploGC.y"
{
			/* Ação 3: Após exp3 (incremento) */
			System.out.printf("rot_%02d:\n", pRot.get(pRot.size()-3)); /* Define rot_continue*/
			System.out.printf("\tJMP rot_%02d\n", pRot.get(pRot.size()-2)); /* Pula para rot_teste*/
          }
break;
case 38:
//#line 293 "exemploGC.y"
{
			/* Ação 4: Após o corpo (cmd) - CORRIGINDO A PILHA */
			System.out.printf("rot_%02d:\n", pRot.pop()); /* Pop rot_corpo e define rótulo*/
			
			int rot_teste = pRot.pop(); 
			int rot_continue = pRot.pop(); 
			int rot_fim = pRot.pop();
			
			pLoopBreak.pop();
			pLoopContinue.pop();
			
			System.out.printf("\tJMP rot_%02d\n", rot_continue); /* Pula p/ incremento*/
			System.out.printf("rot_%02d:\n", rot_fim); /* Define rótulo do fim*/
          }
break;
case 39:
//#line 308 "exemploGC.y"
{	
				pRot.push(proxRot);  proxRot += 2;
								
				System.out.println("\tPOPL %EAX");
				System.out.println("\tCMPL $0, %EAX");
				System.out.printf("\tJE rot_%02d\n", pRot.peek());
			}
break;
case 40:
//#line 317 "exemploGC.y"
{
				System.out.printf("rot_%02d:\n",pRot.peek()+1);
				pRot.pop();
			}
break;
case 41:
//#line 324 "exemploGC.y"
{
					System.out.printf("\tJMP rot_%02d\n", pRot.peek()+1);
					System.out.printf("rot_%02d:\n",pRot.peek());
		}
break;
case 43:
//#line 331 "exemploGC.y"
{
		    System.out.printf("\tJMP rot_%02d\n", pRot.peek()+1);
				System.out.printf("rot_%02d:\n",pRot.peek());
				}
break;
case 44:
//#line 338 "exemploGC.y"
{ System.out.println("\tPUSHL $"+val_peek(0).sval); }
break;
case 45:
//#line 339 "exemploGC.y"
{ System.out.println("\tPUSHL $1"); }
break;
case 46:
//#line 340 "exemploGC.y"
{ System.out.println("\tPUSHL $0"); }
break;
case 47:
//#line 341 "exemploGC.y"
{ 
           System.out.println("\tPOPL %EAX");     /* Pega o endereço*/
           System.out.println("\tMOVL (%EAX), %EAX"); /* Carrega o valor do endereço*/
           System.out.println("\tPUSHL %EAX");    /* Empilha o valor*/
       }
break;
case 49:
//#line 347 "exemploGC.y"
{ gcExpNot(); }
break;
case 50:
//#line 349 "exemploGC.y"
{
          System.out.println("\tPOPL %EAX");     /* Valor da exp */
          System.out.println("\tMOVL _" + val_peek(2).sval + ", %EDX"); /* Valor da var */
          System.out.println("\tADDL %EAX, %EDX");   /* Calcula ID = ID + exp */
          System.out.println("\tMOVL %EDX, _" + val_peek(2).sval); /* Salva o novo valor */
          System.out.println("\tPUSHL %EDX");    /* PUSH O NOVO VALOR para encadear */
          }
break;
case 51:
//#line 357 "exemploGC.y"
{
         System.out.println("\tPOPL %EAX");     /* Valor (da exp)*/
         System.out.println("\tPOPL %EDX");     /* Endereço (da ref)*/
         System.out.println("\tMOVL %EAX, (%EDX)"); /* Salva Valor no Endereço*/
         System.out.println("\tPUSHL %EAX");    /* Empurra o valor de volta*/
     }
break;
case 52:
//#line 364 "exemploGC.y"
{
          System.out.println("\tMOVL _" + val_peek(0).sval + ", %EAX");
          System.out.println("\tADDL $1, %EAX");
          System.out.println("\tMOVL %EAX, _" + val_peek(0).sval);
          System.out.println("\tPUSHL %EAX");
      }
break;
case 53:
//#line 371 "exemploGC.y"
{
          System.out.println("\tMOVL _" + val_peek(1).sval + ", %EAX");
          System.out.println("\tPUSHL %EAX"); /* Empurra valor antigo */
          System.out.println("\tADDL $1, %EAX");
          System.out.println("\tMOVL %EAX, _" + val_peek(1).sval);
      }
break;
case 54:
//#line 378 "exemploGC.y"
{
          System.out.println("\tMOVL _" + val_peek(0).sval + ", %EAX");
          System.out.println("\tSUBL $1, %EAX");
          System.out.println("\tMOVL %EAX, _" + val_peek(0).sval);
          System.out.println("\tPUSHL %EAX");
      }
break;
case 55:
//#line 385 "exemploGC.y"
{
          System.out.println("\tMOVL _" + val_peek(1).sval + ", %EAX");
          System.out.println("\tPUSHL %EAX"); /* Empurra valor antigo */
          System.out.println("\tSUBL $1, %EAX");
          System.out.println("\tMOVL %EAX, _" + val_peek(1).sval);
      }
break;
case 56:
//#line 392 "exemploGC.y"
{ gcExpArit('+'); }
break;
case 57:
//#line 393 "exemploGC.y"
{ gcExpArit('-'); }
break;
case 58:
//#line 394 "exemploGC.y"
{ gcExpArit('*'); }
break;
case 59:
//#line 395 "exemploGC.y"
{ gcExpArit('/'); }
break;
case 60:
//#line 396 "exemploGC.y"
{ gcExpArit('%'); }
break;
case 61:
//#line 398 "exemploGC.y"
{ gcExpRel('>'); }
break;
case 62:
//#line 399 "exemploGC.y"
{ gcExpRel('<'); }
break;
case 63:
//#line 400 "exemploGC.y"
{ gcExpRel(EQ); }
break;
case 64:
//#line 401 "exemploGC.y"
{ gcExpRel(LEQ); }
break;
case 65:
//#line 402 "exemploGC.y"
{ gcExpRel(GEQ); }
break;
case 66:
//#line 403 "exemploGC.y"
{ gcExpRel(NEQ); }
break;
case 67:
//#line 405 "exemploGC.y"
{ gcExpLog(OR); }
break;
case 68:
//#line 406 "exemploGC.y"
{ gcExpLog(AND); }
break;
case 69:
//#line 408 "exemploGC.y"
{ 
      pRot.push(proxRot); proxRot += 2; /* Reserva R_else e R_fim*/
      System.out.println("\tPOPL %EAX");
      System.out.println("\tCMPL $0, %EAX");
      /* Pula para R_else se Falso (Zero) */
      System.out.printf("\tJE rot_%02d\n", pRot.peek()); 
    }
break;
case 70:
//#line 415 "exemploGC.y"
{
        System.out.printf("\tJMP rot_%02d\n", pRot.peek()+1); /* Pula para R_fim*/
        System.out.printf("rot_%02d:\n", pRot.peek()); /* Define R_else*/
    }
break;
case 71:
//#line 419 "exemploGC.y"
{ /* Ação FINAL */
        System.out.printf("rot_%02d:\n", pRot.peek()+1); /* Define R_fim*/
        pRot.pop();
    }
break;
case 74:
//#line 434 "exemploGC.y"
{
          /* Var simples. Empilha o endereço. */
          TS_entry nodo = ts.pesquisa(val_peek(0).sval);
          if (nodo == null) yyerror("(sem) variavel >" + val_peek(0).sval + "< nao declarada");
          System.out.println("\tPUSHL $_" + val_peek(0).sval);
      }
break;
case 75:
//#line 440 "exemploGC.y"
{
          /* Campo de struct (ex: p1.x) */
          String id_var = val_peek(2).sval;
          String id_campo = val_peek(0).sval;
          
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
break;
case 76:
//#line 460 "exemploGC.y"
{
          String id_var = val_peek(3).sval;
          
          TS_entry nodo_var = ts.pesquisa(id_var);
          if (nodo_var == null) yyerror("(sem) array >" + id_var + "< nao declarado");
          if (nodo_var.getTipo() != Parser.ARRAY) yyerror("(sem) >" + id_var + "< nao eh um array");

          /* GERA CÓDIGO: (base + (indice * 4)) */
          System.out.println("\tPOPL %EAX");     /* EAX = indice (da 'exp')*/
          System.out.println("\tIMULL $4, %EAX");  /* EAX = indice * 4*/
          System.out.println("\tADDL $_" + id_var + ", %EAX"); /* EAX = _v + (indice * 4)*/
          System.out.println("\tPUSHL %EAX");    /* Empilha o endereço final*/
      }
break;
case 77:
//#line 474 "exemploGC.y"
{
          TS_entry nodo_var = ts.pesquisa(val_peek(5).sval); /* p1*/
          if (nodo_var == null) yyerror("(sem) variavel >" + val_peek(5).sval + "< nao declarada");
          TS_entry nodo_tipo = ts.pesquisaTipo(nodo_var.getTipoStruct()); /* tipo de p1*/
          if (nodo_tipo == null) yyerror("(sem) tipo >" + nodo_var.getTipoStruct() + "< nao eh um struct");
          TS_entry nodo_campo = nodo_tipo.getCampo(val_peek(3).sval); /* notas*/
          if (nodo_campo == null) yyerror("(sem) campo >" + val_peek(3).sval + "< nao existe");
          if (nodo_campo.getTipo() != Parser.ARRAY) yyerror("(sem) campo >" + val_peek(3).sval + "< nao eh um array");

          System.out.println("\tPOPL %EAX"); /* EAX = indice (da exp)*/
          System.out.println("\tIMULL $" + nodo_campo.getTamanhoElemento() + ", %EAX"); /* EAX = indice * 4*/
          
          System.out.println("\tMOVL $_" + val_peek(5).sval + ", %EDX"); /* EDX = end base (p1)*/
          System.out.println("\tADDL $" + nodo_campo.getOffset() + ", %EDX"); /* EDX = end base + offset */
          
          System.out.println("\tADDL %EDX, %EAX"); /* EAX = (p1+offset_notas) + (indice*4)*/
          System.out.println("\tPUSHL %EAX");
      }
break;
case 78:
//#line 493 "exemploGC.y"
{
          TS_entry nodo_var = ts.pesquisa(val_peek(5).sval); /* lista*/
          if (nodo_var == null) yyerror("(sem) array >" + val_peek(5).sval + "< nao declarado");
          if (nodo_var.getTipo() != Parser.ARRAY) yyerror("(sem) >" + val_peek(5).sval + "< nao eh um array");
          
          TS_entry nodo_tipo = ts.pesquisaTipo(nodo_var.getTipoStruct()); /* Ponto*/
          if (nodo_tipo == null) yyerror("(sem) tipo base >" + nodo_var.getTipoStruct() + "< nao eh struct");
          
          TS_entry nodo_campo = nodo_tipo.getCampo(val_peek(0).sval); /* x*/
          if (nodo_campo == null) yyerror("(sem) campo >" + val_peek(0).sval + "< nao existe");
          
          int tamanho_struct = nodo_var.getTamanhoElemento();
          int offset_campo = nodo_campo.getOffset();

          System.out.println("\tPOPL %EAX"); /* EAX = indice (da exp)*/
          System.out.println("\tIMULL $" + tamanho_struct + ", %EAX"); /* EAX = indice * tam_struct*/
          
          System.out.println("\tADDL $_" + val_peek(5).sval + ", %EAX"); /* EAX = _lista + (indice * tam_struct)*/
          
          System.out.println("\tADDL $" + offset_campo + ", %EAX"); /* EAX = (base + ... ) + offset_x*/
          System.out.println("\tPUSHL %EAX");
      	}
break;
case 80:
//#line 520 "exemploGC.y"
{ System.out.println("\tPUSHL $1"); }
break;
//#line 1529 "Parser.java"
//########## END OF USER-SUPPLIED ACTIONS ##########
    }//switch
    //#### Now let's reduce... ####
    if (yydebug) debug("reduce");
    state_drop(yym);             //we just reduced yylen states
    yystate = state_peek(0);     //get new state
    val_drop(yym);               //corresponding value drop
    yym = yylhs[yyn];            //select next TERMINAL(on lhs)
    if (yystate == 0 && yym == 0)//done? 'rest' state and at first TERMINAL
      {
      if (yydebug) debug("After reduction, shifting from state 0 to state "+YYFINAL+"");
      yystate = YYFINAL;         //explicitly say we're done
      state_push(YYFINAL);       //and save it
      val_push(yyval);           //also save the semantic value of parsing
      if (yychar < 0)            //we want another character?
        {
        yychar = yylex();        //get next character
        if (yychar<0) yychar=0;  //clean, if necessary
        if (yydebug)
          yylexdebug(yystate,yychar);
        }
      if (yychar == 0)          //Good exit (if lex returns 0 ;-)
         break;                 //quit the loop--all DONE
      }//if yystate
    else                        //else not done yet
      {                         //get next state and push, for next yydefred[]
      yyn = yygindex[yym];      //find out where to go
      if ((yyn != 0) && (yyn += yystate) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yystate)
        yystate = yytable[yyn]; //get new state
      else
        yystate = yydgoto[yym]; //else go to new defred
      if (yydebug) debug("after reduction, shifting from state "+state_peek(0)+" to state "+yystate+"");
      state_push(yystate);     //going again, so push state & val...
      val_push(yyval);         //for next action
      }
    }//main loop
  return 0;//yyaccept!!
}
//## end of method parse() ######################################



//## run() --- for Thread #######################################
/**
 * A default run method, used for operating this parser
 * object in the background.  It is intended for extending Thread
 * or implementing Runnable.  Turn off with -Jnorun .
 */
public void run()
{
  yyparse();
}
//## end of method run() ########################################



//## Constructors ###############################################
/**
 * Default constructor.  Turn off with -Jnoconstruct .

 */
public Parser()
{
  //nothing to do
}


/**
 * Create a parser, setting the debug to true or false.
 * @param debugMe true for debugging, false for no debug.
 */
public Parser(boolean debugMe)
{
  yydebug=debugMe;
}
//###############################################################



}
//################### END OF CLASS ##############################
