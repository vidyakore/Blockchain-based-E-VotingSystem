from solcx import compile_standard, install_solc
import json
from web3 import Web3 
from dotenv import load_dotenv
import os
load_dotenv()


with open("vote.sol", "r") as file:
    vote_file = file.read()
    
# compiled solidity

install_solc("0.6.0")
compiled_sol = compile_standard(
    {    
        "language": "Solidity",
        "sources": {"vote.sol": {"content": vote_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}

            }
        }
    },
    solc_version="0.6.0"
)

with open("compiled_code.json","w") as file:
    json.dump(compiled_sol,file)
    
    
#getting bytecode
bytecode = compiled_sol["contracts"]["vote.sol"]["vote"]["evm"]["bytecode"]["object"]

#getting ABI

abi=compiled_sol["contracts"]["vote.sol"]["vote"]["abi"]

# requiremnts for conecting to chain
private_key = os.getenv("PRIVATE_KEY")
my_address = os.getenv("MY_ADDRESS")
url = os.getenv("URL")


w3 = Web3(Web3.HTTPProvider(url))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)
chain_id = 4

#create the contract in python
vote = w3.eth.contract(abi=abi,bytecode=bytecode)


#get the latest transaction

nonce = w3.eth.getTransactionCount(my_address)
print(my_address)


print("deploying . . . . .")
transaction = vote.constructor().buildTransaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce, 
})


print("signing transaction . . . . . .")

# 2. Sign a Transaction
signed_txn = w3.eth.account.sign_transaction(transaction,private_key)

print("signed !*!")
# 3. Send a Transaction to deploy
tx_hash=w3.eth.sendRawTransaction(signed_txn.rawTransaction)
print("deployed !*!") 
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Working with the contract 
# needs to address of deployed contract
# need to get the contract abi

# get the contract address
address=tx_receipt.contractAddress
with open("data.json","w") as file:
    json.dump(abi,file)
print(address)


vote = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)