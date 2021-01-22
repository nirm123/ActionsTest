import hashlib

with open('netid.txt') as f:
    netid = f.readline()

hash_object = hashlib.sha256(b'Hello World')
print(hash_object.hexdigest()[:5])
