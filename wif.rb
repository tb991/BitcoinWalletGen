
require 'digest'

# Checksums use hash256 (where data is hashed twice through sha256)
def hash256(hex)
    binary = [hex].pack("H*")
    hash1 = Digest::SHA256.digest(binary)
    hash2 = Digest::SHA256.digest(hash1)
    result = hash2.unpack("H*")[0]
    return result
end

# Checksums are used when creating addresses
def checksum(hex)
  hash = hash256(hex) # Hash the data through SHA256 twice
  return hash[0...8]  # Return the first 4 bytes (8 characters)
end

def base58_encode(hex)
  @chars = %w[
      1 2 3 4 5 6 7 8 9
    A B C D E F G H   J K L M N   P Q R S T U V W X Y Z
    a b c d e f g h i j k   m n o p q r s t u v w x y z
]
  @base = @chars.length

  i = hex.to_i(16)
  buffer = String.new

  while i > 0
    remainder = i % @base
    i = i / @base
    buffer = @chars[remainder] + buffer
  end

  #! Is it just the 00, or does 05 get converted to 3, etc.
  # add '1's to the start based on number of leading bytes of zeros
  leading_zero_bytes = (hex.match(/^([0]+)/) ? $1 : '').size / 2

  ("1"*leading_zero_bytes) + buffer
end



# Convert Private Key to WIF
privatekey = "<paste hex of pvt key here but REMEMBER TO DELETE EVENTUALLY>"

extended = "80" + privatekey + "01"
extendedchecksum = extended + checksum(extended)
wif = base58_encode(extendedchecksum)

puts wif
