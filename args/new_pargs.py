def get_greater(limit, *args):
  new_list=[]
  for i in args:
    if i> limit:
      new_list.append(i)
  return new_list
result = get_greater(10, 4, 15, 7, 20, 3, 25, 12)
print(result)
