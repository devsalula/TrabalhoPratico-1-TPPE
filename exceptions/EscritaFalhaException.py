class EscritaFalhaException(Exception):
        
    def __str__(self):
        return 'A escrita no arquivo falhou'