import pytest
from main import read_file
from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException

@pytest.mark.parametrize("test_input,expected", [('./assets/test.out', 'Hello World'), ('./assets/test1.out', 'Ola Mundo'), ('./assets/test2.out', 'Hola Mundo')])
def test_read_file(test_input, expected):
    file = read_file(test_input)
    assert file == expected

def test_file_not_found():
    with pytest.raises(ArquivoNaoEncontradoException):
        assert read_file("./assets/n_existe.out")