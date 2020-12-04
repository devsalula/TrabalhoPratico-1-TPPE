import re
import numpy

class ParseData:

    def __init__(self, parser, pattern_to_match, pattern_to_sub):
        self.__parser = parser
        self.__pattern_to_match = pattern_to_match
        self.__pattern_to_sub = pattern_to_sub

    def compute(self):
        self.__content = re.sub(self.__pattern_to_match, self.__pattern_to_sub, self.__parser.content)
        self.__lines = self.__content.split(self.__pattern_to_sub)
        self.__lines = list(filter(lambda a: a != '', self.__lines))
        self.__line_content = []

        for index, line in enumerate(self.__lines, start=1):
            values = line.split('\n')
            values.insert(0, index)
            values = list(filter(lambda a: a != '', values))
            self.__line_content.append(values)

        if self.__parser.exit_format == 'c':
            self.__line_content = numpy.rot90(self.__line_content, 3)
            self.__line_content = numpy.fliplr(self.__line_content)
            self.__line_content = self.__line_content.tolist()

        self.__sequence_content = ''
        for content in self.__line_content:
            for num, item in enumerate(content, start=1):
                self.__sequence_content += str(item)
                if len(content) != num:
                    self.__sequence_content += self.__parser.delimiter

            self.__sequence_content += '\n'

        return self.__sequence_content