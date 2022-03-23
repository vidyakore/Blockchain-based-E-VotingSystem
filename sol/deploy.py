from solcx import compile_standard, install_solc
import json
from web3 import Web3 

from web3.middleware import geth_poa_middleware 

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
# saving complied code to json
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
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
chain_id = 4
# my_address ="0x699e53bBd3B7e870432940CF856F8F54AB814E11"
# private_key = os.getenv("PRIVATE_KEY")

#create the contract in python
vote = w3.eth.contract(abi=abi,bytecode=bytecode)


#get the latest transaction

nonce = w3.eth.getTransactionCount(my_address)
print('current nonce',nonce)

# 1. Build a Transaction

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
print("Sending  Transaction to deploy")

# 3. Send a Transaction to deploy
tx_hash=w3.eth.sendRawTransaction(signed_txn.rawTransaction)



tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print("transaction delpoying Finished !*!")
print("deployed address of contract : ",tx_receipt.contractAddress)
print("deployed !*!") 
# Working with the contract 
# needs to address of deployed contract
# need to get the contract abi

# get the contract address

vote = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)

# there are two ways to interact with the contract
# 1. call() :-> It will not make a state change but it will return the value
# 2. transact() :-> It will make a state change 
#    And it will return the value and also change the state e.g. set value of x


# # calling retrieve() using call
# value = vote.functions.addCandidate("A",1,1).transact()
# print("vlaue before updatation",value)

# # using  transact() and initialising value of favourite number
print(" updating value of favourite number . . . . . .")
# 1. create a transaction
store_transaction = vote.functions.addCandidate("A",1,1).buildTransaction({
    "chainId":chain_id,
    "gasPrice":w3.eth.gas_price,
    "nonce":nonce+1,# a nonce can be used only once for a transaction
})

# 2. sign the transaction

print("signing transaction . . . . . .")

sign_store_txn = w3.eth.account.sign_transaction(store_transaction,private_key)

print("signed !*!")

# 3.Get the transaction hash or send the transaction

print("making state change . . . . . .")

store_txn_hash = w3.eth.sendRawTransaction(sign_store_txn.rawTransaction)

print("state changed made !*!")

# 4.getting txn receipt after getting mined
store_txn_receipt = w3.eth.waitForTransactionReceipt(store_txn_hash)

# # 5. get the value changed by store function
value = vote.functions.get(1).call()

print('value after state change',value)


# # get the contract instance

