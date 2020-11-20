class EscritaNaoPermitidaException(Exception):

    def __init__(self, filename):
        self.filename = filename
        
    def __str__(self):
        return 'Arquivo %s não pode ser criado' % self.filename
