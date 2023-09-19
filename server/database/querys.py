SELECT_ALL_PESSOA = """
  SELECT * FROM pessoas
"""
SELECT_PESSOA_ID = """
  SELECT * FROM pessoas WHERE id_pessoa = %s
"""
INSERT_PESSOA = """
  INSERT INTO pessoas (nome, rg, cpf, data_nascimento, data_admissao, funcao)
  VALUES (%s, %s, %s, %s, %s, %s)
"""
SELECT_PESSOA_CPF = """
  SELECT id_pessoa FROM pessoas WHERE cpf = %s
"""
SELECT_PESSOA_RG = """
  SELECT id_pessoa FROM pessoas WHERE rg = %s
"""
UPDATE_PESSOA = """
  UPDATE pessoas SET nome = %s, funcao = %s, rg = %s, cpf = %s, data_admissao = %s, data_nascimento = %s WHERE id_pessoa = %s
"""
DELETE_PESSOA = """
  DELETE FROM pessoas WHERE id_pessoa = %s
"""