class DelimitadorInvalidoException(Exception):

    def __init__(self, delimitator):
        self.delimitator = delimitator
        
    def __str__(self):
        return 'Delimitador %s inválido' % self.delimitator