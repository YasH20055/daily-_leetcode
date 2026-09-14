numbers = [3, 6, 9, 12, 15]
def get_double(numbers):
  new_list=[]
  for i in numbers:
    new_list.append(i+i)
  return new_list
def get_even(new_list):
  second_list=[]
  for j in new_list:
    if j%2==0:
      second_list.append(j)
  return second_list
def get_total(second_list):
  third_list=0
  for k in second_list:
    third_list=third_list+k
  return third_list
first=get_double(numbers)
print(first)
second=get_even(first)
print(second)
third=get_total(second)
print(third)