import re
import numpy
import os

from exceptions.EscritaFalhaException import EscritaFalhaException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException
from parse_data import ParseData
from persistencia import Persistencia

class Parser:

    def __init__(self):
        self.persistencia = Persistencia()

    def read_file(self, filename):
        self.persistencia.read_file(filename)
        self.set_content(self.persistencia.get_content())

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

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def parse_data(self):
        parser_service = ParseData(self, self.get_content(), r"-+ Evolution \d+ -+", "---")
        self.parsed_data = parser_service.compute()

    def write_response(self):
        try:
            return self.persistencia.write_response(self.path, self.parsed_data)
        except:
            raise EscritaFalhaException()