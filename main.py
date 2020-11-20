from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException

def read_file(file_name):
    try:
        file = open(file_name)
    except:
        raise ArquivoNaoEncontradoException(file_name)
    return file.read()

def delimiter_input():
    pass

def main():
    print("Hello World")
