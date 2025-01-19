# Bitcoin Wallet CLI

Este é um projeto simples de uma CLI para manipulação de uma carteira Bitcoin em um ambiente de teste local (regtest). A ferramenta permite criar endereços Bitcoin, consultar saldos e enviar transações, integrando-se a um nó Bitcoin Core em modo regtest

- [dojo-bitcoin](https://github.com/nrxschool/dojo-bitcoin/tree/main)
- [Zackson Pessoa](https://github.com/ZacksonPessoa)

## Requisitos

- **Python 3.12** ou superior  
- **Bitcoin Core** instalado e configurado no modo regtest  
- **Ambiente virtual Python** (`venv`)

O projeto foi testado e na máquina local fazendo requisições ao nó configurado em um servidor Ubuntu 24.04.1.

> [!NOTE] 
> 0no arquivo rpc_client.py 
> substitua esses trecho pelo configuração do seu nó regtest
```sh 
       command = [
            "ssh", "seu acesso",
            "bitcoin-cli -regtest -rpcuser="You_user" -rpcpassword="you_password" getnewaddress"
        ]
```





## Installation

1 - Clonar o repositório:

```sh
git clone https://github.com/ZacksonPessoa/bitcoin-wallet-cli.git
cd bitcoin-wallet-cli
```

2 - Criar e ativar o ambiente virtual:

```sh
python3.12 -m venv venv
source venv/bin/activate
```
3 - Instalar dependências:

```sh
pip install -r requirements.txt
```

## Comandos Disponíveis


##### Criar um novo endereço

Gera um novo endereço Bitcoin e o salva em um arquivo JSON.
Uso:
```sh
python wallet.py create --wallet_name <nome_da_carteira>
```
Exemplos:
```sh
python wallet.py create --wallet_name testwallet
```
#### Listar endereços existentes
Lista todos os endereços salvos na carteira.
Uso:

```sh
python wallet.py list_address
```
#### Consultar saldo total
Retorna o saldo total disponível.
Uso:
```sh
python wallet.py balance
```
Exemplo: 
```sh
python wallet.py balance
```

#### Consultar saldo detalhado por endereço
Exibe o saldo de cada endereço registrado.
Uso:
```sh
python wallet.py balance --detailed
```

#### Consultar saldo de um endereço específico
Consulta o saldo de um único endereço fornecido
Uso:
```sh
python wallet.py balance --address <endereco_bitcoin>
```
Exemplo:
```sh
python wallet.py balance --address bcrt1qexampleaddress123
```
#### Enviar bitcoins
Transfere uma quantidade especificada de bitcoins de um endereço para outro.
Uso:
```sh
python wallet.py send --from_address <endereco_origem> --to_address <endereco_destino> --amount <quantidade>
```
Exemplos:
```sh
python wallet.py send --from_address bcrt1qexamplefrom --to_address bcrt1qexampleto --amount 1.0
```



## Estrutura do Projeto
```sh
        bitcoin-wallet-cli/
       ├── modules/
       │   ├── rpc_client.py         # Comunicação com o nó Bitcoin Core
       │   ├── wallet_handler.py     # Manipulação do arquivo JSON da carteira
       ├── wallet.py                 # Arquivo principal da CLI
       ├── requirements.txt          # Dependências do projeto
       ├── wallet.json               # Arquivo de endereços gerados (criado >automaticamente)
````



## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
