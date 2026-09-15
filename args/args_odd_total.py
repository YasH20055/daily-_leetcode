def get_odd_total(*args):
  count=0
  for i in args:
    if i%2!=0:
      count+=i
  return count
result = get_odd_total(2, 5, 8, 11, 14, 17, 20, 23)
print(result)
