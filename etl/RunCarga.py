# Internal libs
from etl.Etl import Data

if __name__ == '__main__':
    data = Data('digicade')
    data.carga_stg_ocorrencias()
    data.carga_cliente()
    data.carga_ocorrencia()
