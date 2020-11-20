import pytest
import io

from main import read_file, delimiter_input, response_file

from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException

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

def test_response_file():
    filename = 'assets/response.out'
    assert type(response_file(filename)) == io.TextIOWrapper