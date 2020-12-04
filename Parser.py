import re
import numpy
import os

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException
from exceptions.EscritaFalhaException import EscritaFalhaException

from parse_data import ParseData
class Parser:

    def read_file(self, filename):
        try:
            file = open(filename)
            self.content = file.read()
            self.filename = self.extract_filename(filename, -1, '/')
        except:
            raise ArquivoNaoEncontradoException(filename)

    def extract_filename(self, filename, position, character_split):
        filename_array = filename.split(character_split)
        filename = filename_array[position]
        return filename

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
        parser_service = ParseData(self, r"-+ Evolution \d+ -+", "---")
        self.parsed_data = parser_service.compute()

    def write_response(self):
        try:
            filename = self.extract_filename(self.filename, 0, '.')
            file = open(self.path + filename + 'Tab.out', "w")
            file.write(self.parsed_data)
            file.close()
            return 'Escrita bem sucedida'
        except Exception as err:
            print(err)
            raise EscritaFalhaException()

