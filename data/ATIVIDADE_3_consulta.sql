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
