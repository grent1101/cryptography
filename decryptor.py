import string
from collections import defaultdict

c = open('ctext.txt', 'r')
ctext = c.read()

def slicen(s, n, truncate=False):
    assert n > 0
    while len(s) >= n:
        yield s[:n]
        s = s[n:]
    if len(s) and not truncate:
        yield s


def originalText(cipher_text):
    key = [186, 31, 145, 178, 83, 205, 62]
    count = 0
    orig_text = []
    for op, code in slicen(cipher_text, 2):
        if op == '0':    op = 0
        elif op == '1':    op = 1
        elif op == '2':    op = 2
        elif op == '3':    op = 3
        elif op == '4':    op = 4
        elif op == '5':    op = 5
        elif op == '6':    op = 6
        elif op == '7':    op = 7
        elif op == '8':    op = 8
        elif op == '9':    op = 9
        elif op == 'A':    op = 10
        elif op == 'B':    op = 11
        elif op == 'C':    op = 12
        elif op == 'D':    op = 13
        elif op == 'E':    op = 14
        elif op == 'F':    op = 15
        else: op = 0
        if code == '0':    code = 0
        elif code == '1':    code = 1
        elif code == '2':    code = 2
        elif code == '3':    code = 3
        elif code == '4':    code = 4
        elif code == '5':    code = 5
        elif code == '6':    code = 6
        elif code == '7':    code = 7
        elif code == '8':    code = 8
        elif code == '9':    code = 9
        elif code == 'A':    code = 10
        elif code == 'B':    code = 11
        elif code == 'C':    code = 12
        elif code == 'D':    code = 13
        elif code == 'E':    code = 14
        elif code == 'F':    code = 15 
        else: code = 0
        hexval = ((op * 16) + code)
        x = int(hexval) ^ key[count % 7] 
        orig_text.append(chr(x)) 
        count += 1
    return("" . join(orig_text))  

otext = originalText(ctext)      

c.close()

print(otext)


