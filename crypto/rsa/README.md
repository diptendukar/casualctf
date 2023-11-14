## NAME: 
rsa
## DESC: 
One of the most popular and longest running cryptosystem. https://en.wikipedia.org/wiki/RSA_(cryptosystem) 

Most often algorithms are fine, the implementations are not.

## POINTS: 150

## Solution:
2 ways 

1. factor N easy only 128 bits, proceed with finding d and pow(ct, d, n). Each element in the array becomes a character (demical). Concat and flag. 

OR

2. Brute force the chars in flag since flag is encrypted char by char - Select charset = uppercase+lowercase+digits+symbols . For each character -> pow(pt, e, n) and check if the index matches.
