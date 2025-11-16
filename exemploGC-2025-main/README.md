# T4 Compiladores

## Integrantes:
Bernardo Klein, João Pedro Aiolfi, Lucas Brenner e Lucas Lantmann

## Como Rodar o projeto:
make clean
chmod +x ./yacc.linux
make
java Parser collatz.cmm > collatz.s

sudo apt-get update && sudo apt-get install -y gcc-multilib

gcc -m32 -o collatz collatz.s

./collatz

