placement_counts = [10,15,22,9,17,18]

print("feb month placement count")

feb_mont_placement_count = placement_counts[1]

print(feb_mont_placement_count)

print("january month placement_count")

placement_counts[0] = 12

print(placement_counts)

print("placement count > 15:")

for count in placement_counts:

    if count > 15:

        print(count)

print("Highest placement count----")

largest = placement_counts[0]

for i in placement_counts:

    if i > largest:

        largest = i

print(largest)

print("Lowest placement count----")

lowest = placement_counts[0]

for i in placement_counts:

    if i < lowest:

        lowest = i

print(lowest)

print("second largest----")

largest = placement_counts[0]

second_largest = placement_counts[0]

for count in placement_counts:

    if count > largest:

        second_largest = largest

        largest = count

    elif count > second_largest:

        second_largest = count

print(second_largest)