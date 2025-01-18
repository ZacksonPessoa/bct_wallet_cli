


# Bitcoin Wallet CLI
Bitcoin Wallet CLI
Este é um projeto simples de uma CLI para manipulação de uma carteira Bitcoin em um ambiente de teste local (regtest). A ferramenta permite criar endereços Bitcoin, consultar saldos e enviar transações, integrando-se a um nó Bitcoin Core em modo regtest.

Requisitos
Python 3.12 ou superior
Bitcoin Core instalado e configurado no modo regtest
Ambiente virtual Python (venv)
Instalação
Clonar o repositório:

bash
Copiar
git clone https://github.com/ZacksonPessoa/bct_wallet_cli
cd bitcoin-wallet-cli
Criar e ativar o ambiente virtual:

bash
Copiar
python3.12 -m venv venv
source venv/bin/activate
Instalar dependências:

bash
Copiar
pip install -r requirements.txt
Configurar o nó Bitcoin regtest: Certifique-se de que o Bitcoin Core está rodando no modo regtest. Por exemplo:

bash
Copiar
bitcoind -regtest -daemon
Para consultar o estado da blockchain em regtest:

bash
Copiar
bitcoin-cli -regtest getblockchaininfo
Comandos Disponíveis
Criar um novo endereço
Gera um novo endereço Bitcoin e o salva em um arquivo JSON.

Uso:

bash
Copiar
python wallet.py create --wallet_name <nome_da_carteira>
Exemplo:

bash
Copiar
python wallet.py create --wallet_name testwallet
Listar endereços existentes
Lista todos os endereços salvos na carteira.

Uso:

bash
Copiar
python wallet.py list_address
Consultar saldo total
Retorna o saldo total disponível.

Uso:

bash
Copiar
python wallet.py balance
Exemplo:

bash
Copiar
python wallet.py balance
Consultar saldo detalhado por endereço
Exibe o saldo de cada endereço registrado.

Uso:

bash
Copiar
python wallet.py balance --detailed
Consultar saldo de um endereço específico
Consulta o saldo de um único endereço fornecido.

Uso:

bash
Copiar
python wallet.py balance --address <endereco_bitcoin>
Exemplo:

bash
Copiar
python wallet.py balance --address bcrt1qexampleaddress123
Enviar bitcoins
Transfere uma quantidade especificada de bitcoins de um endereço para outro.

Uso:

bash
Copiar
python wallet.py send --from_address <endereco_origem> --to_address <endereco_destino> --amount <quantidade>
Exemplo:

bash
Copiar
python wallet.py send --from_address bcrt1qexamplefrom --to_address bcrt1qexampleto --amount 1.0
Estrutura do Projeto
bash
Copiar
bitcoin-wallet-cli/
├── modules/
│   ├── rpc_client.py         # Comunicação com o nó Bitcoin Core
│   ├── wallet_handler.py     # Manipulação do arquivo JSON da carteira
├── wallet.py                 # Arquivo principal da CLI
├── requirements.txt          # Dependências do projeto
├── wallet.json               # Arquivo de endereços gerados (criado automaticamente)
Contribuição
Contribuições são bem-vindas! Abra um pull request ou crie uma issue se tiver ideias para melhorias.

Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
# bct_wallet_cli
