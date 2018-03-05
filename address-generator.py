#it's good to comment code

from bitcoin import *      #impoting library
private_key0 = random_key()     #generating random key
print private_key0 + "\n This is generated random private key"  #printing generated key
private_key1 = "hello world"  #generating public key from given phrase
public_key1 = privtopub(private_key1)
print public_key1 + "\n This is public key from prase hello world"
