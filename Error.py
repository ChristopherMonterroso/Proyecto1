class error :
    def __init__(self, token , fila , columna, descripcion="") -> None:
        self.token= token
        self.fila=fila
        self.columna=columna
        self.descripcion=descripcion
    def getErrores(self):
        return {'token':self.token, 'fila':self.fila, 'columna':self.columna, 'descripcion':self.descripcion}