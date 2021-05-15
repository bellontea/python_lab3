from random import sample
import string
 
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
 
def generate_password(m):
    return ''.join(sample(symbols,m))
 
def main(n, m):
    lst = set()
    while len(a) < n:
        lst.add(generate_password(m))
    return lst