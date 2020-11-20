import pytest
import io

from main import read_file, delimiter_input, response_file, sequence_format, parse_data, write_response
from test_data import content_mock1, expected_mock1, content_mock2, expected_mock2

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from exceptions.FormatoInvalidoException import FormatoInvalidoException


@pytest.mark.parametrize("test_input,expected", [('./assets/test.out', 'Hello World'), ('./assets/test1.out', 'Ola Mundo'), ('./assets/test2.out', 'Hola Mundo')])
def test_read_file(test_input, expected):
    file = read_file(test_input)
    assert file == expected

@pytest.mark.parametrize("test_input", [('./error/test.out'), ('./error/failed.out'), ('./error/failed/test2.out')])
def test_file_not_found(test_input):
    with pytest.raises(ArquivoNaoEncontradoException):
        assert read_file(test_input)

@pytest.mark.parametrize("test_input,expected", [(';', ';'), (':', ':'), ('\n', '\n')])
def test_delimiter_input(test_input, expected):
    assert delimiter_input(test_input) == expected

@pytest.mark.parametrize("test_input", [('delimitador invalido'), ('invalid delimit'), ('delimitador no válido')])
def test_invalid_delimit(test_input):
    with pytest.raises(DelimitadorInvalidoException):
        assert delimiter_input(test_input)

@pytest.mark.parametrize("test_input", [('assets/teste.out'), ('assets/valido.out')])
def test_response_file(test_input):
    assert type(response_file(test_input)) == io.TextIOWrapper

@pytest.mark.parametrize("test_input", [('./error/failed.txt'), ('./error/failed.txt')])
def test_invalid_response_file(test_input):
    with pytest.raises(EscritaNaoPermitidaException):
        assert response_file(test_input)

@pytest.mark.parametrize("test_input,expected", [('l', 'l'), ('c', 'c')])
def test_sequence_format(test_input, expected):
    assert sequence_format(test_input) == expected
    
@pytest.mark.parametrize("test_input", [('j'), ('linha'), ('quero coluna')])
def test_invalid_sequence_format(test_input):
    with pytest.raises(FormatoInvalidoException):
        assert sequence_format(test_input)

@pytest.mark.parametrize("content, delimit, exit_format, expected", [(content_mock1, ';', 'l', expected_mock1), (content_mock2, ';', 'c', expected_mock2)])
def test_parse_data(content, delimit, exit_format, expected):
    assert parse_data(content, delimit, exit_format) == expected

def test_write_response():
    file = open('./assets/teste.out', 'w')
    content = expected_mock1
    assert write_response(file, content) == 'Escrita bem sucedida'