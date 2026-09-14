def get_numbers(*args):
  new_list=[]
  for i in args:
    if i%2==0 and i>10:
      new_list.append(i*i)
  return new_list
result = get_numbers(4, 8, 12, 15, 18, 21, 24, 30)
print(result)
