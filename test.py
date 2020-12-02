import pytest
import io

from Parser import Parser
from test_data import expected_mock1, expected_mock2

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException
from exceptions.EscritaFalhaException import EscritaFalhaException


@pytest.mark.parametrize("test_input,expected", [('./assets/test.out', 'Hello World'), ('./assets/test1.out', 'Ola Mundo'), ('./assets/test2.out', 'Hola Mundo')])
def test_read_file(test_input, expected):
    parser = Parser()
    parser.read_file(test_input)
    assert parser.content == expected

@pytest.mark.parametrize("test_input", [('./error/test.out'), ('./error/failed.out'), ('./error/failed/test2.out')])
def test_file_not_found(test_input):
    with pytest.raises(ArquivoNaoEncontradoException):
        parser = Parser()
        assert parser.read_file(test_input)

@pytest.mark.parametrize("test_input,expected", [(';', ';'), (':', ':'), ('\n', '\n')])
def test_delimiter_input(test_input, expected):
    parser = Parser()
    parser.delimiter_input(test_input)
    assert parser.delimiter == expected

@pytest.mark.parametrize("test_input", [('delimitador invalido'), ('invalid delimit'), ('delimitador no válido')])
def test_invalid_delimit(test_input):
    with pytest.raises(DelimitadorInvalidoException):
        parser = Parser()
        assert parser.delimiter_input(test_input)

@pytest.mark.parametrize("path, expected", [('assets', 'assets/'), ('./', './')])
def test_define_path(path, expected):
    parser = Parser()
    parser.define_path(path)
    assert parser.path == expected

@pytest.mark.parametrize("test_input", [('error'), ('../test')])
def test_invalid_path(test_input):
    with pytest.raises(EscritaNaoPermitidaException):
        parser = Parser()
        assert parser.define_path(test_input)

@pytest.mark.parametrize("test_input,expected", [('l', 'l'), ('c', 'c')])
def test_sequence_format(test_input, expected):
    parser = Parser()
    parser.sequence_format(test_input)
    assert parser.exit_format == expected
    
@pytest.mark.parametrize("test_input", [('j'), ('linha'), ('quero coluna')])
def test_invalid_sequence_format(test_input):
    with pytest.raises(FormatoInvalidoException):
        parser = Parser()
        assert parser.sequence_format(test_input)

@pytest.mark.parametrize("filename, delimit, exit_format, expected", [('./assets/contentMock1.out', ';', 'l', expected_mock1), ('./assets/contentMock2.out', ';', 'c', expected_mock2)])
def test_parse_data(filename, delimit, exit_format, expected):
    parser = Parser()
    parser.read_file(filename)
    parser.delimiter_input(delimit)
    parser.sequence_format(exit_format)
    parser.parse_data()
    assert parser.parsed_data == expected

@pytest.mark.parametrize("filename, delimit, exit_format, path", [('./assets/contentMock1.out', ';', 'l', 'assets'), ('./assets/contentMock2.out', ';', 'c', 'assets')])
def test_write_response(filename, delimit, exit_format, path):
    parser = Parser()
    parser.read_file(filename)
    parser.delimiter_input(delimit)
    parser.sequence_format(exit_format)
    parser.define_path(path)
    parser.parse_data()
    assert parser.write_response() == 'Escrita bem sucedida'

def test_write_response_failed():
    with pytest.raises(EscritaFalhaException):
        parser = Parser()
        assert parser.write_response()