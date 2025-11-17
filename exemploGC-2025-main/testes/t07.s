.text

#	 Bernardo Klein Heitz, João Pedro Aiolfi de Figueiredo, Lucas Teixeira Brenner e Lucas Langer Lantmann 
#

.GLOBL _start


_start:
	PUSHL $_a
	PUSHL $_b
	PUSHL $_c
	PUSHL $10
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	POPL %EAX
	POPL %EDX
	MOVL %EAX, (%EDX)
	PUSHL %EAX
	MOVL _b, %EAX
	ADDL $1, %EAX
	MOVL %EAX, _b
	PUSHL %EAX
	MOVL _c, %EAX
	PUSHL %EAX
	SUBL $1, %EAX
	MOVL %EAX, _c
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
