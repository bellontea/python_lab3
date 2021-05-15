import random
 
s1 = "ABCDEFGHJKLMNPQRSTUVWXYZ"
s2 = "abcdefghijkmnpqrstuvwxyz"
s3 = "23456789"
s4 = s1 + s2 + s3
 
 
def generate_password(m):
    passw = []
    passw.append(random.choice(s1))
    passw.append(random.choice(s2))
    passw.append(random.choice(s3))
    for i in range(0, m - 3):
        passw.append(random.choice(s4))
    random.shuffle(passw)
    return ''.join(passw)
 
 
def main(n, m):
    lst = set()
    while len(lst) < n:
        lst.add(generate_password(m))
    return lst