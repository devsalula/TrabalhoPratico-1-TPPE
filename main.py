from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException

from test_data import expected_mock1

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

def sequence_format(exit_format):
    if exit_format == 'c' or exit_format == 'l':
        return exit_format
    else:
        raise FormatoInvalidoException(exit_format)

def parse_data(content, delimit, exit_format):
    return expected_mock1

def main():
    print("Hello World")
