try:

    fr = open("error_handling\\keyword.txt","r")

    for line in fr:

        print(line)

except Exception as e:

    print(e)

finally:

    print("db commit")

    