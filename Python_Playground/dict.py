mariah_info = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

choice = int(input("Please enter a number between 1 to 7: "))

if choice == 1:
    print(mariah_info["last_name"])
elif choice == 2:
    print(mariah_info["birth_date"].split(".")[1])
elif choice == 3:
    print(len(mariah_info["hobbies"]))
elif choice == 4:
    print(mariah_info["hobbies"][-1])
elif choice == 5:
    mariah_info["hobbies"].append("Cooking")
    print("Added 'Cooking' to hobbies:", mariah_info["hobbies"])
elif choice == 6:
    birth_tuple = tuple(map(int, mariah_info["birth_date"].split(".")))
    print(birth_tuple)
elif choice == 7:
    current_year = 2025
    birth_year = int(mariah_info["birth_date"].split(".")[2])
    age = current_year - birth_year
    mariah_info["age"] = age
    print(age)
else:
    print("Invalid choice")

def count_chars(my_str):
    my_str = my_str.replace(" ", "")

    char_count = {}

    for char in my_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

magic_str = "abra cadabra"
print(count_chars(magic_str))

def inverse_dict(my_dict):
    inverse_dict = {}

    for key, value in my_dict.items():

        if value in inverse_dict:
            inverse_dict[value].append(key)

        else:

            inverse_dict[value] = [key]

    for key in inverse_dict:
        inverse_dict[key].sort()

    return inverse_dict
course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
