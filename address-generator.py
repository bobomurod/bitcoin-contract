#it's good to comment code

from bitcoin import *      #impoting library
#set_network("testnet")

private_key0 = random_key()     #generating random key
print private_key0 + "\n This is generated random private key\n"  #printing generated key
private_key1 = sha256("hello world")  #sha256 generated public key from given phrase
print private_key1 + "\private key from phrase hello world"
public_key1 = privtopub(private_key1)
print public_key1 + "\n This is public key from prase hello world"
print pubtoaddr(public_key1)
