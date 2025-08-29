name = '?'
weight = '1'
age = '1'
while True:
    name,age,weight = input().split()
    if name == '#' and weight == '0' and age == '0':
        break
    elif int(age) > 17 or int(weight) >= 80:
        print(name,'Senior')
    else:
        print(name,'Junior')