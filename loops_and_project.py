# user_input = 0
# while user_input not in [5, 6, 7]:
#     user_input = int(input("How many months a year do grizzly bears hibernate?"))
#     print(" You entered: ", user_input)
#
# while user_input < 10:
#     user_input += 1
#     if user_input % 2 == 0:
#         continue
#     print(user_input)
# from random import choice


# def squared_numbers(start, stop):
#     current = start
#     result = []
#
#     while current <= stop:
#         result.append(current ** 2)
#         current += 1
#
#     return result
# print(squared_numbers(4, 8))
# print(squared_numbers(5, 7))
# print(squared_numbers(-3, 8))

# animal_sounds = [["Bear", "roar"], ["dog", "bark"], ["cat", "meow"]]
#
# for item in animal_sounds:
#     print("The sound a " + item[0] +
#           " makes:\t" + item[1])
# """
# \t (Tab):
#
# Represents a horizontal tab.
# It creates spacing between elements,
# often equal to 4 or 8 spaces depending on the environment.
#
# \n (Newline):
#
# Moves the cursor to the next line,
# effectively "lowering" the text to the following line.
#     """

# range(start, stop, step)
# for num in range(5, 10, 2):
#     print(num)
#
# def is_greater(my_list, n):
#     result = []            # רשימה ריקה לאחסון האיברים הגדולים מ-n
#     for num in my_list:    # מעבר על כל איבר ברשימה
#         if num > n:        # בדיקה אם האיבר גדול מ-n
#             result.append(n)    # הוספת האיבר לרשימת התוצאות
#     return result          # החזרת הרשימה החדשה

# def numbers_letters_count(my_str):
#     num_digits = 0
#     num_others = 0
#
#     for char in my_str:
#         if char.isdigit():
#             num_digits += 1
#         else:
#             num_others += 1
#     return [num_others, num_digits]
# print(numbers_letters_count("Python 3.6.3"))

# def seven_boom(end_number):
#     result = []
#     for num in range(end_number + 1):
#
#         if num % 7 or '7' in str(num):
#             result.append("BOOM!")
#         else:
#             result.append(num)
#     return result
# print(seven_boom(27))

# def sequence_del(my_str):
#     """
#     הפונקציה מקבלת מחרוזת ומחזירה מחרוזת שבה כל רצף של תו זהה הוסרה ונשאר רק תו אחד מתוך הרצף.
#     """
#     result = []
#     for i in range(len(my_str)):  # יצירת רשימה שתחזיק את התוצאה
#         if i == 0 or my_str[i] != my_str[i - 1]: # לולאה שעוברת על כל התוים במחרוזת
#             result.append(my_str[i]) # אם התו הנוכחי שונה מהקודם
#     return ''.join(result) # מחזירים את התוצאה כמחרוזת
#
# print(sequence_del("Pythhhhhhhhooooon"))
# print(sequence_del("testttttttt"))
# print(sequence_del("yessss"))
# print(sequence_del("Tesssstt"))

# def print_products(products):
#     """ Prints the list of products. """
#     print("List of products:", products)
#
#
# def count_products(products):
#     """Prints the number of products in the list"""
#     print("Number of products in the list:", len(products))
#
#
# def check_product_exists(products):
#     """Checks if a product is in the list"""
#     product = input("Enter the product name to check if it exists in the list: ")
#     if product in products:
#         print(f"Yes, the product {product} is in the list.")
#     else:
#         print(f"No, the product {product} is not on the list.")
#
#
# def count_product_occurrences(products):
#     """Checks how many times a product appears in the list."""
#     product = input("Enter the product name to check how many times it appears: ")
#     count = products.count(product)
#     print(f"The product {product} appears {count} times.")
#
#
# def remove_product(products):
#     """Removes a product from the list"""
#     product = input("Enter the product name to remove: ")
#     if product in products:
#         products.remove(product)
#         print(f"The product {product} has been removed from the list.")
#     else:
#         print(f"The product {product} is not found in the list.")
#
#
# def add_product(products):
#     """Adds a product to the list."""
#     product = input("Enter a product name to add: ")
#     products.append(product)
#     print(f"The product {product} has been added to the list")
#
#
# def print_invalid_products(products):
#     """Prints all invalid products (less than 3 characters or non-alphabetical)"""
#     invalid_products = []
#     for product in products:
#         if len(product) < 3 or not product.isalpha():
#             invalid_products.append(product)
#     print("Invalid products: ", invalid_products)
#
#
# def remove_duplicates(products):
#     """Removes duplicates from the list."""
#     products = list(set(products))
#     print("Duplicates have been removed from the list.")
#     return products
#
#
# def main():
#     products_str = input("Enter a list of products separated by commas (no spaces): ")
#     products = products_str.split(",")  # Convert the string to a list
#
#     while True:
#         print("\nChoose an action:")
#         print("1 - Print the list of products")
#         print("2 - Print the number of products in the list")
#         print("3 - Check if a product exists in the list")
#         print("4 - Check how many times a product appears in the list")
#         print("5 - Remove a product from the list")
#         print("6 - Add a product to the list")
#         print("7 - Print invalid products")
#         print("8 - Remove duplicates")
#         print("9 - Exit")
#
#         choice = input("Choose a number (1-9): ")
#
#         if choice == '1':
#             print_products(products)
#         elif choice == '2':
#             count_products(products)
#         elif choice == '3':
#             check_product_exists(products)
#         elif choice == '4':
#             count_product_occurrences(products)
#         elif choice == '5':
#             remove_product(products)
#         elif choice == '6':
#             add_product(products)
#         elif choice == '7':
#             print_invalid_products(products)
#         elif choice == '8':
#             products = remove_duplicates(products)  # Fix: assign the updated list back to products
#         elif choice == '9':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice, please choose between 1-9.")
#
#
# # Run the program
# main()


# Practice -->
def arrow(my_char, max_length):
    """
    Generates an arrow-like pattern using the specified character and maximum length.

    Args:
        my_char (str): A single character to build the arrow.
        max_length (int): The maximum width of the arrow's middle row.

    Returns:
        str: A string representation of the arrow pattern.
    """
    lines = []
    # Create the ascending part of the arrow
    for i in range(1, max_length + 1):
        lines.append(' '.join([my_char] * i))

    # Create the descending part of the arrow
    for i in range(max_length -1, 0, -1):
        lines.append(' '.join([my_char] * i))

    return '\n'.join(lines)

print(arrow('*', 5))