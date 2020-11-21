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

def response_file(filename, filename_exit):
    try:
        filename_array = filename.split('.')
        filename = filename_array[0]
        if filename_exit[-1] != '/':
            filename_exit += '/'
        file = open(filename_exit + filename + 'Tab.out', "w")
        return file
    except:
        raise EscritaNaoPermitidaException(filename)

def sequence_format(exit_format):
    if exit_format == 'c' or exit_format == 'l':
        return exit_format
    else:
        raise FormatoInvalidoException(exit_format)

def parse_data(content, delimit, exit_format):
    content = re.sub(r"-+ Evolution \d+ -+", "---", content)
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
    filename = input("Insira o caminho do seu arquivo: ") 
    content = read_file(filename)
    delimit = input("Insira o delimitador desejado: ")
    delimit_valid = delimiter_input(delimit)
    filename_exit = input("Insira o caminho do arquivo de saída: ")
    filename_array = filename.split('/')
    filename = filename_array[-1]
    file = response_file(filename, filename_exit)
    exit_format = input("Insira o tipo de saída - c para Coluna, l - para linha: ")
    exit_format_valid = sequence_format(exit_format)
    content_parsed = parse_data(content, delimit_valid, exit_format_valid)
    write_response(file, content_parsed)
    print("Fim do Programa!")

if __name__ == "__main__":
    main()
