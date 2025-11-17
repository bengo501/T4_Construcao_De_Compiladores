.text

#	 Bernardo Klein Heitz, João Pedro Aiolfi de Figueiredo, Lucas Teixeira Brenner e Lucas Langer Lantmann 
#

.GLOBL _start


_start:
	MOVL $_str_0Len, %EDX
	MOVL $_str_0, %ECX
	CALL _writeLit
	CALL _writeln
	PUSHL $_i
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_01
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $5
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
rot_01:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_04
	JMP rot_02
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EBX
	PUSHL %EBX
	ADDL $1, %EBX
	MOVL %EBX, (%EAX)
rot_03:
	JMP rot_01
	MOVL $_str_1Len, %EDX
	MOVL $_str_1, %ECX
	CALL _writeLit
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EAX
	CALL _write
	CALL _writeln
	JMP rot_02
rot_01:
	MOVL $_str_2Len, %EDX
	MOVL $_str_2, %ECX
	CALL _writeLit
	CALL _writeln
	MOVL $_str_3Len, %EDX
	MOVL $_str_3, %ECX
	CALL _writeLit
	CALL _writeln
	PUSHL $_i
	PUSHL $10
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_05
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $13
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
rot_05:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_08
	JMP rot_06
rot_07:
	JMP rot_05
	MOVL $_str_4Len, %EDX
	MOVL $_str_4, %ECX
	CALL _writeLit
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EAX
	CALL _write
	CALL _writeln
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EBX
	PUSHL %EBX
	ADDL $1, %EBX
	MOVL %EBX, (%EAX)
		# terminou o bloco...
	JMP rot_06
rot_05:
	MOVL $_str_5Len, %EDX
	MOVL $_str_5, %ECX
	CALL _writeLit
	CALL _writeln
	MOVL $_str_6Len, %EDX
	MOVL $_str_6, %ECX
	CALL _writeLit
	CALL _writeln
	PUSHL $_i
	PUSHL $100
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_09
	PUSHL $1
rot_09:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_12
	JMP rot_10
rot_11:
	JMP rot_09
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EBX
	PUSHL %EBX
	ADDL $1, %EBX
	MOVL %EBX, (%EAX)
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $105
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETL  %AL
	PUSHL %EAX
	POPL %EAX
	CMPL $0, %EAX
	JE rot_13
	JMP rot_11
	JMP rot_14
rot_13:
rot_14:
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $110
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETG  %AL
	PUSHL %EAX
	POPL %EAX
	CMPL $0, %EAX
	JE rot_15
	JMP rot_12
	JMP rot_16
rot_15:
rot_16:
	MOVL $_str_7Len, %EDX
	MOVL $_str_7, %ECX
	CALL _writeLit
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EAX
	CALL _write
	CALL _writeln
		# terminou o bloco...
	JMP rot_10
rot_09:
	MOVL $_str_8Len, %EDX
	MOVL $_str_8, %ECX
	CALL _writeLit
	CALL _writeln
	MOVL $_str_9Len, %EDX
	MOVL $_str_9, %ECX
	CALL _writeLit
	CALL _writeln
	PUSHL $_i
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_17
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $3
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
rot_17:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_20
	JMP rot_18
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EBX
	PUSHL %EBX
	ADDL $1, %EBX
	MOVL %EBX, (%EAX)
rot_19:
	JMP rot_17
	PUSHL $_j
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_21
	PUSHL $_j
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $3
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
rot_21:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_24
	JMP rot_22
	PUSHL $_j
	POPL %EAX
	MOVL (%EAX), %EBX
	PUSHL %EBX
	ADDL $1, %EBX
	MOVL %EBX, (%EAX)
rot_23:
	JMP rot_21
	MOVL $_str_10Len, %EDX
	MOVL $_str_10, %ECX
	CALL _writeLit
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $_j
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EBX
	POPL %EAX
	IMULL %EBX, %EAX
	PUSHL %EAX
	POPL %EAX
	CALL _write
	CALL _writeln
	JMP rot_22
rot_21:
	JMP rot_18
