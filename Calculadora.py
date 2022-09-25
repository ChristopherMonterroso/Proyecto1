import math
from ReporteHTML import reporte
class calculo:
    def __init__(self,tupla,descripcion,titulo,colores,tamaños) -> None:
        self.colores = colores
        self.tamaños=tamaños
        self.report=reporte()
        self.titulo=titulo
        self.descripcion=descripcion
        self.tupla = tupla
        self.tipo= []
        self.operaciones = []
        self.totales= []
        self.ordenados = []
        self.signos = ["+","-","*","/","**","sqrt","sen","cos","tan","%","1/"]
        self.igual()
        self.total()
        self.generar()
        
    def igual (self):   
        for i in range (len(self.tupla)):
            llave=0
            key=0
            listaaux=[]
            text= ""
            text2="("
            if(len(self.tupla[i]))==2:
                text=str(self.tupla[i][0])+"("+str(self.tupla[i][1])+")"
                self.ordenados.append(text)
                if str(self.tupla[i][0])=="sen":
                    self.tipo.append("Seno")
                if str(self.tupla[i][0])=="cos":
                    self.tipo.append("Coseno")
                if str(self.tupla[i][0])=="tan":
                    self.tipo.append("Tangente")
                if str(self.tupla[i][0])=="1/":
                    self.tipo.append("Inverso")
                
            else: 
                for p in range(len(self.signos)): 
                    if self.tupla[i][1]==self.signos[p]:
                        self.tipo.append("Compleja")
                        self.ordenados.append("-------")
                        llave=1
                if llave==0:

                    listaaux.append(self.tupla[i][1])
                    text+=(str(self.tupla[i][1]))
                    var2=0
                    listaaux.append(self.tupla[i][0])
                    text+=(str(self.tupla[i][0]))
                    #condición para saber si es una operación compleja
                    if (len(self.tupla[i]))>3:
                        for j in range (2,len(self.tupla[i])):    
                            for k in range (len(self.signos)):              
                                if self.tupla[i][j]==self.signos[k]:
                                    for l in range (len(self.signos)):
                                        if self.tupla[i][j+2]==self.signos[l]:
                                            key =1
                                            var =j+2
                                        
                                            text2+=(str(self.tupla[i][j+1]))
                                            
                                            text2+=(str(self.tupla[i][j])+"(")
                                    if len(self.tupla[i])<6:
                                        
                                        var2=j               
                            if key==1:
                                if j==var:
                                    
                                    text2+=(str(self.tupla[i][j+1]))
                                    text2+=(str(self.tupla[i][j]))
                                    text2+=(str(self.tupla[i][j+2]))
                            if j==var2:
                                text2+=(str(self.tupla[i][j+1]))
                                text2+=(str(self.tupla[i][j]))
                                text2+=(str(self.tupla[i][j+2]))
                                text2+=")" 
                                text+=text2
                                self.ordenados.append(text)
                            if len(self.tupla[i])>5:
                                if j==len(self.tupla[i])-1:
                                    text2+=")" 
                                    text+=text2
                                    self.ordenados.append(text)
                                    self.tipo.append("Compleja")
                    else:
                        text+=(str(self.tupla[i][2])) 
                        self.ordenados.append(text)
                        if str(self.tupla[i][0])=="+":
                            self.tipo.append("Suma")
                        if str(self.tupla[i][0])=="-":
                            self.tipo.append("Resta")
                        if str(self.tupla[i][0])=="*":
                            self.tipo.append("Multiplicación")
                        if str(self.tupla[i][0])=="/":
                            self.tipo.append("División")
                        if str(self.tupla[i][0])=="**":
                            self.tipo.append("Potencia")
                        if str(self.tupla[i][0])=="sqrt":
                            self.tipo.append("Raíz")
                        if str(self.tupla[i][0])=="%":
                            self.tipo.append("Residuo")
        #print("\n",self.ordenados,"\n")
        #print(self.operaciones)

    def total(self):
        for i in range(len(self.tupla)):
            llave= 0
            total = 0
            operando=0
            #saber el tamaño de la operación
            for s in range (len(self.signos)):
                if self.tupla[i][1]==self.signos[s]:
                    llave=1
                    if len(self.tupla[i])==7:
                    
                        total=self.calcular(self.tupla[i][4],self.tupla[i][5],self.tupla[i][6])
                        operando=self.calcular(self.tupla[i][1],self.tupla[i][2],self.tupla[i][3])
                        total=self.calcular(self.tupla[i][0],operando,total)
                        self.totales.append(total)
                    if len(self.tupla[i])==9:
                        total=self.calcular(self.tupla[i][7],self.tupla[i][8],None)
                        operando=self.calcular(self.tupla[i][5],self.tupla[i][6],None)
                        total=self.calcular(self.tupla[i][4],operando,total)
                        total=self.calcular(self.tupla[i][3],total,None)
                        operando=self.calcular(self.tupla[i][1],self.tupla[i][2],None)
                        total=self.calcular(self.tupla[i][0],operando,total)
                        self.totales.append(total)

                elif s==(len(self.signos))-1 and llave ==0:
                    if len(self.tupla[i])==2:
                        total=self.calcular(self.tupla[i][0],self.tupla[i][1],None)
                        self.totales.append(total)
                    elif len(self.tupla[i])>3 and len(self.tupla[i])<6:
                        total=self.calcular(self.tupla[i][2],self.tupla[i][3],self.tupla[i][4])
                        total=self.calcular(self.tupla[i][0],self.tupla[i][1],total)
                        self.totales.append(total)
                    elif len(self.tupla[i])>5 and len(self.tupla[i])<8:
                        total=self.calcular(self.tupla[i][4],self.tupla[i][5],self.tupla[i][6])
                        total=self.calcular(self.tupla[i][2],self.tupla[i][3],total)
                        total=self.calcular(self.tupla[i][0],self.tupla[i][1],total)
                        self.totales.append(total)
                        
                    else:
                        total=self.calcular(self.tupla[i][0],self.tupla[i][1],self.tupla[i][2])
                        self.totales.append(total)
        print(self.totales)
        #for i in range (len(self.totales)):

            #print("Operación: ",self.ordenados[i]," Resultado:",self.totales[i])
           
    #Método para saber que signo es  y operar      
    def calcular(self, signo, numero1, numero2):
        if signo =="+":    
            calcular=float(numero1) + float(numero2)
            return calcular
        elif signo =="-":
            calcular=float(numero1) - float(numero2)
            return calcular
        elif signo =="/":
            calcular=float(numero1) / float(numero2)
            return calcular
        elif signo =="*":
            calcular=float(numero1) * float(numero2)
            return calcular
        elif signo =="**":
            calcular=float(numero2) ** float(numero1) #potencia
            return calcular
        elif signo =="sqrt":
            calcular = float(numero2)**(1/float(numero1))
            return calcular
        elif signo=="1/":
            calcular= 1/(numero1)
            return calcular
        elif signo =="%":
            calcular = float(numero1)%float(numero2)
            return calcular
        elif signo=="sen":
            calcular= math.sin(numero1)
            return calcular
        elif signo=="cos":
            calcular= math.cos(numero1)
            return calcular
        elif signo=="tan":
            calcular= math.sin(numero1)
            return calcular
            
    def generar(self):
        self.report.resultados(self.tipo,self.ordenados,self.totales,self.descripcion,self.titulo,self.colores,self.tamaños)
        

    
        

                
                


                                      
            
                                     
