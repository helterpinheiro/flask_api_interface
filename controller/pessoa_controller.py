from flask import Blueprint, jsonify, request
import mysql.connector
from database.config import DB_CONFIG
from database.querys import SELECT_ALL_PESSOA, SELECT_PESSOA_ID, INSERT_PESSOA, SELECT_PESSOA_CPF, SELECT_PESSOA_RG, UPDATE_PESSOA
from utils.varificador_cpf import verificando_cpf
from dotenv import load_dotenv

load_dotenv()

pessoa = Blueprint('pessoa', __name__)

# Função para conectar ao banco de dados
def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

@pessoa.route('/api/v1/pessoas', methods=['GET'])
def listar_pessoas():
  try:
      # Conectando ao banco de dados
      connection = connect_db()
      cursor = connection.cursor(dictionary=True)

      # Executando busca
      cursor.execute(SELECT_ALL_PESSOA)

      # Recebendo todos os registros e adicionando em uma lista
      pessoas = cursor.fetchall()

      # Fechando o cursor e a conexão
      cursor.close()
      connection.close()

      return jsonify({'pessoas': pessoas})

  except Exception as e:
      return jsonify({'error': str(e)})

@pessoa.route('/api/v1/pessoas/<int:user_id>', methods=['GET'])
def buscar_pessoa_id(user_id):
    try:
      # Conectando ao banco de dados
      connection = connect_db()
      cursor = connection.cursor(dictionary=True)

      # Executando a consulta SQL para buscar o usuario pelo ID
      cursor.execute(SELECT_PESSOA_ID, (user_id,))

      # recebendo usuario encontrado
      pessoa = cursor.fetchone()

      # Fechando o cursor e a conexão
      cursor.close()
      connection.close()

      if pessoa:
          return jsonify({'pessoa': pessoa})
      else:
          return jsonify({'message': 'Usuário não encontrado'}), 404
      
    except Exception as e:
      return jsonify({'error': str(e)})

@pessoa.route('/api/v1/pessoas', methods=['POST'])
def criar_pessoa():
    try:
      # Obtendo os dados da pessoa do corpo da solicitacao
      data = request.json
      campos_obrigatorios = ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao']
      # Verificando os campos obrigatorios
      for campo in campos_obrigatorios:
        if campo not in data:
           return jsonify({
              'error': f'O campo {campo} é obrigatório'
           })
      
      # Conectando ao banco de dados
      connection = connect_db()
      cursor = connection.cursor()

      # Verificando se ja existe uma pessoa com o mesmo CPF
      cursor.execute(SELECT_PESSOA_CPF, (data['cpf'],))
      pessoa_existente_cpf = cursor.fetchone()

      if pessoa_existente_cpf:
        cursor.close()
        connection.close()
        return jsonify({
           'error': 'Já existe uma pessoa com o mesmo CPF cadastrada'
        })
      
      # Verificando se o CPF tem uma quantidade de caracteres valida
      cpf = verificando_cpf()
      
      if cpf == False:
        return jsonify({
          'error': 'Informe um CPF válido'
        })

      # Verificando se ja existe uma pessoa com o mesmo RG
      cursor.execute(SELECT_PESSOA_RG, (data['rg'],))
      pessoa_existente_rg = cursor.fetchone()

      if pessoa_existente_rg:
        cursor.close()
        connection.close()
        return jsonify({
           'error': 'Já existe uma pessoa com o mesmo RG cadastrada'
        })


      # Inserindo nova pessoa no banco de dados caso nao haja duplicatas
      cursor.execute(INSERT_PESSOA, (data['nome'], data['rg'], data['cpf'], data['data_nascimento'], data['data_admissao'], data['funcao']))

      # Commit das mudancas
      connection.commit()

      # Fechando o cursor e a conexão
      cursor.close()
      connection.close()

      return jsonify({'message': 'Pessoa criada com sucesso'})

    except Exception as e:
        return jsonify({'error': str(e)})

@pessoa.route('/api/v1/pessoas/<int:user_id>', methods=['PUT'])
def atualizar_pessoa(user_id):
  try:
    data = request.json

    # Conectando ao banco de dados
    connection = connect_db()
    cursor = connection.cursor()

    # Verificando se ja existe no banco de dados
    cursor.execute(SELECT_PESSOA_ID, (user_id,))
    pessoa_existente_id = cursor.fetchone()
    cursor.close()
    connection.close()

    if not pessoa_existente_id:
        return jsonify({'message': 'Pessoa não encontrada'}), 404
    
    # Verificando se 'nome' e 'funcao' estão presentes nos dados solicitados
    if 'nome' not in data or 'funcao' not in data:
        return jsonify({'error': 'Os campos "nome" e "funcao" são obrigatórios'}), 400
    
    # Conectando ao banco de dados
    connection = connect_db()
    cursor = connection.cursor()

    # Atualizando nome e funcao no banco de dados
    update_pessoa = (data['nome'], data['funcao'], user_id)
    cursor.execute(UPDATE_PESSOA, update_pessoa)
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({'message': 'Pessoa atualizada com sucesso'})

  except Exception as e:
    return jsonify({'error': str(e)}), 500



