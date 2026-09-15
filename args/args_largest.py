def find_max(*args):
  larger=0
  for i in args:
    if i >larger:
      larger=i
  return larger
result = find_max(12, 45, 7, 89, 23, 56)
print(result)
