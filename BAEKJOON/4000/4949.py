while True:
  line = input()
  line = list(line)
  if line == ['.']:
    break
  
  else:
    stack = []
    result = 'yes'
    for l in line:
      if l == '(':
        stack.append('(')
      elif l == '[':
        stack.append('[')
      elif l == ')' and len(stack) != 0:
        if stack[-1] == '(':
          stack.pop()
        else:
          result = 'no'
          break
      elif l == ']' and len(stack) != 0:
        if stack[-1] == '[':
          stack.pop()
        else:
          result = 'no'
          break
      elif (l == ')' or l == ']') and len(stack) == 0:
        result = 'no'
        break
    if line[-1] != '.' or len(stack) != 0:
      result = 'no'
    print(result)