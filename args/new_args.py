def get_even(*args):
  # total=0
  new_list=[]
  for i in args:
    if i%2==0:
      new_list.append(i)
      # total=total+new_list
  return new_list
def get_total(new_list):
  total=0
  for j in new_list:
    total+=j
  return total

result = get_even(3, 8, 11, 14, 17, 20, 25, 30)
final=get_total(result)
print(final)
