class EscritaNaoPermitidaException(Exception):

    def __init__(self, path):
        self.path = path
        
    def __str__(self):
        return 'Arquivo não pode ser escrito no caminho %s' % self.path
