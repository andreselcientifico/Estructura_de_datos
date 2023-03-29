class suma:
    initial_missing = object()
    def __init__(self,funcion, lista, inicial=initial_missing):
        self.funcion = funcion
        self.lista = lista
        self.initial_missing = inicial
        
    
    def suma (self):
        it = iter(self.lista)

        if self.initial_missing is self.initial_missing :
            try:
                value = next(it)
            except StopIteration:
                raise TypeError("suma() of empty sequence with no initial value") from None
        else:
            value = self.initial_missing

        for element in it:
            value = self.funcion(value, element)

        return value