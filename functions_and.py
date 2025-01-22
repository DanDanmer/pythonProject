# def mystery(index):
#     print("z" * len(index))
#
# func = mystery
# func("Python")
# id(func)

# animal = "rabbit"
#
# def water():
#      animal = "goldfish"
#      print(animal)
# water()
# print(id(animal))

# def num_of_oranges(small_cups, large_cups ):
#     oranges_result = small_cups + large_cups * 3
#     return oranges_result
#
# print(num_of_oranges(8, 10))

# def amount_of_oranges(small_cups = 20, large_cups = 10):
#     oranges_result = small_cups + large_cups * 3
#     kg_result = oranges_result / 5
#     return oranges_result, kg_result
# oranges_result, kg_result = amount_of_oranges()
#
# print("Today you'll need", oranges_result, "oranges.")
# print("Buy", kg_result, "kg of oranges,")

# def profit(small_cups, large_cups,
#            price_small = 2, price_large = 5):
#     money = ((small_cups * price_small) +
#              (price_large * large_cups))
#     print("We earned", money, "shekels")
# profit(large_cups=16, small_cups=22)
#
# def add(num1, num2):
#     return num1 + num2
#
# sum = add(15, 20)
# print(sum)

# def sum_and_avg(a, b):
#     sum_num = a + b
#     avg_num = (a + b) / 2
#     return sum_num, avg_num
# print(sum_and_avg(a= 3, b= 6))
#
# def multiply(base =4, multiplier = 5):
#     print(base * multiplier)
# multiply(2, 3)
#
# def show_date(day, month, year = 2012):
#     print("Today is ",day,"/",month,"/",year)
#
# show_date(day = 15, month= 12)

# def remainder(base, divide_by = 2, show_greeting = True):
#     if show_greeting:
#         print("Welcome to my function")
#     print(base % divide_by)
# (remainder(11))

# def show_date(day, month, year=17):
#     print(day, "/", month, "/", year)
# show_date(15, )
# def last_early(my_str):
#     my_str = my_str.lower()
#
#     last_char = my_str[-1]
#
#     if last_char in my_str[:-1]:
#         return True
#     else:
#         return
# print(last_early("happy birthday"))
# print(last_early("best of luck"))
# print(last_early("Wow"))
# print(last_early("X"))

# def distance(num1 = 2, num2 = 3, num3 = 4):
#     is_close_to_num1 = abs(num1 - num2) == 1 or abs(num1 - num3) == 1
#     is_far_from_others = abs(num1 - num3) >= 2 or abs(num3 - num2) >= 2 or \
#         abs(num1 - num3) >= 2 and abs(num3 - num2) >= 2
#     return is_far_from_others and is_far_from_others
#
# print(distance(1, 2, 10))
# print(distance(2, 4, 6))
# print(distance(4, 5, 3))
# def fix_age(age):
#     if 13 <= age >= 19 and age not in(15, 16):
#         return 0
#
#     return age
#
# def filter_teens(a = 13, b = 13, c = 13):
#     a_fixed = fix_age(a)
#     b_fixed = fix_age(b)
#     c_fixed = fix_age(c)
#
#     return a_fixed, b_fixed, c_fixed
#
# print(filter_teens())
# print(filter_teens(1, 2, 3))
# print(filter_teens(12, 14, 15))
# print(filter_teens(1, 23, 1))
#
#
# def chocolate_maker(small, big, x):
#
#     big_used = min(big, x // 5)
#
#     remaining = x - big_used * 5
#
#     if remaining <= small:
#         return True
#     else:
#         return False
#
# print(chocolate_maker(3, 1, 8))
# print(chocolate_maker(3, 1, 9))
# print(chocolate_maker(3, 2, 10))

def func(num1, num2):
    """
    Computes the product of two numbers.

    Args:
        num1 (int or float): The first number
        num2 (int or float): The second number

    :Returns
        int or float: The product of num1 and num2
    """
    return num1, num2

def main():
    result = func(4, 5)
    print("The product of 4 and 5 is: ", result)

    help(func)

if __name__ == "__main__":
    main()