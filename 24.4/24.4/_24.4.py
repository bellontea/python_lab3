dic = {}
n = int(input())
for i in range(n):
    word = input().lower()
    str = ''.join(sorted(word))
    dic[str] = dic.get(str, set())
    dic[str].add(word)
new_words = [' '.join(sorted(i)) for i in dic.values() if len(i) > 1]
print()
print(*sorted(new_words), sep='\n')
