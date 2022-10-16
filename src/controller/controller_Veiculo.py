from model.Veiculo import Veiculo
from conexion.oracle_queries import OracleQueries

class Controller_Veiculo:
    def __init__(self):
        pass
        
    def inserir_veiculo(self) -> Veiculo:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        #Solicita ao usuario a nova descrição do produto
        descricao_novo_veiculo = input("Descrição (Novo): ")

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = (CodCarro ,modelo) = descricao_novo_veiculo
        # Executa o bloco PL/SQL anônimo para inserção do novo produto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :CodCarro := VEICULO_CODCARRO_VEICULO_SEQ.NEXTVAL;
            insert into Veiculo values(:CodCarro, :modelo);
        end;
        """, data)
        # Recupera o código do novo produto
        CodCarro = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_veiculo = oracle.sqlToDataFrame(f"select CodCarro, modelo from Veiculo where idVenda = {CodCarro}")
        # Cria um novo objeto Produto
        CodCarro = Veiculo(df_veiculo.CodCarro.values[0], df_veiculo.modelo.values[0])
        # Exibe os atributos do novo produto
        print(CodCarro.to_string())
        # Retorna o objeto novo_produto para utilização posterior, caso necessário
        return CodCarro

    def atualizar_Veiculo(self) -> Veiculo:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        CodCarro = int(input("Código do Veiculo que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_Veiculo(oracle, CodCarro):
            # Solicita a nova descrição do produto
            novo_modelo_veiculo = input("Descrição (Novo):")
            # Atualiza a descrição do produto existente
            oracle.write(f"update Veiculos set modelo = nova_descricao_veiculo where CodCarro = {CodCarro}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_veiculo = oracle.sqlToDataFrame(f"select CodCarro, modelo from Veiculo where CodCarro = {CodCarro}")
            # Cria um novo objeto Produto
            veiculo_atualizado = Veiculo(df_veiculo.CodCarro.values[0], CodCarro.modelo.values[0])
            # Exibe os atributos do novo produto
            print(veiculo_atualizado.to_string())
            # Retorna o objeto produto_atualizado para utilização posterior, caso necessário
            return veiculo_atualizado
        else:
            print(f"O código {CodCarro} não existe.")
            return None

    def excluir_veiculo(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        CodCarro = int(input("Código do Veiculo que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_veiculo(oracle, CodCarro):           
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_veiculo = oracle.sqlToDataFrame(f"select CodCarro, modelo from Veiculo where CodCarro = {CodCarro}")
            # Revome o produto da tabela
            oracle.write(f"delete from Veiculo where CodCarro = {CodCarro}")            
            # Cria um novo objeto Produto para informar que foi removido
            veiculo_excluido = Veiculo(df_veiculo.CodCarro.values[0], df_veiculo.modelo.values[0])
            # Exibe os atributos do produto excluído
            print("Veiculo Removido com Sucesso!")
            print(veiculo_excluido.to_string())
        else:
            print(f"O código {CodCarro} não existe.")

    def verifica_existencia_veiculo(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo}")
        return df_veiculo.empty