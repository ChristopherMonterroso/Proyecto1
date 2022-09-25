from enum import Enum
import re
class tokens(Enum):
    TK_MENOR = "<"
    TK_E_NUMERO = "Numero"
    TK_MAYOR = ">"
    TK_NUMERO = "[0-9]*[.]?[0-9]*"
    TK_BARRAINV = "/"
    TK_E_OPERACION = "Operacion"
    TK_IGUAL = "="
    TK_OP_SUMA = "SUMA",
    TK_OP_MOD = "MOD",
    TK_OP_RESTA = "RESTA"
    TK_OP_MULTIPLICACION = "MULTIPLICACION"
    TK_E_TIPO = "Tipo"
    TK_OP_POTENCIA= "POTENCIA"
    TK_OP_RAIZ="RAIZ"
    TK_OP_INVERSO="INVERSO"
    TK_OP_SENO="SENO"
    TK_OP_COSENO="COSENO"
    TK_OP_TANGENTE="TANGENTE"
    TK_E_TEXTO="Texto"
    TK_E_PARRAFO="[a-zA-Z,À-ÿ\u00f1\u00d1,'+'-'-','*',0.0-9.0*,':','%','=','/','^','√','(',')']*"
    TK_E_Funcion="Funcion"
    TK_E_ESTILO="Estilo"
    TK_E_Titulo="Titulo"
    TK_DEMAS="(\s*[a-zA-ZÀ-ÿ\u00f1\u00d10-9\!\¡\#\$\%\&\(\)\\+\,\-\.\/\:\;\<\=\>\?\¿\[\\\]\^\_\{\|\}\~](\s*[a-zA-ZÀ-ÿ\u00f1\u00d10-9\!\¡\#\$\%\&\(\)\\+\,\-\.\/\:\;\<\=\>\?\¿\[\\\]\^\_\{\|\}\~]+)"
    TK_MAYUS="[A-Z]*"