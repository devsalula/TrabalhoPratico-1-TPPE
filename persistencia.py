import os

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException

class Persistencia:

    def get_content(self):
        return self.__content

    def __extract_filename(self, filename, position, character_split):
        filename_array = filename.split(character_split)
        filename = filename_array[position]
        return filename

    def read_file(self, filename):
        try:
            file = open(filename)
            self.__content = file.read()
            self.__filename = self.__extract_filename(filename, -1, '/')
        except:
            raise ArquivoNaoEncontradoException(filename)

    def write_response(self, path, content):
        filename = self.__extract_filename(self.__filename, 0, '.')
        file = open(path + filename + 'Tab.out', "w")
        file.write(content)
        file.close()
        return 'Escrita bem sucedida'