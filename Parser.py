import re
import numpy
import os

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException
from exceptions.EscritaFalhaException import EscritaFalhaException


class Parser:

    def read_file(self, filename):
        try:
            file = open(filename)
            self.content = file.read()
            self.extract_filename(filename)
        except:
            raise ArquivoNaoEncontradoException(filename)

    def extract_filename(self, filename):
        filename_array = filename.split('/')
        filename = filename_array[-1]
        self.filename = filename

    def delimiter_input(self, delimiter):
        if len(delimiter) == 1:
            self.delimiter = delimiter
        else:
            raise DelimitadorInvalidoException(delimiter)

    def define_path(self, path):
        if path[-1] != '/':
            path += '/'
        has_access = os.access(path, os.W_OK)
        if has_access:
            self.path = path
        else:
            raise EscritaNaoPermitidaException(path)
    
    def sequence_format(self, exit_format):
        if exit_format == 'c' or exit_format == 'l':
            self.exit_format = exit_format
        else:
            raise FormatoInvalidoException(exit_format)

    def parse_data(self):
        content = re.sub(r"-+ Evolution \d+ -+", "---", self.content)
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
        if self.exit_format == 'c':
            line_content = numpy.rot90(line_content, 3)
            line_content = numpy.fliplr(line_content)
            line_content = line_content.tolist()

        for content in line_content:
            for num, item in enumerate(content, start=1):
                sequence_content += str(item)
                if len(content) != num:
                    sequence_content += self.delimiter
            
            sequence_content += '\n'
        
        self.parsed_data = sequence_content

    def write_response(self):
        try:
            filename_array = self.filename.split('.')
            filename = filename_array[0]
            file = open(self.path + filename + 'Tab.out', "w")
            file.write(self.parsed_data)
            file.close()
            return 'Escrita bem sucedida'
        except Exception as err:
            print(err)
            raise EscritaFalhaException()
