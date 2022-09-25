class reporte:
    def __init__(self) -> None:
        
        pass
    def resultados(self,tipo,operacion,resultado,descripcion:str,titulo:str,colores,tamaños):
        coloresIngles=[]
        for i in range (len(colores)):

            if colores[i]=="AZUL":
                color="blue" 
                coloresIngles.append(color)
            if colores[i]=="VERDE":
                color="green"
                coloresIngles.append(color)
            if colores[i]=="NEGRO":
                color="black"
                coloresIngles.append(color)
            if colores[i]=="ROJO":
                color="red"
                coloresIngles.append(color)
            if colores[i]=="AMARILLO":
                color="yellow"
                coloresIngles.append(color)
            if colores[i]=="NARANJA":
                color="orange"
                coloresIngles.append(color)
            if colores[i]=="MORADO":
                color="purple"
                coloresIngles.append(color)


        txt="""
        <html>
            <title>
            Resultados
            </title>
            <head>
            <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
            </head>
            <body style="background-color: #E2E5B8;">

            <font face="nunito,arial,verdana">

            <center>
            <FONT SIZE="""+str(tamaños[0])+""" COLOR="""+coloresIngles[0]+""" FACE="impact" style="text-align: center;">"""+ titulo+"""</FONT>
            </center>
            <center>
            <FONT SIZE="""+str(tamaños[1])+""" COLOR="""+coloresIngles[1]+""" FACE="roman" style="text-align: center;">"""+ descripcion+"""</FONT>
            </center>
            <br><br/>
            <table style="height: 54px; width: 90%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="3">
            <tbody>
            <tr style="height: 36px;background-color: #F67C62;">
            <td style="width: 25%; height: 36px; text-align: center;">No.</td>
            <td style="width: 25%; height: 36px; text-align: center;">Tipo</td>
            <td style="width: 25%; height: 36px; text-align: center;">Operación</td>
            <td style="width: 25%; height: 36px; text-align: center;">Resultado</td>
            </tr>
            """
        for i in range(len(tipo)):
            txt+="""
                <tr style="height: 18px;background-color: #FFFFFF">
                <td style="width: 25%; height: 18px; text-align: center;">"""+str(i+1)+"""</td>
                <td style="width: 25%; height: 18px; text-align: center;">"""+str(tipo[i])+"""</td>
                <td style="width: 25%; height: 18px; text-align: center;">"""+str(operacion[i])+"""</td>
                <td style="width: 25%; height: 18px; text-align: center;">"""+str(resultado[i])+"""</td>
                </tr>
                """
        txt+="""
            </tbody>
            </table>
            </font>
            </body>
        </html>
        """
        Reporte=open("./Records/RESULTADOS_201902363.html","w+")
        Reporte.write(txt)
        Reporte.close

    def Errores(self, lista):
        cont=1
        txt="""
        <html>
            <title>
            Reporte de Errores
            </title>
            <head>
            <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
            </head>
            <body style="background-color: #E7FAF8;">

            <font face="nunito,arial,verdana">

            <table style="border: hidden; width: 100%; height: 90px; margin-left: auto; margin-right: auto;">
            <tbody style="border: hidden;">
            <tr style="border: hidden; height: 104px;">
            <td style="height: 90px; width: 92%;">
            </td>
            </tr>
            </tbody>
            </table>
            <h1  style="text-align: center;">REPORTE DE ERRORES</h1>
            <table style="height: 54px; width: 90%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="3">
            <tbody>
            <tr style="height: 36px;background-color: #F67C62">
            <td style="width: 20%; height: 36px; text-align: center;">No.</td>
            <td style="width: 20%; height: 36px; text-align: center;">Lexema</td>
            <td style="width: 20%; height: 36px; text-align: center;">Fila</td>
            <td style="width: 20%; height: 36px; text-align: center;">Columna</td>
            <td style="width: 20%; height: 36px; text-align: center;">Tipo</td>
            
            </tr>
            """
        for i in lista:
            i = i.getErrores()
            txt+="""
                <tr style="height: 18px;background-color: #FFFFFF">
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(cont)+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(i['token'])+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(i['fila'])+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(i['columna'])+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(i['descripcion'])+"""</td>
                </tr>
                """
            cont+=1
        txt+="""
            </tbody>
            </table>
            </font>
            </body>
        </html>
        """
        Reporte=open("./Records/ERRORES_201902363.html","w+",encoding="utf-8")
        Reporte.write(txt)
        Reporte.close