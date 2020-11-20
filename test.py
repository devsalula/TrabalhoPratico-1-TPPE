import pytest
import io

from main import read_file, delimiter_input, response_file, sequence_format

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

def test_sequence_format():
    exit_format = 'l'
    assert sequence_format(exit_format) == exit_format

def test_invalid_sequence_format():
    with pytest.raises(FormatoInvalidoException):
        assert sequence_format('d')