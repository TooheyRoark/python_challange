text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """

def decode_text(text):
    new_text = ''
    for char in text:
        if char.isalpha():
            if ord(char) + 2 < 123:
                new_text += chr(ord(char) + 2)
            else:
                new_text += chr(ord(char) + 2 - 26)
        else:
            new_text += char
    return new_text

print decode_text(text)
print decode_text('map')

