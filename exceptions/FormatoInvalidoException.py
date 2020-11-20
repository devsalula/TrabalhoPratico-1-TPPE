class FormatoInvalidoException(Exception):

    def __init__(self, exit_format):
        self.exit_format = exit_format
        
    def __str__(self):
        return '%s não é um formato válido' % self.exit_format
