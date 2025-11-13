#helper para importar gerador_codigo de qualquer lugar
import sys
import os

def setup_import_path():
    #configura o path para importar gerador_codigo
    # obtém o diretório do arquivo atual
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    # diretório raiz do projeto (sobe dois níveis de src/teste/)
    dir_raiz = os.path.dirname(os.path.dirname(dir_atual))
    # caminho para src/
    dir_src = os.path.join(dir_raiz, 'src')
    
    # adiciona src/ ao path se o arquivo gerador_codigo.py existir
    if os.path.exists(os.path.join(dir_src, 'gerador_codigo.py')):
        if dir_src not in sys.path:
            sys.path.insert(0, dir_src)
        return dir_src
    # se não, tenta o diretório pai (caso esteja em src/)
    elif os.path.exists(os.path.join(os.path.dirname(dir_atual), 'gerador_codigo.py')):
        dir_pai = os.path.dirname(dir_atual)
        if dir_pai not in sys.path:
            sys.path.insert(0, dir_pai)
        return dir_pai
    # último recurso: diretório atual
    else:
        if dir_atual not in sys.path:
            sys.path.insert(0, dir_atual)
        return dir_atual

# configura o path automaticamente ao importar este módulo
setup_import_path()

