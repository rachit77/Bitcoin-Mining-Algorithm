from hashlib import sha256
MAX_NONCE = 10000000     #increase according to your computational power

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash")

if __name__=='__main__':
    transactions='''
    difficulty=19 # number of leading zero's needed in new hash. 19 zeroe's are currently needed
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(689435,transactions,'00000000000000000002dc178270764a4d4acca241453e99977e21e5e09f166a', difficulty)
    total_time = str((time.time() - start))
    print(f"Mining took: {total_time} seconds")
    print(new_hash)