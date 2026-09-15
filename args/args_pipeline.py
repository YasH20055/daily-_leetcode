def new_numbers(*args):
  new_list=[]
  for i in args:
    if i%2==0 and i>10:
      new_list.append(i*i)
  return new_list
def process_numbers(new_list):
  count=0
  for i in new_list:
    count+=i
  return count
result = new_numbers(3, 12, 15, 18, 7, 20, 25, 30)
final=process_numbers(result)
print(final)
