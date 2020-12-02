from Parser import Parser

def main():
    parser = Parser()
    filename = input("Insira o caminho do seu arquivo: ") 
    parser.read_file(filename)
    delimit = input("Insira o delimitador desejado: ")
    parser.delimiter_input(delimit)
    exit_format = input("Insira o tipo de saída - c para Coluna, l - para linha: ")
    parser.sequence_format(exit_format)
    path = input("Insira o caminho do arquivo de saída: ")
    parser.define_path(path)
    parser.parse_data()
    parser.write_response()
    print("Fim do Programa!")

if __name__ == "__main__":
    main()