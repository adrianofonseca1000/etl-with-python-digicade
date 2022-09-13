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