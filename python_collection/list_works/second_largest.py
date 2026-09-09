placement_counts = [10,15,22,9,17,18]

print("second largest placement count----")

largest = placement_counts[0]

second_largest = placement_counts[0]

for count in placement_counts:

    if count > largest:

        second_largest = largest

        largest = count

    elif count > second_largest:

        second_largest = count

print(second_largest)