from ast import Pass
from email import message
from tkinter import messagebox
from ReporteHTML import reporte
from Calculadora import calculo
import re
from Token import tokens as L_tokens
from Error import error as err
from enum import Enum
listaErroresLexicos = []
lista_total=[]
lista_operacion=[]
lista_PRIN=[]

class Analizador:
    def __init__(self,contenido):
        self.report= reporte()
        self.cadena = ""
        self.linea = 0
        self.columna = 0  
        self.lista_cadena = []
        self.tmp_cadena = ""
        self.contenido= contenido
        self.txt= ""
        self.titulo=""
        self.tamaños=[]
        self.colores=[]

    def quitar(self, _cadena :str, _num : int):
        
        _tmp = ""
        count = 0
        for i in _cadena:
            if count >= _num:
                _tmp += i
            else:
                self.tmp_cadena += i 
            count += 1
        
        return _tmp

    def aumentarLinea(self):
        _tmp = self.lista_cadena[self.linea]
        
        if _tmp == self.tmp_cadena:
            self.linea += 1
            self.tmp_cadena = ""
            self.columna = 0 

    def esLaetiqueta(self, _cadena : str, _etiqueta : str):
        tmp = ""
        count = 0
        for i in _cadena:
            if count < len(_etiqueta):
                tmp += i
            count += 1

        if tmp == _etiqueta:
            return True
        else:
            return False

    def Numero(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_NUMERO.value,         # 10
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value     # >
        ]
        _numero = ""

        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                if i == L_tokens.TK_NUMERO.value:
                    
                    _numero = s.group()
                    self.lis.append(float(_numero))
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("GUARDANDO ERROR")
                e = err(i, self.linea, self.columna, "Error de código")
                listaErroresLexicos.append(e)
                self.reiniciar()
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}
                

        return {'resultado':_numero, "cadena":_cadena, "Error":False}

    def Operacion(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_OPERACION.value,  # Operacion
            L_tokens.TK_IGUAL.value,              # =
            "OPERADOR",                     # OPERADOR
            L_tokens.TK_MAYOR.value,        # >
            "NUMERO",                       # NUMERO
            "NUMERO",                       # NUMERO
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_OPERACION.value,  # Operacion
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""
        _operador = None
        for i in tokens:
            try:
                if "NUMERO" == i:
                    if self.esLaetiqueta(_cadena, "<Numero>"):
                        _result = self.Numero(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            e = err(i, self.linea, self.columna, "Error de código")
                            listaErroresLexicos.append(e)
                            self.reiniciar()
        
                            print("Ocurrio un error")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}

                    elif self.esLaetiqueta(_cadena, "<Operacion="):
                        _result = self.Operacion(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            e = err(i, self.linea, self.columna, "Error de código")
                            listaErroresLexicos.append(e)
                            self.reiniciar()
                            print("Ocurrio un error")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}
                    else:
                        # GUARDAR ERROR
                        e = err(i, self.linea, self.columna, "Error de código")
                        listaErroresLexicos.append(e)
                        self.reiniciar()                
                        print("Ocurrio un error")
                        return {'resultado':_numero, "cadena":_cadena, "Error": True}
                
                else:
                    if "OPERADOR" == i:
                        # SUMA
                        spatron = re.compile(f'^SUMA')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "SUMA"
                            self.lis.append("+")
                            _operador = L_tokens.TK_OP_SUMA

                        # RESTA
                        spatron = re.compile(f'^RESTA')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "RESTA"
                            self.lis.append("-")
                            _operador = L_tokens.TK_OP_RESTA
                        # MULTIPLICACION
                        spatron = re.compile(f'^MULTIPLICACION')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "MULTIPLICACION"
                            self.lis.append("*")
                            _operador = L_tokens.TK_OP_RESTA
                        # DIVISION
                        spatron = re.compile(f'^DIVISION')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "DIVISION"
                            self.lis.append("/")
                            _operador = L_tokens.TK_OP_RESTA
                        # POTENCIA
                        spatron = re.compile(f'^POTENCIA')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "POTENCIA"
                            self.lis.append("**")
                            _operador = L_tokens.TK_OP_RESTA
                        # RAIZ
                        spatron = re.compile(f'^RAIZ')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "RAIZ"
                            self.lis.append("sqrt")
                            _operador = L_tokens.TK_OP_RESTA
                        #INVERSO
                        spatron = re.compile(f'^INVERSO')
                        t = spatron.search(_cadena)   
                        if t != None:
                            i = "INVERSO"
                            self.lis.append("1/")
                            _operador = L_tokens.TK_OP_SENO
                            tokens.pop(6)

                        # MOD
                        spatron = re.compile(f'^MOD')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "MOD"
                            self.lis.append("%")
                            _operador = L_tokens.TK_OP_RESTA
                        spatron = re.compile(f'^SENO')
                        t = spatron.search(_cadena)   
                        if t != None:
                            i = "SENO"
                            self.lis.append("sen")
                            _operador = L_tokens.TK_OP_SENO
                            tokens.pop(6)
                        #COSENO
                        spatron = re.compile(f'^COSENO')
                        t = spatron.search(_cadena)   
                        if t != None:
                            i = "COSENO"
                            self.lis.append("cos")
                            _operador = L_tokens.TK_OP_SENO
                            tokens.pop(6)
                        #TANGENTE
                        spatron = re.compile(f'^TANGENTE')
                        t = spatron.search(_cadena)   
                        if t != None:
                            i = "TANGENTE"
                            self.lis.append("tan")
                            _operador = L_tokens.TK_OP_SENO
                            tokens.pop(6)
                        if _operador == None:
                            print(_operador)
                            # GUARDAR ERROR
                            e = err(i, self.linea, self.columna, "Error de código")
                            listaErroresLexicos.append(e)
                            self.reiniciar()
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}
    
            
                    patron = re.compile(f'^{i}')
                    s = patron.search(_cadena)
                    
                    # GUARDAR EL TOKEN
                    print("| ", self.linea, " | ", self.columna, " | ", s.group())
                    self.columna += int(s.end())
                    _cadena = self.quitar(_cadena, s.end())
                    #print(lista_operacion)
                    
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("Ocurrio un error")
                e = err(i, self.linea, self.columna, "Error de código")
                listaErroresLexicos.append(e)
                self.reiniciar()
                return {'resultado':_numero, "cadena":_cadena, "Error": True}
        
        # NUMERO1 OPERADOR NUMERO2
        return {'resultado':_numero, "cadena":_cadena, "Error":False}

    def Tipo(self, _cadena : str):
        
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_TIPO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
            "OPERACIONES",                  # OPERACIONES
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_TIPO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""
    
        for i in tokens:
            try: 
                if "OPERACIONES" == i:
                    salida = True
                    while salida:
                        print("--------------------------------")
                        self.lis = []
                        _result = self.Operacion(_cadena)
                        lista_total.append(self.lis)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            e = err(i, self.linea, self.columna, "Error de código")
                            listaErroresLexicos.append(e)
                            self.reiniciar()
                            print("Ocurrio un error")
                            salida=False
                        if self.esLaetiqueta(_cadena, "</Tipo>"):  
                            salida = False                
                else:
                    patron = re.compile(f'^{i}')
                    s = patron.search(_cadena)
                    # GUARDAR EL TOKEN
                    
                    print("| ", self.linea, " | ", self.columna, " | ", s.group())
                    self.columna += int(s.end())
                    _cadena = self.quitar(_cadena, s.end())
                    
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("Ocurrio un error xd")
                e = err(i, self.linea, self.columna, "Error de código")
                listaErroresLexicos.append(e)
                self.reiniciar()
                return {'resultado':_numero, "cadena":_cadena, "Error": True}
        self.Texto(_cadena)
        return {'resultado':_numero, "cadena":_cadena, "Error": False}



    def Texto(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_TEXTO.value,       # Texto
            L_tokens.TK_MAYOR.value,        # >
            L_tokens.TK_E_PARRAFO.value,                  # PARRAFO
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_TEXTO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""
        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                if i == L_tokens.TK_E_PARRAFO.value:
                    self.txt += s.group()
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                e = err(i, self.linea, self.columna, "Error de codigo")
                listaErroresLexicos.append(e)
                self.reiniciar()
                print("Ocurrio un error")
                
                return {'resultado':_numero, "cadena":_cadena, "Error": True}
        self.Funcion(_cadena)
        return {'resultado':_numero, "cadena":_cadena, "Error":False}

    def Funcion(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_Funcion.value,    # Funcion
            L_tokens.TK_IGUAL.value,        # =
            "ESCRIBIR",                     # ESCRIBIR 
            L_tokens.TK_MAYOR.value,        # >
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_Titulo.value,     # TITULO
            L_tokens.TK_MAYOR.value,        # >
            L_tokens.TK_E_PARRAFO.value,    # PARRAFO
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_Titulo.value,     # TITULO
            L_tokens.TK_MAYOR.value,        # >
            L_tokens.TK_MENOR.value,        # <
            "Descripcion",
            L_tokens.TK_MAYOR.value,        # > 
            "\[TEXTO\]","<","/","Descripcion",">","<","Contenido",">","\[TIPO\]","<","/","Contenido",#contenido inservible xd
             L_tokens.TK_MAYOR.value,        # >        
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_Funcion.value,    # Funcion
            L_tokens.TK_MAYOR.value,        # >
        ]
        txt=""
        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                if i == L_tokens.TK_E_PARRAFO.value:
                    txt += s.group()
                
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                e = err(i, self.linea, self.columna, "Error de codigo")
                listaErroresLexicos.append(e)
                self.reiniciar()
                print("Ocurrio un error")
                return { "cadena":_cadena, "Error": True}
        self.titulo=txt
        self.Estilo(_cadena)
        return { "cadena":_cadena, "Error":False}
    
    def Estilo(self,_cadena : str):
        tokens =[
            "<","Estilo",">",
            "<","Titulo","Color","=",L_tokens.TK_MAYUS.value,"tamanio","=",L_tokens.TK_NUMERO.value ,"/",">"
            ,"<","Descripcion","Color","=",L_tokens.TK_MAYUS.value,"tamanio","=",L_tokens.TK_NUMERO.value,"/",">",
            "<","Contenido","Color","=",L_tokens.TK_MAYUS.value,"tamanio","=",L_tokens.TK_NUMERO.value,"/",">"
            "<","/","Estilo",">"
        ]
         

        for i in tokens:
            colores=""
            tamaños=0
            listaaux=[]
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                if i == L_tokens.TK_MAYUS.value:
                    colores += s.group()
                if colores!="":
                    self.colores.append(colores)
                if i == L_tokens.TK_NUMERO.value:
                    tamaños = int(s.group())

                if tamaños>0:
                    self.tamaños.append(tamaños)
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                self.reiniciar()
                e = err(i, self.linea, self.columna, "Error de codigo")
                listaErroresLexicos.append(e)
                self.reiniciar()
                print("Ocurrio un error")
               
                return { "cadena":_cadena, "Error": True}
        print(self.tamaños)
        return { "cadena":_cadena, "Error":False}

    def compile(self):        
        # LIMPIAR MI ENTRADA
        nueva_cadena = ""
        lista_cadena = []
        for i in self.contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            i = i.replace('\t', '')
            i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)
        self.lista_cadena = lista_cadena
        self.Tipo(nueva_cadena)
        print(listaErroresLexicos)
        print(lista_total)
        if listaErroresLexicos:
            self.report.Errores(listaErroresLexicos)
        if len(self.tamaños)>0:
            calculo(lista_total,self.txt,self.titulo,self.colores,self.tamaños)
            self.reiniciar()
        else:
            messagebox.showerror(title="Atención",message="Se detectó un error, presione el botón errores para mostrar el error")

    def reiniciar (self):
        lista_total.clear()
        self.txt=""
        self.titulo=""
        self.colores.clear()
        self.tamaños.clear()
        
        

