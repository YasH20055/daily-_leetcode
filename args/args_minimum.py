def find_min(*args):
  smaller_number=args[0]
  for i in args:
    if i <smaller_number:
      smaller_number= i
  return smaller_number
result = find_min(45, 12, 78, -5, 23, 9)
print(result)
