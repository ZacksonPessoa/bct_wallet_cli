import subprocess

def get_new_address():
    """Obter um novo endereço Bitcoin do nó remoto via RPC."""
    command = [
        "ssh", "seu acesso",
        "bitcoin-cli -regtest -rpcuser="user" -rpcpassword="Senha" getnewaddress"
    ]
    return subprocess.check_output(command).decode("utf-8").strip()
def get_balance():
    command = [
        "ssh", "seu acesso",
        "bitcoin-cli -regtest -rpcuser="user" -rpcpassword="Senha" 1 getbalance"
    ]
    return float(subprocess.check_output(command).decode("utf-8").strip())

def send_to_address(address, amount):
    """Envia uma transação para o endereço especificado."""
    command = [
       "ssh", "seu acesso",
        "bitcoin-cli -regtest -rpcuser="user" -rpcpassword="Senha" 1 sendtoaddress {address} {amount}"
    ]
    return subprocess.check_output(command).decode("utf-8").strip()
def get_received_by_address(address):
    """Obtém a quantidade total de bitcoins recebidos por um endereço."""
    command = [
        "ssh", "seu acesso",
        "bitcoin-cli -regtest -rpcuser="user" -rpcpassword="Senha"  getreceivedbyaddress {address}"
    ]
    return float(subprocess.check_output(command).decode("utf-8").strip())
