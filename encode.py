from web3 import Web3
import sys

def encode_function(method, args):
    w3 = Web3()
    signature = f"{method}"
    types = signature[signature.find('(')+1 : signature.find(')')].split(',')
    func_selector = w3.keccak(text=signature)[:4]
    encoded_args = w3.codec.encode_abi(types, args)
    return '0x' + (func_selector + encoded_args).hex()

if __name__ == "__main__":
    method = input("Enter method (e.g., transfer(address,uint256)): ")
    raw_args = input("Enter arguments comma-separated: ")
    args = [eval(arg.strip()) for arg in raw_args.split(',')]
    calldata = encode_function(method, args)
    print("Encoded calldata:", calldata)
