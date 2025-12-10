import requests

cep = input("Digite o CEP que deseja consultar: ")

link = f"https://viacep.com.br/ws/{cep}/json/" ## Link que será utilizado na requisição GET, após receber o CEP digitado

requisicao = requests.get(link) ## requisição GET
print(requisicao) ##se retornar 200, significa que a conexão foi bem sucedida

dados = requisicao.json() ## A parte relevante é o .json() que vai retornar os dados json da API obtidos pela requisição GET

##print(dados) ## Printa todos os dados da requisição

logradouro = dados["logradouro"] ## Salva uma variável apenas com um dos dados obtidos na requisição
complemento = dados["complemento"]
localidade = dados["localidade"]
estado = dados["estado"]
uf = dados["uf"]

print(f"{logradouro}")