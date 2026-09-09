fr_all_students = open("file_operation\\all_students.txt","r")

fr_passed_students = open("file_operation\\passed_students.txt","r")

fw_failed_students = open("file_operation\\failed_students.txt","w")

all_students = {name.rstrip("\n") for name in fr_all_students}

passed_students = {name.rstrip("\n") for name in fr_passed_students}

failed_students = all_students.difference(passed_students)

for student in failed_students:

    fw_failed_students.write(student +"\n")

print("completed...")



    