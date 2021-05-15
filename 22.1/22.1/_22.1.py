def encrypt_caesar(msg, shift):
    res = ""

    if (shift == 0):
        return (msg)

    for i in range(len(msg)):
        if (msg[i].isalpha() == False):
            res += msg[i]
            continue

        letter = msg[i].lower()
        j = 0
        while (chr(ord(letter) + j) != "я" and (shift - j) != 0):
            j += 1
        if (shift != j):
            j += 1
            if (msg[i].isupper()):
                res += chr(ord("а") + shift - j).upper()
            else:
                res += chr(ord("а") + shift - j)
        else:
            if (msg[i].isupper()):
                res += chr(ord(letter) + shift).upper()
            else:
                res += chr(ord(letter) + shift)

    return(res)

def decrypt_caesar(msg, shift):
    res = ""

    if (shift == 0):
        return (msg)

    for i in range(len(msg)):
        if (msg[i].isalpha() == False):
            res += msg[i]
            continue

        letter = msg[i].lower()
        j = 0
        while (chr(ord(letter) - j) != "а" and (shift - j) != 0):
            j += 1
        if (shift != j):
            j += 1
            if (msg[i].isupper()):
                res += chr(ord("я") - shift + j).upper()
            else:
                res += chr(ord("я") - shift + j)
        else:
            if (msg[i].isupper()):
                res += chr(ord(letter) - shift).upper()
            else:
                res += chr(ord(letter) - shift)

    return(res)
