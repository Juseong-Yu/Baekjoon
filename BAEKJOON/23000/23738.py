arr = list(input())
dic = {
    'A' : 'a',
    'K' : 'k',
    'M' : 'm',
    'O' : 'o',
    'T' : 't',
    "B" : 'v',
    'E' : 'ye',
    'H' : 'n',
    'P' : 'r',
    'C' : 's',
    'Y' : 'u',
    'X' : 'h'
    }
result = ''
for ele in arr:
    result += dic[ele]
print(result)