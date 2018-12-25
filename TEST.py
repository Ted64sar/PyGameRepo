dop = input().split()
d = {}
d1 = {}
for i in range(len(dop)):
    s = input().split()
    for j in range(len(s)):
        if ':' in s[j]:
            word = s.pop(j)
            word1 = word.replace(':', '')
            s.insert(j, word1)
        elif ',' in s[j]:
            word = s.pop(j)
            word1 = word.replace(',', '')
            s.insert(j, word1)
    sub = s[0][::- 1]
    for j in range(1, len(s)):
        name = s[j]
        if name in d:
            d[name].append(sub)
        else:
            d[name] = [sub]
names = input().split(', ')
arg = []
for name in names:
    d1[name] = d[name]
for key, val in d1.items():
    arg.append([key, len(val)])
n = 1
while n < len(arg):
    for i in range(len(arg) - n):
        if (arg[i][1] < arg[i + 1][1] or
                (arg[i][1] == arg[i + 1][1] and arg[i][0] > arg[i + 1][0])):
            arg[i], arg[i + 1] = arg[i + 1], arg[i]
    n += 1
d[arg[0][0]].sort()
print(arg[0][0] + ': ' + ', '.join(d[arg[0][0]]))
