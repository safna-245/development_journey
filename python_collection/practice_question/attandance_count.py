"""
q3) attendance = ["p","p","a","a","o","o","h"]

    write a program to print attendance count
"""
attendance = ["p","p","a","a","o","o","h"]

attendance_set = set(attendance)

attendance_count = {}

for atd in attendance_set:

    attendance_count[atd] = attendance.count(atd)

print(attendance_count)


