import java.util.HashMap;
import java.util.Map;

public class TS_entry {
    public String id;
    public int tipo;        // INT, BOOL, STRUCT, ARRAY
    public int tamanho;     // Tamanho total em bytes
    public int offset;      // Para campos de struct
    
    // Para Structs
    public String tipo_struct; // Nome do tipo (ex: "Ponto")
    public Map<String, TS_entry> campos; // Mapa de campos

    // Para Arrays
    public int nElem;       // Número de elementos
    public int tipoBase;    // Tipo dos elementos (INT, BOOL, STRUCT)
    public int tamanhoElemento; // Tamanho de cada elemento (ex: 4 p/ int, 8 p/ Ponto)

    /* Construtor para VAR SIMPLES (int x) */
    public TS_entry(String id, int tipo) {
        this.id = id;
        this.tipo = tipo;
        this.tamanho = 4; // Padrão 4 bytes
        this.nElem = -1;
    }

    /* Construtor para TIPO STRUCT (struct Ponto { ... }) */
    public TS_entry(String id_tipo, int tamanho_total, Map<String, TS_entry> campos_struct) {
        this.id = id_tipo;
        this.tipo = Parser.STRUCT; 
        this.tipo_struct = id_tipo;
        this.tamanho = tamanho_total;
        this.campos = campos_struct;
        this.nElem = -1;
    }

    /* Construtor para VAR STRUCT (Ponto p1) */
    public TS_entry(String id_var, TS_entry tipo_struct_info) {
        this.id = id_var;
        this.tipo = Parser.STRUCT; 
        this.tipo_struct = tipo_struct_info.id;
        this.tamanho = tipo_struct_info.getTamanho();
        this.campos = null;
        this.nElem = -1;
    }

    /* Construtor para CAMPO SIMPLES (int x;) */
    public TS_entry(String id_campo, int tipo_campo, int offset_campo) {
        this.id = id_campo;
        this.tipo = tipo_campo;
        this.tamanho = 4; // Padrão 4 bytes
        this.offset = offset_campo;
        this.nElem = -1;
    }

    /* Construtor para CAMPO ARRAY (int notas[4];) */
    public TS_entry(String id_campo, int tipo_campo, int offset_campo, int nElem) {
        this.id = id_campo;
        this.tipo = Parser.ARRAY;
        this.tipoBase = tipo_campo;
        this.nElem = nElem;
        this.tamanhoElemento = 4; // Assume array de int/bool no campo
        this.tamanho = nElem * this.tamanhoElemento;
        this.offset = offset_campo;
    }
    
    /* Construtor para VAR ARRAY (int v[10] ou Ponto p[10]) */
    public TS_entry(String id, int nElem, int tipoBase, String tipoStruct, int tamanhoElem) {
        this.id = id;
        this.tipo = Parser.ARRAY;
        this.nElem = nElem;
        this.tipoBase = tipoBase;
        this.tipo_struct = tipoStruct;
        this.tamanhoElemento = tamanhoElem;
        this.tamanho = nElem * tamanhoElem;
    }
    
    public String toString() {
        if (tipo == Parser.ARRAY && tipoBase == Parser.STRUCT) {
            return "VAR_ARRAY_STRUCT: " + id + " (Tipo: " + tipo_struct + ", N_Elem: " + nElem + ", Tam: " + tamanho + ")";
        } else if (tipo == Parser.ARRAY) {
            return "VAR_ARRAY_SIMPLES: " + id + " (TipoBase: " + tipoBase + ", N_Elem: " + nElem + ", Tam: " + tamanho + ")";
        } else if (campos != null) {
            return "TIPO_STRUCT: " + id + " (Tam: " + tamanho + ") Campos: " + campos.keySet();
        } else if (tipo_struct != null) {
            return "VAR_STRUCT: " + id + " (Tipo: " + tipo_struct + ", Tam: " + tamanho + ")";
        }
        return "VAR_SIMPLES: " + id + " (Tipo: " + tipo + ", Tam: " + tamanho + ")";
    }

    // Getters
    public int getTamanho() { return this.tamanho; }
    public Map<String, TS_entry> getCampos() { return this.campos; }
    public TS_entry getCampo(String nome) {
        if (campos != null) return campos.get(nome);
        return null;
    }
    public int getOffset() { return this.offset; }
    public String getTipoStruct() { return this.tipo_struct; }
    public int getTipo() { return this.tipo; }
    public int getTamanhoElemento() { return this.tamanhoElemento; }
}