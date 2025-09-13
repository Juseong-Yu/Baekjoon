month = int(input())
day = int(input())

if month < 2 or (month == 2 and day < 18):
    result = 'Before'
elif month == 2 and day == 18:
    result = 'Special'
else:
    result = 'After'

print(result)