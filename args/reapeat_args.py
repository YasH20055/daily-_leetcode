def count_value(*args,value):
  count=0
  for i in args:
    if i==value:
      count+=1
  print(count) 
count_value(10, 20, 10, 30, 10, 40, 10, value=10)
count_value(5, 7, 5, 9, 5, value=5)
