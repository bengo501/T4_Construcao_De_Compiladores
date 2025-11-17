import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class TabSimb {
    /*
     'lista' (global) para variáveis (ex: p1)
     'tipos' para definições de tipos (ex: Ponto)
     */
    private ArrayList<TS_entry> lista;
    private Map<String, TS_entry> tipos; // Armazena definições de struct

    public TabSimb() {
        lista = new ArrayList<TS_entry>();
        tipos = new HashMap<String, TS_entry>();
    }

    public void insert(TS_entry nodo) {
        lista.add(nodo);
    }
    
    public void insert_tipo(TS_entry nodo) {
        tipos.put(nodo.id, nodo);
    }

    public void listar() {
        System.out.println("\n\n# Listagem da Tabela de Simbolos (Variaveis):");
        for (TS_entry nodo : lista) {
            System.out.println("# " + nodo);
        }
        
        System.out.println("\n# Listagem da Tabela de Tipos (Structs):");
        for (TS_entry nodo : tipos.values()) {
            System.out.println("# " + nodo);
        }
    }

    public TS_entry pesquisa(String umId) {
        for (TS_entry nodo : lista) {
            if (nodo.id.equals(umId)) {
                return nodo;
            }
        }
        return null;
    }
    
    public TS_entry pesquisaTipo(String id_tipo) {
        return tipos.get(id_tipo);
    }

    public void geraGlobais() {
        System.out.println("#");
        System.out.println("# variaveis globais");
        System.out.println("#");
        for (TS_entry nodo : lista) {
            // Usa o tamanho armazenado no nodo, não mais ".zero 4"
            System.out.println("_" + nodo.id + ": .zero " + nodo.getTamanho());
        }
    }
}