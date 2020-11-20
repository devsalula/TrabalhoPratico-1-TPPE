import pytest
from main import read_file
from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException

def test_read_file():
    file_name = "./assets/test.out"
    file = read_file(file_name)
    assert file == 'Hello World'

def test_file_not_found():
    with pytest.raises(ArquivoNaoEncontradoException):
        assert read_file("./assets/n_existe.out")