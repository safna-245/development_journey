student_data = [
    {"name":"anu","place":"tsr","weight":40},
    {"name":"manju","place":"pkd","weight":50},
    {"name":"anju","place":"tsr","weight":45},
    {"name":"manu","place":"ekm","weight":60},
    {"name":"ammu","place":"pkd","weight":52}
]

print(student_data[3].get("place"))

student_details = [["anu","tsr",40],
                   ["manu","pkd",60],
                   ["manju","pkd",50],
                   ["ammu","pkd",61],
                   ["anju","pkd",60]]

print(student_details[3][1])