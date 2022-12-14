from flask import Flask, render_template
from time import time


class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        # Create genesis block
        self.create_block(0, '00')

    def create_block(self, nonce, previous_hash):
        """
        Adds a block of transactions to the blockchain
        :param nonce:
        :param previous_hash:
        :return:
        """
        block = {'block_number': len(self.chain) + 1,
                 'timestamp': time(),
                 'transactions': self.transactions,
                 'nonce': nonce,
                 'previous_hash': previous_hash}

        # Reset the current list of transactions
        self.transactions = []


# instantiate the blockchain
blockchain = Blockchain()

# instantiate the node
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('./index.html')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
