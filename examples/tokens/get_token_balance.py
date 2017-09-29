from etherscan.tokens import Tokens
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

#  tokenname options msut be address of token contract

address = '0xB432aD51fF09623F37690b5C14e7fDdee21A8952'
api = Tokens(contractaddress='0x08f5a9235b08173b7569f83645d2c7fb55e8ccd8', api_key=key)
address = '0x0a869d79a7052c7f1b55a8ebabbea3420f0d1e13'
balance = api.get_token_balance(address=address)
print(balance)
