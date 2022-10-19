select c.idCarro
     , c.nome 
     , c.cpf
     , c.email
     , c.telefone
     , c.endereco
  from cliente c
 order by c.nome