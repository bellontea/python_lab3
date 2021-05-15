import random
 
s1 = "ABCDEFGHJKLMNPQRSTUVWXYZ"
s2 = "abcdefghijkmnpqrstuvwxyz"
s3 = "23456789"
s4 = s1 + s2 + s3
 
 
def generate_password(m):
    passw = []
    symb1 = random.choice(s1)
    symb2 = random.choice(s2)
    symb3 = random.choice(s3)
 
    if symb1 not in passw:
        passw.append(symb1)
    if symb2 not in passw:
        passw.append(symb2)
    if symb3 not in passw:
        passw.append(symb3)
    for i in range(0, m - 3):
        while True:
            symb = random.choice(s4)
            if symb not in passw:
                passw.append(symb)
                break
            else:
                continue
    random.shuffle(passw)
    return ''.join(passw)
 
 
def main(n, m):
    lst = set()
    while len(lst) < n:
        if generate_password(m) not in lst:
            lst.add(generate_password(m))
    return lst
