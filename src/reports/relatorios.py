from pandas import DataFrame
from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_veiculos.sql") as f:
            self.query_relatorio_veiculo = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_vendaVeiculo.sql") as f:
            self.query_relatorio_vendaVeiculo = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_cliente.sql") as f:
            self.query_relatorio_cliente = f.read()

    def get_relatorio_vendaVeiculo(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_vendaVeiculo))
        input("Pressione Enter para Sair do Relatório de venda de veiculo")

  

    def get_relatorio_veiculo(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_veiculo))
        input("Pressione Enter para Sair do Relatório de Veiculos")

    def get_relatorio_cliente(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_cliente))
        input("Pressione Enter para Sair do Relatório de Cliente")