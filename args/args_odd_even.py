def analyze_numbers(*args):
  odd_count=0
  even_count=0
  for i in args:
    if i%2==0:
      even_count+=1
    else:
      odd_count+=1
  return even_count,odd_count
result = analyze_numbers(10, 15, 20, 23, 30, 35, 40)
print(result)
