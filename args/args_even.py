def show_numbers(*args):
  for number in args:
    if number%2==0:
      print(number)
    

show_numbers(10, 15, 20, 23, 30, 35, 40)