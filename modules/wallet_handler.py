import json

WALLET_FILE = "wallet.json"

def save_address(wallet_name, address):
    """Save a new address to the wallet file."""
    try:
        with open(WALLET_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append({"wallet_name": wallet_name, "address": address})

    with open(WALLET_FILE, "w") as file:
        json.dump(data, file, indent=4)

def list_addresses():
    """List all addresses saved in the wallet file."""
    try:
        with open(WALLET_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
