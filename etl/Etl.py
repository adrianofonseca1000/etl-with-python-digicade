# Importing the libraries
import pandas as pd
import petl as etl
# Internal libs
from etl.Config import Base


class Data(Base):

    def __init__(self, database):
        super().__init__(database)

    def carga_stg_ocorrencias(self):
        print("Read csv ocorrencias")

        ocorrencias = pd.read_csv('../data/clientes/ocorrencias.csv', encoding="latin-1", sep=",")

        print("Load for table stg_ocorrencias...")
        print('This one dataset it has %s rows e %s columns' % (ocorrencias.shape[0], ocorrencias.shape[1]))

        tb_stg_ocorrencias = etl.fromdataframe(ocorrencias)
        self.cursor().execute('SET SQL_MODE=ANSI_QUOTES')
        self.cursor().execute('TRUNCATE TABLE digicade.stg_ocorrencias')
        ocorrencias = etl.todb(tb_stg_ocorrencias, self.cursor(), 'stg_ocorrencias', schema='digicade', commit=True,
                               sample=1000)
        return ocorrencias

    def carga_cliente(self):
        query_cliente = '''SELECT CPF_CLIENTE FROM digicade.stg_ocorrencias'''
        cliente = pd.read_sql_query(query_cliente, self.DB_ACCESS)

        print("Load for table cliente...")
        print('This one dataset it has %s rows e %s columns' % (cliente.shape[0], cliente.shape[1]))

        self.cursor().execute('SET SQL_MODE=ANSI_QUOTES')
        self.cursor().execute('TRUNCATE TABLE digicade.cliente')
        tb_cliente = etl.fromdataframe(cliente)
        cliente = etl.todb(tb_cliente, self.cursor(), 'cliente', schema='digicade', commit=True,
                           sample=1000)
        return cliente

    def carga_ocorrencia(self):
        query_ocorrencia = '''SELECT DATA_HORA AS DT_OCORRENCIA,DESCRICAO AS DSC_OCORRENCIA, LONGITUDE, LATITUDE FROM digicade.stg_ocorrencias'''
        query_id_cliente = '''SELECT ID_CLIENTE FROM digicade.cliente'''
        ocorrencia = pd.read_sql_query(query_ocorrencia, self.DB_ACCESS)
        id_cliente = pd.read_sql_query(query_id_cliente, self.DB_ACCESS)

        print("Load for table ocorrencia")
        ocorrencia = pd.concat([id_cliente, ocorrencia], axis=1, join='inner')
        print('This one dataset it has %s rows e %s columns' % (ocorrencia.shape[0], ocorrencia.shape[1]))

        self.cursor().execute('SET SQL_MODE=ANSI_QUOTES')
        self.cursor().execute('TRUNCATE TABLE digicade.ocorrencia')
        tb_ocorrencia = etl.fromdataframe(ocorrencia)
        ocorrencia = etl.todb(tb_ocorrencia, self.cursor(), 'ocorrencia', schema='digicade', commit=True,
                              sample=1000)
        return ocorrencia
