# def shift_left(my_list):
#     return my_list[1:] + [my_list[0]]
# print(shift_left([0, 1, 2]))

# list1 = [1, 2, 3, 4]
# # list2 = [5, 6, 7]
# # list3 = list1 + list2
# # list4 = [list1 + list2]
# #
# # print(len(list2 * list1[1]))
# def format_list(my_list):
#     even_items = my_list[::2]
#
#     if len(even_items) > 1:
#         result = ", ".join(even_items[:-1]) + ", and " + even_items[-1]
#     else:
#         result = even_items[0]
#
#     return result
#
# my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
# print(format_list(my_list))

# def extend_list_x(list_x, list_y):
#     for i in range(len(list_y) - 1, -1, -1):
#         list_x.insert(0, list_y[i])
#     return list_x
#
# x = [4, 5, 6]
# y = [1, 2, 3]
# print(extend_list_x(x, y))


# def are_lists_equal(list1, list2):
#
#     return sorted(list1) == sorted(list2)
#
# list1 = [0.6, 1, 2, 3]
# list2 = [3, 2, 0.6, 1]
# list3 = [9, 0, 5, 10.5]
#
# print(are_lists_equal(list1, list2))
# print(are_lists_equal(list1, list3))

def longest(my_list):
    return max(my_list, key=len)

list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))
