from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException

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

def response_file(filename):
    try:
        file = open(filename, "w")
        return file
    except:
        raise EscritaNaoPermitidaException(filename)


def main():
    print("Hello World")
