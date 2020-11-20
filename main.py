from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException

def read_file(file_name):
    try:
        file = open(file_name)
    except:
        raise ArquivoNaoEncontradoException(file_name)
    return file.read()

def delimiter_input(symbol):
    if len(symbol) == 1:
        return symbol
    else:
        raise DelimitadorInvalidoException(symbol)

def main():
    print("Hello World")
