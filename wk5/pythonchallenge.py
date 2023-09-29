# Challenge 0
# print(2**38)

# Challenge  1


def decrypt(encrypted_message):
    decrypted = ''
    for c in encrypted_message:
        if c.isalpha():
            if c == 'y':  # There must be a better way
                decrypted += 'a'
            elif c == 'z':
                decrypted += 'b'
            else:
                decrypted += chr(ord(c) + 2)
        else:
            decrypted += c

    print(decrypted)


encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decrypt(encrypted)
decrypt('map')
