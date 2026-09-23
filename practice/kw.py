def get_salary(**kwargs):
  kwargs.get("salary", "Salary not provided")
    
  return kwargs.get("salary", "Salary not provided")
  
result = get_salary(name="Yash", salary=90000, department="Robotics")
print(result)
result = get_salary(name="Yash", salary=90000, department="Robotics")
print(result)

result = get_salary(name="Yash", department="Robotics")
print(result)
