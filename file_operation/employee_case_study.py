fr = open("file_operation\\employee.csv")

employees = []

for line in fr:

    line = line.rstrip("\n")

    id,name,department,salary,location = line.split(",")

    emp_dict = {"id":id,"name":name,"department":department,"salary":salary,"location":location}

    employees.append(emp_dict)

print(employees)