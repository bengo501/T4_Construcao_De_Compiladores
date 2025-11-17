#script de regressao para os exemplos em `exemplo/`
#varre os arquivos `teste_*.txt`, executa a funcao correspondente em `exemplos_teste`
#e compara o codigo gerado com o snapshot esperado.
from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
EXEMPLO_DIR = PROJECT_ROOT / "exemplo"
EXPECTED_DIR = EXEMPLO_DIR / "expected"

@dataclass
class ResultadoTeste:
    nome: str
    arquivo_txt: Path
    esperado: str
    obtido: str
    sucesso: bool
    mensagem: str = ""

def normalizar_saida(texto: str) -> str:    #normaliza para comparar: remove espacos extras e usa lf.
    linhas = [linha.rstrip() for linha in texto.strip().splitlines()]
    return "\n".join(linhas)

def extrair_snapshot(path_txt: Path) -> str:    #extrai o trecho apos 'código gerado:'
    conteudo = path_txt.read_text(encoding="utf-8")
    marcador = "código gerado:"
    if marcador not in conteudo:
        raise ValueError(f"'{marcador}' nao encontrado em {path_txt}")
    trecho = conteudo.split(marcador, 1)[1].strip()
    if not trecho:
        raise ValueError(f"snapshot vazio em {path_txt}")
    return trecho

def salvar_snapshot(nome: str, snapshot: str) -> None:    #salva o snapshot
    EXPECTED_DIR.mkdir(parents=True, exist_ok=True)
    destino = EXPECTED_DIR / f"{nome}.txt"
    destino.write_text(snapshot + "\n", encoding="utf-8")

def executar_testes() -> list[ResultadoTeste]:    #executa os testes
    if not EXEMPLO_DIR.exists():
        raise FileNotFoundError(f"diretorio {EXEMPLO_DIR} nao encontrado")

    sys.path.insert(0, str(BASE_DIR))
    modulo = importlib.import_module("exemplos_teste")

    resultados: list[ResultadoTeste] = [] #lista de resultados  
    arquivos_txt = sorted(EXEMPLO_DIR.glob("teste_*.txt"))

    if not arquivos_txt:
        raise FileNotFoundError("nenhum arquivo teste_*.txt encontrado em exemplo/")

    for arquivo_txt in arquivos_txt:
        nome_base = arquivo_txt.stem  # ex: teste_01_expressao_atribuicao
        try:
            func = getattr(modulo, nome_base)
        except AttributeError as exc:
            resultados.append(
                ResultadoTeste(
                    nome=nome_base,
                    arquivo_txt=arquivo_txt,
                    esperado="",
                    obtido="",
                    sucesso=False,
                    mensagem=f"funcao {nome_base} nao encontrada em exemplos_teste ({exc})",
                )
            )
            continue

        try:
            esperado = normalizar_saida(extrair_snapshot(arquivo_txt))
        except Exception as exc:  # pylint: disable=broad-except
            resultados.append(
                ResultadoTeste(
                    nome=nome_base,
                    arquivo_txt=arquivo_txt,
                    esperado="",
                    obtido="",
                    sucesso=False,
                    mensagem=f"erro ao extrair snapshot: {exc}",
                )
            )
            continue

        try:
            obtido_bruto = func()
        except Exception as exc:  # pylint: disable=broad-except
            resultados.append(
                ResultadoTeste(
                    nome=nome_base,
                    arquivo_txt=arquivo_txt,
                    esperado=esperado,
                    obtido="",
                    sucesso=False,
                    mensagem=f"erro ao executar funcao {nome_base}: {exc}",
                )
            )
            continue

        obtido = normalizar_saida(obtido_bruto)
        salvar_snapshot(nome_base, obtido)

        sucesso = obtido == esperado
        mensagem = "" if sucesso else "saida divergente"
        resultados.append(
            ResultadoTeste(
                nome=nome_base,
                arquivo_txt=arquivo_txt,
                esperado=esperado,
                obtido=obtido,
                sucesso=sucesso,
                mensagem=mensagem,
            )
        )

    return resultados

def main() -> int:
    print("=" * 60)
    print("regressao dos exemplos (exemplo/teste_*.txt)")
    print("=" * 60)

    resultados = executar_testes()

    total = len(resultados)
    sucesso = sum(1 for r in resultados if r.sucesso)
    falhas = total - sucesso

    for resultado in resultados:
        status = "[ok]" if resultado.sucesso else "[erro]"
        print(f"\n{status} {resultado.nome}")
        if not resultado.sucesso and resultado.mensagem:
            print(f"  motivo: {resultado.mensagem}")
            if resultado.esperado:
                print("  esperado:")
                print(resultado.esperado)
            if resultado.obtido:
                print("  obtido:")
                print(resultado.obtido)

    print("\n" + "=" * 60)
    print(f"testes executados: {total}")
    print(f"testes passaram:  {sucesso}")
    print(f"testes falharam:  {falhas}")

    return 0 if falhas == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

