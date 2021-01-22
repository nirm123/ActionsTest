import hashlib

with open('netid.txt') as f:
    netid = f.readline()

# Generate secret
secret = hashlib.sha256(b'Hello World').hexdigest()[:5]

with open('secret.txt', 'w') as f:
    if len(netid) != 0:
        f.write(secret)
    else:
        f.write('netid.txt is empty')
