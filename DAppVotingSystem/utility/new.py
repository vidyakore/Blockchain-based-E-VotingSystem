from solcx import compile_standard, install_solc
import json
from web3 import Web3 
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
import os
load_dotenv()

# requiremnts for conecting to chain
private_key = os.getenv("PRIVATE_KEY")
my_address = os.getenv("MY_ADDRESS")
url = os.getenv("URL")
abi = '[{"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "CandidateIdtoBool", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "CandidateIdtoName", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "string", "name": "_candidateName", "type": "string"}, {"internalType": "uint256", "name": "_candidateId", "type": "uint256"}, {"internalType": "uint256", "name": "_partyId", "type": "uint256"}], "name": "addCandidate", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "candidateIdToVotes", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "candidateId", "type": "uint256"}], "name": "getVotes", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "partyIdToCandidateId", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_candidateId", "type": "uint256"}], "name": "validCandidate", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "candidateId", "type": "uint256"}], "name": "voteForCandidate", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]'


w3 = Web3(Web3.HTTPProvider(url))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)
chain_id = 4
contract_address = '0xA4DCFE551a1dBBA59bEb6aB99e0B67A10c681Af5'

#create the contract in python
vote_contract = w3.eth.contract(address=contract_address ,abi=abi)
print(vote_contract)

nonce = w3.eth.get_transaction_count(my_address)

#  ########  #### ######## ######## ######## ######## ######## ######## ######## ######## ######## ########
#                                                                                   defining transaction body                                                                                      #
#  ########  #### ######## ######## ######## ######## ######## ######## ######## ######## ######## ########

def trx_body():
    nonce = w3.eth.get_transaction_count(my_address)
    # nonce = w3.eth.get_transaction_count(my_address)
    return {
    "gasPrice": w3.toWei('25','gwei'), 
    "chainId": chain_id, 
    "from": "0x922047D9009aE66793D0676BAB1FF031a59508cC", 
    "nonce": nonce, 
    "gas": 1000000
    }
    
    
#  ########  #### ######## ######## ######## ######## ######## ######## ######## ######## ######## ########
#                                                                                       adding a candidate                                                                                             # 
#  ########  #### ######## ######## ######## ######## ######## ######## ######## ######## ######## ########


def add_candidate(contract_instance,candidate_name,candidate_id,party_id):
    tx_body=trx_body()
    print("hello")   
    
    trx=contract_instance.functions.addCandidate(candidate_name,candidate_id,party_id).buildTransaction(tx_body)
    
    
    signed_trx=w3.eth.account.signTransaction(trx,private_key)
    
    
    trx_hash=w3.eth.sendRawTransaction(signed_trx.rawTransaction)
    
    
    tx_receipt = w3.eth.waitForTransactionReceipt(trx_hash)
    
    
    
    return tx_receipt
add_candidate(vote_contract,candidate_name="vidyunmali",candidate_id=1,party_id=2)



print("done")
print(vote_contract.functions.getVotes(2).call())


#  ########  #### ######## ######## ######## ######## ######## ######## ######## ######## ######## ########
#                                                                               Voting For A candidate                                                                                              #
#  ########  #### ######## ######## ######## ######## ######## ######## ######## ######## ######## ########


def voteForCandidate(contract_instance,candidate_id):
    tx_body=trx_body()
    print("voting")
 
    trx=contract_instance.functions.voteForCandidate(candidate_id).buildTransaction(tx_body)
    
    print("create tx")
    signed_trx=w3.eth.account.signTransaction(trx,private_key)
    
    
    print("signed")
    trx_hash=w3.eth.sendRawTransaction(signed_trx.rawTransaction)
    
    print("sent")
    tx_receipt = w3.eth.waitForTransactionReceipt(trx_hash)
    print("done")
    
    
    return tx_receipt
voteForCandidate(vote_contract,2)
print(vote_contract.functions.getVotes(2).call())

