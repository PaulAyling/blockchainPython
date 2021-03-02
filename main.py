import hashlib
from Block import Block

blockchain=[]

genesis_block = Block("Paul is awesome",['paul send dat 1 BTC','Jimmy sent bob 1 BTC'])
print('genesis_block:',genesis_block.block_hash)

second_block = Block(genesis_block.block_hash, ['paul sent 1 BTC to jenny!    3214321413 set 3BTC 5432543254', 'Jenny sent 4BTC to bob'])
print('second_block:',second_block.block_hash)

third_block = Block(second_block.block_hash, ['Mark sent 100BTC to Jim', 'Arnold sent 500 BTC to Greg'])
print('Third_block:',third_block.block_hash)