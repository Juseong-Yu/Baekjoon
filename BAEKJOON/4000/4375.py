#문제 이해가 좀 어려웠음.. 입력값 n의 배수가 1, 11, 111, 1111... 이 되는 경우 이것이 몇 자리인지 구하는 문제였음

while True:
  try:
    n = int(input())
    count = 1
    while True:
      if count % n == 0:
        print(len(str(count)))
        break
      else:
        count = (count * 10) + 1
  except EOFError:
    break


