# T4 Compiladores

## Integrantes:
Bernardo Klein, João Pedro Aiolfi, Lucas Brenner e Lucas Lantmann

## Como Rodar o projeto:

make


java Parser collatz.cmm > collatz.s

# 1. Monta o .s e cria um executável "collatz"
gcc -m32 -o collatz collatz.s

# 2. Roda o programa
./collatz