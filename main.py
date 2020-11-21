import re
import numpy

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException
from exceptions.EscritaFalhaException import EscritaFalhaException

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
    content = re.sub(r"\n---------- Evolution \d+ ----------", "---", content)
    lines = content.split('---')
    lines = list(filter(lambda a: a != '', lines))
    line_content = []
    index = 0
    for index, line in enumerate(lines, start=1):
        values = line.split('\n')
        values.insert(0, index)
        values = list(filter(lambda a: a != '', values))
        line_content.append(values)

    sequence_content = ''
    if exit_format == 'c':
        line_content = numpy.rot90(line_content, 3)
        line_content = numpy.fliplr(line_content)
        line_content = line_content.tolist()
    
    for content in line_content:
        for num, item in enumerate(content, start=1):
            sequence_content += str(item)
            if len(content) != num:
                sequence_content += delimit
        
        sequence_content += '\n'
    
    return sequence_content

def write_response(file, content):
    try:
        file.write(content)
        file.close()
        return 'Escrita bem sucedida'
    except:
        raise EscritaFalhaException()

def main():
    print("Hello World")
