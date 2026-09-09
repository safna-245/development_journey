# string_object.strip(value)- remove values from both ends
text = "@hello@"

new_text = text.strip("@")

print(new_text)

#string_object.lstrip(value)- remove values from beginning

word = "@hello"

new_word = word.lstrip("@")

print(new_word)

#string_object.rstrip(value)- remove values from  end

password = "hello@"

new_password=password.rstrip("@")

print(new_password)


