# Digicadê ETL utilizando Python
 
 - Instruções para a execução do teste:

- Não se preocupe com erros de sintaxe, você será avaliado pela estrutura e lógica do código, não por uma vírgula errada;
- Se tiver alguma dúvida, faça a questão com o melhor entendimento que você teve, descrevendo a dúvida e qual foi sua decisão;
- Leia todas as questões antes de começar, pois elas estão interligadas.

1 – Escreva um script em Python para ler um arquivo CSV e carregar em uma tabela em uma instância de banco de dados. O banco de dados poderá ser uma instância Oracle, ou outro qualquer que se sinta mais confortável.

- Caminho do arquivo: /data/clientes/ocorrencias.csv
- Estrutura de campos do arquivo:
   - CPF_CLIENTE: CPF do cliente;
   - DATA_HORA: data da ocorrência no formato “YYYY-MM-DD HH:MI:SS”;
   - DESCRICAO: texto com a descrição detalhada da ocorrência;
   - LONGITUDE: longitude em graus decimais da localização da ocorrência;
   - LATITUDE: latitude em graus decimais da localização da ocorrência.
- A string de conexão ao banco será passada através da variável de ambiente “DB_ACCESS”
- Estrutura da tabela a ser carregada:
   - Tabela: STG_OCORRENCIAS
   - Colunas: 
      - CPF_CLIENTE: texto com no máximo 11 caracteres;
      - DATA_HORA: data e hora;
      - DESCRICAO: texto com no máximo 4000 caracteres;
      - LONGITUDE: valor numérico;
      - LATITUDE: valor numérico.

Exemplo das 10 primeiras linhas do arquivo:
“CPF_CLIENTE”,”DATA_HORA”,”DESCRICAO”,”LONGITUDE”,”LATITUDE”
“23847628937”,”2000-03-28 16:31:12”,”Lorem ipsum dolor sit amet”,-43.9128347621,-19.441287346
“70923487023”,”2000-01-27 12:59:01”,”Aenean convallis sapien”,-43.8421376482,-19.34123412
“70923487023”,”2000-01-30 10:24:09”,”Nullam cursus laoreet mollis”,-43.823456234,-19.2432846231
“53495872376”,”2000-12-15 09:34:45”,”Aliquam erat volutpat”,-43.543223486,-19.84123876412
“53495872376”,”2001-01-09 13:43:10”,”Nullam feugiat sem malesuada”,-44.24321348123,-19.28327462
“53495872376”,”2000-02-01 16:34:54”,”Vestibulum pretium elementum nisi”,-44.12782362,-19.12361823
“53487562533”,”2000-02-10 12:23:58”,”Nulla eleifend facilisis dui”,-43.54234659823,-20.12423764
“43248652345”,”2000-11-09 20:19:39”,”Sed quis felis venenatis”,-43.412846213,-19.4128364213
“43248652345”,”2000-12-01 19:01:44”,”Etiam vulputate ipsum”,-43.982374523,-20.123184621

Observações:
- A tabela deverá ser limpa antes de ser carregada;
- O arquivo CSV poderá ter milhares de linhas, desta forma, dê COMMIT a cada 1000 registros inseridos.

# ATIVIDADE_1_2_modelagem_script_teste_banco_digicade.sql

use digicade;

create table CLIENTE
(
   ID_CLIENTE           int not null,
   CPF_CLIENTE          varchar(11)
);

alter table CLIENTE
   add primary key (ID_CLIENTE);
   
alter table CLIENTE
   change ID_CLIENTE ID_CLIENTE int not null auto_increment;

create table OCORRENCIA
(
   ID_OCORRENCIA        int not null,
   ID_CLIENTE           int not null,
   DT_OCORRENCIA        datetime,
   DSC_OCORRENCIA       varchar(100),
   LONGITUDE            numeric (14, 11),
   LATITUDE             numeric (14, 11)
);

alter table OCORRENCIA
   add primary key (ID_OCORRENCIA, ID_CLIENTE);

alter table OCORRENCIA
   add unique AK_Key_2 (ID_CLIENTE);
   
