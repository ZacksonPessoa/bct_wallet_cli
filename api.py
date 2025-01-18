from flask import Flask, request, jsonify
from modules.rpc_client import get_new_address, get_balance, send_to_address, get_received_by_address
from modules.wallet_handler import save_address, list_addresses

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_address():
    data = request.get_json()
    wallet_name = data.get('wallet_name')
    if not wallet_name:
        return jsonify({'error': 'wallet_name is required'}), 400

    try:
        new_address = get_new_address()
        save_address(wallet_name, new_address)
        return jsonify({'success': True, 'address': new_address}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/balance', methods=['GET'])
def get_wallet_balance():
    detailed = request.args.get('detailed', 'false').lower() == 'true'

    try:
        total_balance = get_balance()
        response = {'total_balance': total_balance}

        if detailed:
            addresses = list_addresses()
            response['detailed'] = [
                {
                    'address': addr['address'],
                    'balance': get_received_by_address(addr['address'])
                } for addr in addresses
            ]

        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send', methods=['POST'])
def send_transaction():
    data = request.get_json()
    from_address = data.get('from_address')
    to_address = data.get('to_address')
    amount = data.get('amount')

    if not from_address or not to_address or not amount:
        return jsonify({'error': 'from_address, to_address, and amount are required'}), 400

    try:
        tx_id = send_to_address(from_address, to_address, amount)
        return jsonify({'success': True, 'transaction_id': tx_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
