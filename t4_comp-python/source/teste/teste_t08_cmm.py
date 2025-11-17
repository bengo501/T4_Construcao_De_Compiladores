#teste t08.cmm: do-while
#do {
#    write("Informe um numero <= 0: ");
#    read( num );
#    write("Valor lido: ", num);
#} while ( num > 0 );
import _import_helper
from gerador_codigo import GeradorCodigo

def gerar_teste():
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_variavel("num", "integer", 4)
    
    # do {
    rotulo_inicio, rotulo_fim = gc.inicio_do_while()
    
    # corpo do do-while (write e read não implementados, então só a estrutura)
    # write("Informe um numero <= 0: ");
    # read( num );
    # write("Valor lido: ", num);
    
    # } while ( num > 0 );
    gc.carregar_variavel("num")
    gc.ldc(0)
    gc.grt()  # num > 0
    gc.fim_do_while()
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste t08.cmm: do-while")
    print()
    print("programa fonte:")
    print("int num;")
    print("do {")
    print("    write(\"Informe um numero <= 0: \");")
    print("    read( num );")
    print("    write(\"Valor lido: \", num);")
    print("} while ( num > 0 );")
    print()
    print("codigo gerado:")
    print(gerar_teste())