alter table OCORRENCIA
   add unique AK_Key_3 (DT_OCORRENCIA);
   
alter table OCORRENCIA
   change ID_OCORRENCIA ID_OCORRENCIA int not null auto_increment;

alter table OCORRENCIA add constraint FK_Cliente_Ocorrencia_FK foreign key (ID_CLIENTE)
      references CLIENTE (ID_CLIENTE);

create table STG_OCORRENCIAS
(
   CPF_CLIENTE          varchar(11),
   DATA_HORA            datetime,
   DESCRICAO            varchar(100),
   LONGITUDE            numeric (14, 11),
   LATITUDE             numeric (14, 11)
);

2- A tabela “STG_OCORRENCIAS”, que foi carregada na questão anterior, agora servirá de base para atualizar a tabela definitiva, que se chama “OCORRENCIA”. 

- Campos da tabela “OCORRENCIA”:
   - ID: chave primária da tabela, que obtem o seu valor a partir da sequence “SQ_OCORRENCIA”;
   - ID_CLIENTE: referência externa à tabela “CLIENTE”;
   - DT_OCORRENCIA: campo de tipo DATE;
   - DSC_OCORRENCIA: campo texto do tipo VARCHAR2(4000);
   - LONGITUDE: campo do tipo NUMBER;
   - LATITUDE: campo do tipo NUMBER,

- Instruções:
   - A carga deverá ser feita através da linguagem procedural do banco de dados escolhido na questão 1;
   - O valor do campo ID_CLIENTE deve ser obtido da tabela “CLIENTE”;
   - A tabela “CLIENTE”, possui o campo ID, que é sua chave primária, o campo CPF e outros;
   - Os campos ID_CLIENTE e DT_OCORRENCIA da tabela “OCORRENCIA” são uma chave única;
   - Caso já exista um registro com o mesmo ID_CLIENTE e DT_OCORRENCIA vindo da carga, os campos DSC_OCORRENCIA, LONGITUDE e LATITUDE deverão ser atualizados, caso contrário deverá ser inserido um novo registro;

Observações:
- Como a tabela “STG_OCORRENCIAS” poderá conter milhares de registros, o COMMIT deverá ser dado a cada 1000 registros processados.

3 – Elaborar uma consulta SQL utilizando as tabelas “OCORRENCIA” e “CLIENTE”, que retorne as seguintes informações:

- CPF do cliente;
- Data da última ocorrência do cliente;
- Descrição da última ocorrência do cliente;
- Longitude e latitude da última ocorrência do cliente.

Regras e filtros:
- Retornar somente as ocorrências que estejam dentro do retângulo delimitado entre as longitudes -44.15 e -43.82, e as latitudes -20.23 e -19.91;
- Retornar somente um registro para cada cliente, o registro retornado deverá ser o que tenha a maior data de ocorrência, ou seja, a última ocorrência do cliente.

# ATIVIDADE_3_consulta.sql

3 – Elaborar uma consulta SQL utilizando as tabelas “OCORRENCIA” e “CLIENTE”, que retorne as seguintes informações:

- CPF do cliente;
- Data da última ocorrência do cliente;
- Descrição da última ocorrência do cliente;
- Longitude e latitude da última ocorrência do cliente.

Regras e filtros:
- Retornar somente as ocorrências que estejam dentro do retângulo delimitado entre as longitudes -44.15 e -43.82, e as latitudes -20.23 e -19.91;
- Retornar somente um registro para cada cliente, o registro retornado deverá ser o que tenha a maior data de ocorrência, ou seja, a última ocorrência do cliente.


SELECT 
    dc.CPF_CLIENTE,
    MAX(dio.DT_OCORRENCIA),
    dio.DSC_OCORRENCIA,
    dio.LONGITUDE,
    dio.LATITUDE
FROM
    digicade.cliente dc
        INNER JOIN
    digicade.ocorrencia dio ON (dio.ID_CLIENTE = dc.ID_CLIENTE)
WHERE
    dio.LONGITUDE BETWEEN '-44.15' AND '-43.82'
        AND LATITUDE BETWEEN '-20.23' AND '-19.91'
GROUP BY CPF_CLIENTE;
