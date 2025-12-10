import requests
import sqlite3 ##Banco de dados relaciona que já vem com  o python


DB_NOME = "registroConsultaCEP.db" ## nome do banco de dados  que será criado

cep = input("Digite o CEP que deseja consultar: ") ## 8 números, sem hífen ou ponto

link = f"https://viacep.com.br/ws/{cep}/json/" ## Link que será utilizado na requisição GET, após receber o CEP digitado

requisicao = requests.get(link) ## requisição GET
print(requisicao) ##se retornar 200, significa que a conexão foi bem sucedida

dados = requisicao.json() ## A parte relevante é o .json() que vai retornar os dados json da API obtidos pela requisição GET

##print(dados) ## Printa todos os dados da requisição, bom pra saber quais dados a API informa


logradouro = dados["logradouro"] ## Salva uma variável apenas com um dos dados obtidos na requisição
complemento = dados["complemento"]
localidade = dados["localidade"]
estado = dados["estado"]
uf = dados["uf"]

print(f"{logradouro}, {complemento}, {localidade}, {estado} - {uf}")

def criar_tabela(): ## função para criar a tabela onde salvarei os registros
    conectar = sqlite3.connect(DB_NOME)
    cursor = conectar.cursor() #isso  envia os comandos sql
    consulta = sqlite3.connect(DB_NOME)
    
    ### os """ são obrigaorios
    cursor.execute(""" #enviando o comando para criar a tabela
                    CREATE TABLE IF NOT EXISTS enderecos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cep TEXT NOT NULL,
                        logradouro TEXT,
                        bairro TEXT,
                        localidade TEXT,
                        uf TEXT
                    );
    """
    )
    
    conectar.commit() #commit da criação
    conectar.close()
    
def salvar_dados_API (cep, dados): #salvado os dados que vamos pegar
    logradouro = dados.get("logradouro") 
    complemento = dados.get("complemento")
    localidade = dados.get("localidade")
    estado = dados.get("estado")
    uf = dados.get("uf")
    
    cursor.executed("""
        
        INSERT INTO enderecos (cep, logradouro, complemento, bairro, localidade, uf)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (cep, logradouro, complemento, bairro, localidade, uf))

    consulta.commit()
    consulta.close()                
                    
    print("Endereço salvo no banco de dados (SQLite).")      
    