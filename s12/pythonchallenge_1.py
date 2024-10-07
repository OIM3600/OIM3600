import webbrowser


def decrypt(s):
    """Returns the decoded message"""
    res = ""
    for c in s:
        if c.isalpha():
            if c == "y":  # there must be a better/more elegant way to do this
                res += "a"
            elif c == "z":
                res += "b"
            else:
                decoded_c = chr(ord(c) + 2)
                res += decoded_c
        else:
            res += c
    return res


def main():
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(decrypt(message))
    url = "http://www.pythonchallenge.com/pc/def/map.html"
    new_url = url.replace("map", decrypt("map"))
    webbrowser.open(new_url)


main()