rot_17:
	MOVL $_str_11Len, %EDX
	MOVL $_str_11, %ECX
	CALL _writeLit
	CALL _writeln
	MOVL $_str_12Len, %EDX
	MOVL $_str_12, %ECX
	CALL _writeLit
	CALL _writeln
	PUSHL $_i
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_25
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $3
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
rot_25:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_28
	JMP rot_26
	PUSHL $_i
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL (%EDX), %EBX
	ADDL %EAX, %EBX
	MOVL %EBX, (%EDX)
	PUSHL %EBX
rot_27:
	JMP rot_25
	PUSHL $_j
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_29
	PUSHL $_j
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $3
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
rot_29:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_32
	JMP rot_30
	PUSHL $_j
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL (%EDX), %EBX
	ADDL %EAX, %EBX
	MOVL %EBX, (%EDX)
	PUSHL %EBX
rot_31:
	JMP rot_29
	MOVL $_str_13Len, %EDX
	MOVL $_str_13, %ECX
	CALL _writeLit
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $_j
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EBX
	POPL %EAX
	IMULL %EBX, %EAX
	PUSHL %EAX
	POPL %EAX
	CALL _write
	CALL _writeln
	JMP rot_30
rot_29:
	JMP rot_26
rot_25:



#
# devolve o controle para o SO (final da main)
#
	mov $0, %ebx
	mov $1, %eax
	int $0x80


#
# Funcoes da biblioteca (IO)
#


_writeln:
	MOVL $__fim_msg, %ECX
	DECL %ECX
	MOVB $10, (%ECX)
	MOVL $1, %EDX
	JMP _writeLit
_write:
	MOVL $__fim_msg, %ECX
	MOVL $0, %EBX
	CMPL $0, %EAX
	JGE _write3
	NEGL %EAX
	MOVL $1, %EBX
_write3:
	PUSHL %EBX
	MOVL $10, %EBX
_divide:
	MOVL $0, %EDX
	IDIVL %EBX
	DECL %ECX
	ADD $48, %DL
	MOVB %DL, (%ECX)
	CMPL $0, %EAX
	JNE _divide
	POPL %EBX
	CMPL $0, %EBX
	JE _print
	DECL %ECX
	MOVB $'-', (%ECX)
_print:
	MOVL $__fim_msg, %EDX
	SUBL %ECX, %EDX
_writeLit:
	MOVL $1, %EBX
	MOVL $4, %EAX
	int $0x80
	RET
_read:
	MOVL $15, %EDX
	MOVL $__msg, %ECX
	MOVL $0, %EBX
	MOVL $3, %EAX
	int $0x80
	MOVL $0, %EAX
	MOVL $0, %EBX
	MOVL $0, %EDX
	MOVL $__msg, %ECX
	CMPB $'-', (%ECX)
	JNE _reading
	INCL %ECX
	INC %BL
_reading:
	MOVB (%ECX), %DL
	CMP $10, %DL
	JE _fimread
	SUB $48, %DL
	IMULL $10, %EAX
	ADDL %EDX, %EAX
	INCL %ECX
	JMP _reading
_fimread:
	CMPB $1, %BL
	JNE _fimread2
	NEGL %EAX
_fimread2:
	RET



#
# area de dados
#
.data
#
# variaveis globais
#
#
# variaveis globais
#
_i: .zero 4
_j: .zero 4

#
# area de literais
#
__msg:
	.zero 30
__fim_msg:
	.byte 0


_str_0:
	 .ascii "> teste 1 "
_str_0Len = . - _str_0
_str_1:
	 .ascii " i: "
_str_1Len = . - _str_1
_str_2:
	 .ascii " "
_str_2Len = . - _str_2
_str_3:
	 .ascii "> teste 2 "
_str_3Len = . - _str_3
_str_4:
	 .ascii " i: "
_str_4Len = . - _str_4
_str_5:
	 .ascii " "
_str_5Len = . - _str_5
_str_6:
	 .ascii "> teste 3 "
_str_6Len = . - _str_6
_str_7:
	 .ascii " i: "
_str_7Len = . - _str_7
_str_8:
	 .ascii " "
_str_8Len = . - _str_8
_str_9:
	 .ascii "> teste 4 "
_str_9Len = . - _str_9
_str_10:
	 .ascii " - "
_str_10Len = . - _str_10
_str_11:
	 .ascii " "
_str_11Len = . - _str_11
_str_12:
	 .ascii "> teste 5 "
_str_12Len = . - _str_12
_str_13:
	 .ascii " - "
_str_13Len = . - _str_13
