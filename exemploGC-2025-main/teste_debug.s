.text

#	 Bernardo Klein Heitz, João Pedro Aiolfi de Figueiredo, Lucas Teixeira Brenner e Lucas Langer Lantmann 
#

.GLOBL _start


_start:
	MOVL $_str_0Len, %EDX
	MOVL $_str_0, %ECX
	CALL _writeLit
	CALL _writeln
	MOVL $_str_1Len, %EDX
	MOVL $_str_1, %ECX
	CALL _writeLit
	CALL _writeln
	PUSHL $_i
	PUSHL $1
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	JMP rot_01
rot_04:
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
rot_04:
	POPL %EAX
	CMPL $0, %EAX
	JE rot_03
	JMP rot_02
	MOVL _i, %EAX
	PUSHL %EAX
	ADDL $1, %EAX
	MOVL %EAX, _i
rot_02:
	JMP rot_04
	MOVL $_str_2Len, %EDX
	MOVL $_str_2, %ECX
	CALL _writeLit
	PUSHL $_i
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EAX
	CALL _write
	CALL _writeln
rot_01:
	JMP rot_02
rot_03:
	PUSHL $_a
	PUSHL $10
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	PUSHL $_b
	PUSHL $11
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	PUSHL $_c
	PUSHL $9
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	PUSHL $_me
	PUSHL $_a
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	PUSHL $_b
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
	POPL %EAX
	POPL %EDX
	CMPL %EAX, %EDX
	MOVL $0, %EAX
	SETLE %AL
	PUSHL %EAX
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	PUSHL $_a
	POPL %EAX
	MOVL (%EAX), %EAX
	PUSHL %EAX
