from hashlib import sha256
nonce_max=10000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number,transactions,previous_hash, prefix_zeros  ):
    prefix_str='0'*prefix_zeros
    for nonce in range(nonce_max):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
             print(f"congratulations!,successfully mined bitcoins of nonce value:{nonce}")
             return new_hash
    raise BaseException(f"Couldn't find correct has after trying {nonce_max} times")
    return new_hash

if __name__=='__main__':
   transacations='''
   anto->chandhan->10
   felix->ajay->25 
   '''
   difficulty=6
   import time
   start=time.time()
   print("start mining")
   new_hash=mine(5,transacations,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficulty)
   total_time = str((time.time() - start))
   print(f"end mining. Mining took: {total_time} seconds")
   print(new_hash)
