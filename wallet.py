import argparse
from modules.rpc_client import get_new_address, get_balance, send_to_address, get_received_by_address
from modules.wallet_handler import save_address, list_addresses
import re

def is_valid_bitcoin_address(address):
    """Validate the format of a Bitcoin address (including Bech32)."""
    return bool(re.match(r'^(bcrt|1|3)[a-zA-HJ-NP-Z0-9]{25,}$', address))

def main():
    parser = argparse.ArgumentParser(description="Bitcoin Wallet CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command 'create'
    create_parser = subparsers.add_parser(
        "create",
        help="Generate a new Bitcoin address and save it to a wallet"
    )
    create_parser.add_argument(
        "--wallet_name", "-w",
        required=True,
        help="Name of the wallet (required)"
    )

    # Command 'balance'
    balance_parser = subparsers.add_parser("balance", help="Check balance of the wallet")
    balance_parser.add_argument(
        "--address", "-a",
        help="Address to check balance for"
    )
    balance_parser.add_argument(
        "--detailed", "-d",
        action="store_true",
        help="Show balance details for all addresses"
    )

    # Command 'send'
    send_parser = subparsers.add_parser("send", help="Send Bitcoin to an address")
    send_parser.add_argument("--from_address", required=True, help="Source Bitcoin address")
    send_parser.add_argument("--to_address", required=True, help="Destination Bitcoin address")
    send_parser.add_argument("--amount", type=float, required=True, help="Amount of Bitcoin to send")

    # Command 'list_address'
    subparsers.add_parser("list_address", help="List all wallet addresses")

    args = parser.parse_args()

    if args.command == "create":
        try:
            new_address = get_new_address()
            save_address(args.wallet_name, new_address)
            print(f"Success: New address '{new_address}' created and saved to wallet '{args.wallet_name}'.")
        except Exception as e:
            print(f"Error: Could not create a new address. Details: {e}")

    elif args.command == "balance":
        try:
            if args.address:
                # Verificar o saldo de um endereço específico
                received = get_received_by_address(args.address)
                print(f"Balance for address {args.address}: {received:.8f} BTC")
            elif args.detailed:
                # Listar saldos detalhados de todos os endereços
                print("Detailed balance by address:")
                addresses = list_addresses()
                for addr in addresses:
                    received = get_received_by_address(addr["address"])
                    print(f"  Address: {addr['address']} | Balance: {received:.8f} BTC")
            else:
                # Mostrar o saldo total
                total_balance = get_balance()
                print(f"Wallet total balance: {total_balance:.8f} BTC")
        except Exception as e:
            print(f"Error: Could not retrieve balance. Details: {e}")

    elif args.command == "send":
        # Verifique a validade dos endereços
        if not is_valid_bitcoin_address(args.from_address):
            print("Error: Invalid source Bitcoin address format.")
            return

        if not is_valid_bitcoin_address(args.to_address):
            print("Error: Invalid destination Bitcoin address format.")
            return

        if args.amount <= 0:
            print("Error: Amount must be greater than zero.")
            return

        # Se os endereços forem válidos, envie a transação
        try:
            tx_id = send_to_address(args.to_address, args.amount)
            print(f"Success: Sent {args.amount} BTC from {args.from_address} to {args.to_address}. Transaction ID: {tx_id}")
        except Exception as e:
            print(f"Error: Could not send Bitcoin. Details: {e}")

    elif args.command == "list_address":
        try:
            addresses = list_addresses()
            if not addresses:
                print("No addresses found.")
            else:
                print("List of addresses:")
                for entry in addresses:
                    print(f"Wallet: {entry['wallet_name']}, Address: {entry['address']}")
        except Exception as e:
            print(f"Error: Could not list addresses. Details: {e}")

if __name__ == "__main__":
    main()
