import hashlib

def hash256(hex):
    binary = bytes.fromhex(hex)
    hash1 = hashlib.sha256(binary).digest()
    hash2 = hashlib.sha256(hash1).digest()
    result = hash2.hex()
    return result

def checksum(hex):
    hash = hash256(hex)
    return hash[:8]

def base58_encode(hex):
    chars = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    base = len(chars)
    i = int(hex, 16)
    buffer = ''
    while i > 0:
        remainder = i % base
        i = i // base
        buffer = chars[remainder] + buffer
    leading_zero_bytes = len(hex.lstrip('0')) // 2
    return buffer

privatekey = ""
extended = "80" + privatekey + "01"
extendedchecksum = extended + checksum(extended)
wif = base58_encode(extendedchecksum)
#print(wif)

def go(pvtkey):
	extended = "80" + pvtkey + "01"
	extendedchecksum = extended + checksum(extended)
	wif = base58_encode(extendedchecksum)
	print(wif)
