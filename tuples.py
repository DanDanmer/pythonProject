# milk_info = ("lactose", "11/08/2022", "dairy cows", "135.6 liters", 300)
# print(len(milk_info))
# print(milk_info[0])
# print(milk_info[2:])
# print(str(milk_info[4]) + " " + milk_info[2])
#
# for info in milk_info:
#     print("-- " + str(info) + " --" )
from wsgiref.validate import validator


# def picnic_shopping(list_of_prices):
#     total = sum(list_of_prices)
#     is_total_ok = total < 150
#
#     return total, is_total_ok
#
# prices_for_picnic = [17.90, 23.5, 85]
# money, is_budget_possible = picnic_shopping(prices_for_picnic)
# print(picnic_shopping(prices_for_picnic))

# def sum_and_avg(a, b):
#     sum_num = a + b
#     avg_num = (a + b) / 2
#     return sum_num, avg_num
#
# x , y = sum_and_avg(3, 6)
#
# print(y, x)

# data = ("self", "py", 1.543)
# format_string = "Hello {} {}. {} learner, you have only {} units left before you master the course!"
#
# formatted_string = format_string.format(data[0], data[1], data[2], 1.543)
# print(formatted_string)

# """
# Or..
# data = ("self", "py", 1.543)
# format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
#
# print(format_string % data)
#
# """
# def sort_prices(list_of_tuples):
#
#     sorted_list = sorted(list_of_tuples, key=lambda tup: float(tup[1]), reverse=True)
#     return sorted_list
#
# products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
# sorted_products = sort_prices(products)
#
# print(sorted_products)

# def mult_tuple(tuple1, tuple2):
#     result = []  # רשימה שתאחסן את כל הזוגות
#     for item1 in tuple1:  # עוברים על כל איבר בטאפל הראשון
#         for item2 in tuple2:  # עוברים על כל איבר בטאפל השני
#             result.append((item1, item2))  # מוסיפים זוג מהטאפל הראשון והשני
#             result.append((item2, item1))  # מוסיפים זוג מהטאפל השני והראשון
#
#     return tuple(result)

def sort_anagrams(list_of_strings):
    anagrams = {}

    for word in list_of_strings:

        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
                 'ternaries', 'smelters', 'termless', 'salted',
                 'staled', 'greatening', 'lasted', 'resmelts']
result = sort_anagrams(list_of_words)
print(result)


