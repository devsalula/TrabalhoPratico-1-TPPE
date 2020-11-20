import pytest
from main import read_file

def test_read_file():
    file_name = "./assets/test.out"
    file = read_file(file_name)
    assert file == 'Hello World'
