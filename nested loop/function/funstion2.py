numbers = [4, 7, 10, 13, 16, 19, 22]
def find_greater(numbers):
  first=[]
  for i in numbers:
    if i>10:
      first.append(i)
  return first
def get_squre(first):
  sec=[]
  for j in first:
    sec.append(j*j)
    
  return sec
def get_total(sec):
  t=0
  for k in sec:
    t+=k
  return t
a=find_greater(numbers)
b=get_squre(a)
c=get_total(b)
print(c)