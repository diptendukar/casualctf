## NAME: 
exclusive

## DESC: 
We again built an exclusive cipher. This time we are confident it cannot be broken. The key is random 8 bytes. What can go wrong?

## POINTS: 
150

## Solution - 
We get the encrypted flag which is `plaintext flag XOR key (8 radnom bytes)`. We can also interact with the program. This uses `known plaintext`. We can input 8 chars e.g. `abcdefgh` and we get the ciphertext. So CT XOR PT = key . We recover the key. Use the key to recover the plaintext flag. enc flag XOR key = pt flag. 
